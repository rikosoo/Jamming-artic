#!/usr/bin/env python3
"""Monta a série temporal a partir dos diários do GPSJAM.

Lê os arquivos baixados por gpsjam_fetch.py, resolve cada célula H3 em coordenadas,
filtra pelas caixas de config.py e agrega por dia e por caixa. Saída em CSV, pronta
para o G1.

Sobre o conteúdo: o GPSJAM classifica cada célula pela fração de aeronaves que reportaram
qualidade de navegação degradada em 24h — verde < 2%, amarelo 2–10%, vermelho > 10%.
O cálculo dele subtrai uma aeronave da contagem degradada antes de dividir, para que um
único transponder defeituoso não pinte uma célula inteira de vermelho. Reproduzimos as
duas versões: `fracao_ruim` (crua) e `fracao_ruim_gpsjam` (com o -1), para poder comparar
nosso número com o mapa dele.

⚠ Os nomes de coluna ainda não foram confirmados contra um arquivo real (o ambiente não
tem acesso a gpsjam.org). `extrair_celulas` isola essa dependência: com o primeiro
arquivo em mãos, ajuste só ela.

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

# Nomes plausíveis, em ordem de preferência. Ajustar com um arquivo real.
COL_H3 = ("hex", "h3", "cell", "hex_id")
COL_BOAS = ("count_good", "good", "num_good", "good_count")
COL_RUINS = ("count_bad", "bad", "num_bad", "bad_count")
COL_LAT = ("lat", "latitude")
COL_LON = ("lon", "lng", "longitude")


def primeiro(d: dict, nomes):
    for n in nomes:
        if n in d and d[n] not in ("", None):
            return d[n]
    return None


def coordenadas(reg: dict):
    """Coordenadas da célula: direto se houver lat/lon, senão pelo índice H3."""
    lat, lon = primeiro(reg, COL_LAT), primeiro(reg, COL_LON)
    if lat is not None and lon is not None:
        return float(lat), float(lon)

    idx = primeiro(reg, COL_H3)
    if idx is None:
        return None

    import h3

    return h3.cell_to_latlng(str(idx))


def extrair_celulas(caminho: Path):
    """Normaliza um diário do GPSJAM em (lat, lon, boas, ruins)."""
    if caminho.suffix == ".csv":
        registros = list(csv.DictReader(caminho.open()))
    else:
        doc = json.loads(caminho.read_text())
        bruto = doc.get("features", doc) if isinstance(doc, dict) else doc
        registros = [r.get("properties", r) for r in bruto]

    for reg in registros:
        coord = coordenadas(reg)
        if coord is None:
            continue
        boas = primeiro(reg, COL_BOAS) or 0
        ruins = primeiro(reg, COL_RUINS) or 0
        yield coord[0], coord[1], int(float(boas)), int(float(ruins))


def dentro(caixa, lat, lon) -> bool:
    return caixa.lat_min <= lat <= caixa.lat_max and caixa.lon_min <= lon <= caixa.lon_max


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--origem", type=Path, default=ORIGEM)
    p.add_argument("--saida", type=Path, default=SAIDA)
    args = p.parse_args()

    arquivos = sorted(list(args.origem.glob("*.csv")) + list(args.origem.glob("*.json")))
    if not arquivos:
        print(f"nada em {args.origem} — rode gpsjam_fetch.py primeiro")
        return 1

    agregado = defaultdict(lambda: [0, 0])  # (dia, caixa) -> [boas, ruins]
    celulas = defaultdict(lambda: [0, 0])  # (caixa, lat, lon) -> [boas, ruins]  (G3)

    for arq in arquivos:
        dia = arq.stem
        for lat, lon, boas, ruins in extrair_celulas(arq):
            for nome, caixa in CAIXAS.items():
                if not dentro(caixa, lat, lon):
                    continue
                acc = agregado[(dia, nome)]
                acc[0] += boas
                acc[1] += ruins
                cel = celulas[(nome, round(lat, 3), round(lon, 3))]
                cel[0] += boas
                cel[1] += ruins

    args.saida.parent.mkdir(parents=True, exist_ok=True)
    with args.saida.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            ["data", "caixa", "aeronaves_boas", "aeronaves_ruins", "fracao_ruim", "fracao_ruim_gpsjam"]
        )
        for (dia, nome), (boas, ruins) in sorted(agregado.items()):
            total = boas + ruins
            crua = ruins / total if total else ""
            # o -1 é a de-noising do próprio GPSJAM; mantemos as duas para comparar
            gpsjam = max(ruins - 1, 0) / total if total else ""
            w.writerow([dia, nome, boas, ruins, crua, gpsjam])

    mapa = args.saida.parent / "gpsjam_celulas.csv"
    with mapa.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["caixa", "lat", "lon", "aeronaves_boas", "aeronaves_ruins", "fracao_ruim"])
        for (nome, lat, lon), (boas, ruins) in sorted(celulas.items()):
            total = boas + ruins
            w.writerow([nome, lat, lon, boas, ruins, ruins / total if total else ""])

    print(f"{len(agregado)} linhas → {args.saida}")
    print(f"{len(celulas)} células → {mapa}")
    print("\nConfira antes de plotar: se fracao_ruim vier vazia ou zero em toda parte,")
    print("o mapeamento de colunas no topo do arquivo está errado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
