"""Parâmetros compartilhados da análise.

Tudo que define o recorte do estudo mora aqui. Mudou aqui, mudou em todos os scripts —
e o diff no git registra que a decisão foi tomada antes de rodar, não depois de ver o
resultado.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Caixa:
    nome: str
    lat_min: float
    lat_max: float
    lon_min: float
    lon_max: float


# Área principal: Finnmark / Península de Varanger (Kirkenes, Vadsø, Vardø)
FINNMARK = Caixa("finnmark", 68.5, 71.5, 22.0, 32.0)

# Controle: mesma faixa de latitude, longe da fronteira russa
CONTROLE = Caixa("controle", 67.5, 69.5, 12.0, 17.0)

CAIXAS = {c.nome: c for c in (FINNMARK, CONTROLE)}

# Limiar de degradação. Ver analise/README.md — verificar contra o paper A8.
NACP_DEGRADADO = 7

# Faixas de altitude em metros, para o gráfico G2 (o da tese).
FAIXAS_ALTITUDE = [(0, 1000), (1000, 3000), (3000, 6000), (6000, 10000), (10000, 15000)]

# Altitude mínima considerada: abaixo disso é solo/taxi e polui a faixa baixa.
ALTITUDE_MINIMA_M = 150

# Janelas de comparação do G2.
PERIODO_INICIAL = ("2022-02-01", "2023-12-31")
PERIODO_RECENTE = ("2025-01-01", "2026-08-01")

# Resolução H3 usada pelo GPSJAM.
H3_RESOLUCAO = 4
