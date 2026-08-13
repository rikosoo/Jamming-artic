#!/usr/bin/env python3
"""Baixa o histórico diário do GPSJAM.org.

O GPSJAM publica, por dia, um agregado por célula H3 (resolução 4) com a contagem de
aeronaves que reportaram boa e má qualidade de navegação naquela célula. A série começa
em fevereiro de 2022 e o conjunto é distribuído sob CC-BY — exige crédito a John Wiseman
/ gpsjam.org e, em cascata, ao ADS-B Exchange, que é a origem do ADS-B cru.

⚠ O CAMINHO EXATO DOS ARQUIVOS AINDA NÃO FOI CONFIRMADO. O ambiente onde este script foi
escrito não tem acesso de rede a gpsjam.org (bloqueio de egress), então os padrões abaixo
são candidatos, não fato. Rode primeiro:

    python gpsjam_fetch.py --descobrir 2024-03-15

Ele testa cada candidato para uma data e diz qual responde 200. Fixe o vencedor em
URL_DIARIA e só então rode a série inteira. São ~1.600 dias; descobrir o caminho errado
depois de baixar tudo custa caro.

Uso:
    python gpsjam_fetch.py --descobrir 2024-03-15
    python gpsjam_fetch.py --inicio 2022-02-01 --fim 2026-08-01
"""

import argparse
import csv
import io
import sys
import time
from datetime import date, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

DESTINO = Path(__file__).resolve().parent.parent / "dados" / "bruto" / "gpsjam"

# Candidatos observados/plausíveis. O primeiro que responder 200 em --descobrir vence.
CANDIDATOS = [
    "https://gpsjam.org/data/{d}-h3_4.csv",
    "https://gpsjam.org/data/{d}/h3_4.csv",
    "https://gpsjam.org/data/{d}-h3_4.json",
    "https://gpsjam.org/data/{d}/h3_4.json",
]

URL_DIARIA = CANDIDATOS[0]

PAUSA_S = 1.0  # educação com um serviço gratuito mantido por uma pessoa
USER_AGENT = "pesquisa-jamming-artico/0.1 (jornalismo de dados; contato no repositorio)"


def datas(inicio: date, fim: date):
    d = inicio
    while d <= fim:
        yield d
        d += timedelta(days=1)


def buscar(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=60) as r:
        return r.read()


def descobrir(d: date) -> int:
    """Testa os candidatos numa data e imprime o que funciona."""
    alvo = d.isoformat()
    achou = False
    for padrao in CANDIDATOS:
        url = padrao.format(d=alvo)
        try:
            corpo = buscar(url)
        except HTTPError as e:
            print(f"  {e.code}  {url}")
            continue
        except URLError as e:
            print(f"  ERRO {e.reason}  {url}")
            continue

        achou = True
        print(f"  200  {url}   ({len(corpo)} bytes)")
        print("  --- primeiras linhas ---")
        for linha in corpo.decode("utf-8", "replace").splitlines()[:5]:
            print(f"  {linha}")
        print("  ---")

    if not achou:
        print(
            "\nNenhum candidato respondeu. Abra https://gpsjam.org, escolha uma data e"
            "\nolhe a aba Network do devtools: o arquivo diário aparece ali. Acrescente"
            "\no padrão real a CANDIDATOS.",
            file=sys.stderr,
        )
        return 1

    print("\nFixe o padrão que funcionou em URL_DIARIA e rode sem --descobrir.")
    return 0


def validar(corpo: bytes, url: str) -> None:
    """Recusa gravar lixo. Uma página de erro HTML de 200 é o modo comum de falhar."""
    texto = corpo.decode("utf-8", "replace").lstrip()
    if texto.startswith("<"):
        raise ValueError(f"resposta parece HTML, não dados: {url}")
    if url.endswith(".csv"):
        linhas = list(csv.reader(io.StringIO(texto)))
        if len(linhas) < 2:
            raise ValueError(f"CSV com menos de 2 linhas: {url}")


def baixar(d: date, destino: Path) -> str:
    """Retorna 'ok', 'cache' ou 'ausente'."""
    sufixo = ".csv" if URL_DIARIA.endswith(".csv") else ".json"
    saida = destino / f"{d.isoformat()}{sufixo}"
    if saida.exists() and saida.stat().st_size > 0:
        return "cache"

    url = URL_DIARIA.format(d=d.isoformat())
    try:
        corpo = buscar(url)
    except HTTPError as e:
        if e.code == 404:
            return "ausente"  # dias sem cobertura existem; não é erro
        raise

    validar(corpo, url)
    saida.write_bytes(corpo)
    return "ok"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--descobrir", metavar="AAAA-MM-DD", help="testa os padrões de URL numa data")
    p.add_argument("--inicio", default="2022-02-01")
    p.add_argument("--fim", default=date.today().isoformat())
    p.add_argument("--destino", type=Path, default=DESTINO)
    args = p.parse_args()

    if args.descobrir:
        print(f"testando candidatos para {args.descobrir}:")
        return descobrir(date.fromisoformat(args.descobrir))

    args.destino.mkdir(parents=True, exist_ok=True)
    inicio = date.fromisoformat(args.inicio)
    fim = date.fromisoformat(args.fim)

    contagem = {"ok": 0, "cache": 0, "ausente": 0}
    primeira = True

    for d in datas(inicio, fim):
        try:
            estado = baixar(d, args.destino)
        except (URLError, ValueError) as e:
            print(f"FALHA em {d}: {e}", file=sys.stderr)
            if primeira:
                print("Falhou na primeira data. Rode --descobrir antes de insistir.", file=sys.stderr)
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
