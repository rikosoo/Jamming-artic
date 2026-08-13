# Jamming no Ártico

Projeto de reportagem + análise de dados sobre interferência de GNSS (GPS) no Alto Norte
europeu — Finnmark (NO), Lapônia (FI) e mar de Barents.

**Tese:** o jamming deixou de ser incidente pontual e virou condição ambiental permanente.
E a curva está descendo em altitude — jamming forte a 500 m atinge a fase de aproximação,
onde a margem de segurança é menor. Isso muda a natureza do risco, não só a frequência.

## Estrutura

```
artigo/
  00-esqueleto.md     Estrutura da matéria, seção a seção, com o que cada uma precisa provar
  01-cronologia.md    Linha do tempo 2017 → 2026 (fatos + fonte de cada um)
  fontes.md           Registro de fontes: o que está verificado, o que falta checar
  entrevistas.md      Pauta de campo: quem procurar, o que perguntar
analise/
  README.md           Metodologia NACp — o que medimos e por quê
  gpsjam_fetch.py     Baixa o histórico diário do GPSJAM.org
  gpsjam_series.py    Monta série temporal por célula geográfica
  nacp_opensky.py     Extrai NACp do ADS-B cru (OpenSky) na caixa do Ártico
dados/
  bruto/              Downloads intactos (não versionado)
  processado/         Séries e agregados (versionado quando pequeno)
graficos/             Saídas finais para a matéria
```

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

OpenSky exige conta gratuita para acesso histórico (Trino/Impala). Coloque as
credenciais em `.env` (ver `.env.example`) — o arquivo não é versionado.

## Estado

Esqueleto montado. Próximo passo: verificação de fontes (`artigo/fontes.md`) e
primeira coleta GPSJAM.
