#!/usr/bin/env python3
"""Extrai NACp do ADS-B cru (OpenSky) para as caixas do Ártico.

Este é o núcleo da matéria: a medida física, vinda da própria aeronave, em vez de
contagem de notificações administrativas.

Requer conta gratuita no OpenSky Network e a biblioteca `pyopensky` configurada
(~/.config/pyopensky/settings.conf ou variáveis de ambiente).

⚠ VERIFICAR: o nome da tabela e das colunas do NACp no backend Trino do OpenSky. O NACp
viaja na mensagem de *operational status* (DO-260B), que o OpenSky decodifica em tabela
própria — não está no state vector padrão. Rode primeiro com --amostra, olhe o que volta,
e ajuste CONSULTA. Uma consulta errada em 4 anos de dados custa horas.

Uso:
    python nacp_opensky.py --amostra                       # 1 dia, para conferir o schema
    python nacp_opensky.py --caixa finnmark --inicio 2022-02-01 --fim 2026-08-01
"""

import argparse
from pathlib import Path

from config import (
    ALTITUDE_MINIMA_M,
    CAIXAS,
    FAIXAS_ALTITUDE,
    NACP_DEGRADADO,
)

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "dados" / "processado"

# ⚠ Hipótese de trabalho — confirmar nomes com --amostra antes de rodar a série inteira.
CONSULTA = """
SELECT
    date_trunc('day', from_unixtime(o.mintime))            AS dia,
    o.icao24,
    min(o.nacp)                                            AS nacp_min,
    avg(s.baroaltitude)                                    AS altitude_media
FROM operational_status_data4 o
JOIN state_vectors_data4 s
    ON s.icao24 = o.icao24
   AND s.time BETWEEN o.mintime - 5 AND o.maxtime + 5
WHERE o.hour BETWEEN {inicio_h} AND {fim_h}
  AND s.hour BETWEEN {inicio_h} AND {fim_h}
  AND s.lat BETWEEN {lat_min} AND {lat_max}
  AND s.lon BETWEEN {lon_min} AND {lon_max}
  AND s.onground = false
  AND s.baroaltitude >= {alt_min}
  AND o.nacp IS NOT NULL
GROUP BY 1, 2
"""


def faixa_de(altitude_m):
    for baixo, alto in FAIXAS_ALTITUDE:
        if baixo <= altitude_m < alto:
            return f"{baixo}-{alto}"
    return "acima"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--caixa", choices=sorted(CAIXAS), default="finnmark")
    p.add_argument("--inicio", default="2022-02-01")
    p.add_argument("--fim", default="2026-08-01")
    p.add_argument(
        "--amostra",
        action="store_true",
        help="roda um único dia e imprime o resultado cru, para conferir o schema",
    )
    p.add_argument("--saida", type=Path, default=SAIDA)
    args = p.parse_args()

    try:
        import pandas as pd
        from pyopensky.trino import Trino
    except ImportError:
        print("faltam dependências: pip install -r requirements.txt")
        print("e configure as credenciais do OpenSky (ver README).")
        return 1

    from datetime import datetime, timezone

    caixa = CAIXAS[args.caixa]
    inicio = datetime.fromisoformat(args.inicio).replace(tzinfo=timezone.utc)
    fim = datetime.fromisoformat(args.fim).replace(tzinfo=timezone.utc)
    if args.amostra:
        fim = inicio.replace(hour=23, minute=59)

    sql = CONSULTA.format(
        inicio_h=int(inicio.timestamp()),
        fim_h=int(fim.timestamp()),
        lat_min=caixa.lat_min,
        lat_max=caixa.lat_max,
        lon_min=caixa.lon_min,
        lon_max=caixa.lon_max,
        alt_min=ALTITUDE_MINIMA_M,
    )

    print(f"consultando OpenSky: caixa={caixa.nome} {args.inicio}→{fim.date()}")
    df = Trino().query(sql)

    if args.amostra:
        print(df.head(30).to_string())
        print(f"\ncolunas: {list(df.columns)}  linhas: {len(df)}")
        print("Se vier vazio ou sem coluna nacp_min, ajuste CONSULTA antes de seguir.")
        return 0

    if df.empty:
        print("resultado vazio — verifique CONSULTA com --amostra")
        return 1

    df["degradado"] = df["nacp_min"] <= NACP_DEGRADADO
    df["faixa_altitude"] = df["altitude_media"].map(faixa_de)
    df["mes"] = pd.to_datetime(df["dia"]).dt.to_period("M").astype(str)

    args.saida.mkdir(parents=True, exist_ok=True)

    # Base aeronave-dia: uma aeronave que passou o dia todo na área conta uma vez.
    base = args.saida / f"nacp_{caixa.nome}_aeronave_dia.parquet"
    df.to_parquet(base)

    # G1 — série mensal
    g1 = df.groupby("mes").agg(
        aeronaves_dia=("icao24", "size"), degradadas=("degradado", "sum")
    )
    g1["fracao"] = g1["degradadas"] / g1["aeronaves_dia"]
    g1.to_csv(args.saida / f"g1_serie_mensal_{caixa.nome}.csv")

    # G2 — perfil de altitude (o gráfico da tese)
    g2 = df.groupby(["mes", "faixa_altitude"]).agg(
        aeronaves_dia=("icao24", "size"), degradadas=("degradado", "sum")
    )
    g2["fracao"] = g2["degradadas"] / g2["aeronaves_dia"]
    g2.to_csv(args.saida / f"g2_altitude_{caixa.nome}.csv")

    print(f"{len(df)} aeronave-dia → {args.saida}")
    print(f"fração degradada geral: {df['degradado'].mean():.3f}")
    print("\nLembrete: este número sozinho não significa nada. Rode também")
    print("  --caixa controle  e compare. A diferença é o resultado; o absoluto não é.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
