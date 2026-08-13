#!/usr/bin/env python3
"""Baixa o histórico diário do GPSJAM.org.

O GPSJAM publica, por dia, um agregado por célula H3 com a fração de aeronaves que
reportaram baixa precisão de navegação naquela célula. É a forma mais barata de obter a
forma geral da série antes de gastar consulta no OpenSky.

⚠ VERIFICAR ANTES DE RODAR EM SÉRIE: o caminho exato dos arquivos diários. Abra
https://gpsjam.org, escolha uma data, e olhe a requisição no devtools. Ajuste URL_DIARIA.
O script foi escrito para falhar alto — se o caminho mudou, ele diz na primeira data em
vez de gravar 1.600 arquivos vazios.

Uso:
    python gpsjam_fetch.py --inicio 2022-02-01 --fim 2026-08-01
"""

import argparse
import json
import sys
import time
from datetime import date, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DESTINO = Path(__file__).resolve().parent.parent / "dados" / "bruto" / "gpsjam"

# ⚠ a confirmar — ver docstring.
URL_DIARIA = "https://gpsjam.org/data/{ano}-{mes:02d}-{dia:02d}-h3_4.json"

PAUSA_S = 1.0  # educação com um serviço gratuito de uma pessoa só
USER_AGENT = "pesquisa-jamming-artico/0.1 (jornalismo de dados; contato no repositorio)"


def datas(inicio: date, fim: date):
    d = inicio
    while d <= fim:
        yield d
        d += timedelta(days=1)


def baixar(d: date, destino: Path) -> str:
    """Retorna 'ok', 'cache' ou 'ausente'. Erros de rede sobem como exceção."""
    saida = destino / f"{d.isoformat()}.json"
    if saida.exists() and saida.stat().st_size > 0:
        return "cache"

    url = URL_DIARIA.format(ano=d.year, mes=d.month, dia=d.day)
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=60) as r:
            corpo = r.read()
    except HTTPError as e:
        if e.code == 404:
            return "ausente"  # dias sem cobertura existem; não é erro
        raise

    json.loads(corpo)  # valida antes de gravar: melhor falhar que guardar lixo
    saida.write_bytes(corpo)
    return "ok"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--inicio", default="2022-02-01")
    p.add_argument("--fim", default=date.today().isoformat())
    p.add_argument("--destino", type=Path, default=DESTINO)
    args = p.parse_args()

    args.destino.mkdir(parents=True, exist_ok=True)
    inicio = date.fromisoformat(args.inicio)
    fim = date.fromisoformat(args.fim)

    contagem = {"ok": 0, "cache": 0, "ausente": 0}
    primeira = True

    for d in datas(inicio, fim):
        try:
            estado = baixar(d, args.destino)
        except (URLError, json.JSONDecodeError) as e:
            print(f"FALHA em {d}: {e}", file=sys.stderr)
            if primeira:
                print(
                    "Falhou já na primeira data — provavelmente URL_DIARIA está errada.\n"
                    "Confira o caminho real no devtools de gpsjam.org antes de insistir.",
                    file=sys.stderr,
                )
                return 1
            raise

        contagem[estado] += 1
        primeira = False
        if estado == "ok":
            time.sleep(PAUSA_S)

    print(f"baixados={contagem['ok']} cache={contagem['cache']} ausentes={contagem['ausente']}")
    print(f"destino: {args.destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
