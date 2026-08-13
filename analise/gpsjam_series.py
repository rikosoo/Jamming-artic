#!/usr/bin/env python3
"""Monta a série temporal a partir dos diários do GPSJAM.

Lê os JSON baixados por gpsjam_fetch.py, filtra as células que caem dentro das caixas de
config.py e agrega por dia. Saída em CSV, pronta para o G1.

⚠ O formato interno do JSON do GPSJAM precisa ser confirmado com um arquivo real. A função
`extrair_celulas` isola essa dependência: quando você abrir o primeiro arquivo baixado,
ajuste só ela. O resto do script não muda.

Uso:
    python gpsjam_series.py
"""

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

from config import CAIXAS

RAIZ = Path(__file__).resolve().parent.parent
ORIGEM = RAIZ / "dados" / "bruto" / "gpsjam"
SAIDA = RAIZ / "dados" / "processado" / "gpsjam_serie.csv"


def extrair_celulas(doc):
    """Normaliza o JSON diário do GPSJAM em (lat, lon, boas, ruins).

    ⚠ AJUSTAR com um arquivo real em mãos. Os nomes abaixo são a hipótese de trabalho,
    baseada no vocabulário do próprio GPSJAM (contagem de aeronaves com boa e má precisão
    de navegação por célula). Se os campos diferirem, é aqui — e só aqui — que se mexe.
    """
    registros = doc.get("features", doc) if isinstance(doc, dict) else doc
    for r in registros:
        props = r.get("properties", r)
        lat = props.get("lat") or props.get("latitude")
        lon = props.get("lon") or props.get("longitude")
        boas = props.get("count_good") or props.get("good") or 0
        ruins = props.get("count_bad") or props.get("bad") or 0
        if lat is None or lon is None:
            continue
        yield float(lat), float(lon), int(boas), int(ruins)


def dentro(caixa, lat, lon) -> bool:
    return (
        caixa.lat_min <= lat <= caixa.lat_max and caixa.lon_min <= lon <= caixa.lon_max
    )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--origem", type=Path, default=ORIGEM)
    p.add_argument("--saida", type=Path, default=SAIDA)
    args = p.parse_args()

    arquivos = sorted(args.origem.glob("*.json"))
    if not arquivos:
        print(f"nada em {args.origem} — rode gpsjam_fetch.py primeiro")
        return 1

    # (data, caixa) -> [boas, ruins]
    agregado = defaultdict(lambda: [0, 0])

    for arq in arquivos:
        dia = arq.stem
        doc = json.loads(arq.read_text())
        for lat, lon, boas, ruins in extrair_celulas(doc):
            for nome, caixa in CAIXAS.items():
                if dentro(caixa, lat, lon):
                    acc = agregado[(dia, nome)]
                    acc[0] += boas
                    acc[1] += ruins

    args.saida.parent.mkdir(parents=True, exist_ok=True)
    with args.saida.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["data", "caixa", "aeronaves_boas", "aeronaves_ruins", "fracao_ruim"])
        for (dia, nome), (boas, ruins) in sorted(agregado.items()):
            total = boas + ruins
            fracao = ruins / total if total else ""
            w.writerow([dia, nome, boas, ruins, fracao])

    print(f"{len(agregado)} linhas → {args.saida}")
    print("Confira as primeiras linhas antes de plotar: se fracao_ruim vier vazia ou 0 em")
    print("todo lugar, o mapeamento de campos em extrair_celulas() está errado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
