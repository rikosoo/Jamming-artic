# Jamming no Ártico

Projeto de reportagem + análise de dados sobre interferência de GNSS (GPS) no Alto Norte
europeu — Finnmark (NO), Lapônia (FI) e mar de Barents.

**Tese:** o jamming deixou de ser incidente pontual e virou condição ambiental permanente.
E a curva está descendo em altitude — jamming forte a 500 m atinge a fase de aproximação,
onde a margem de segurança é menor. Isso muda a natureza do risco, não só a frequência.

**O que a apuração acrescentou à tese:** a Nkom não descreve o jamming como ataque à
Noruega, e sim como transbordamento da autodefesa eletromagnética das bases russas em Kola.
Isso torna a permanência um mecanismo, não uma metáfora — um ataque pode cessar, um
transbordamento não tem interlocutor. Ver a nota editorial em `artigo/fontes.md`.

## Estrutura

```
artigo/
  00-esqueleto.md          Estrutura em 8 seções, com o que cada uma precisa provar
  fontes.md                Registro de verificação: 12 afirmações, status e proveniência
  cronologia-fatos.md      Linha do tempo 2017 → 2026, uma fonte por linha
  entrevistas.md           Pauta de campo por prioridade, com perguntas dirigidas
  secao-0-abertura.md      Rascunho — a cena de Vardø
  secao-1-cronologia.md    Rascunho — de anomalia a clima, e a armadilha Zapad
  secao-2-numeros.md       Rascunho — por que a estatística oficial não basta
  secao-4-altitude.md      Rascunho — o argumento da altitude, coração da tese
analise/
  README.md           Metodologia NACp/NIC, limiares, caixa de controle, confundidores
  config.py           Recorte geográfico e parâmetros, fixados antes de rodar
  gpsjam_fetch.py     Coleta dos diários do GPSJAM.org (tem modo --descobrir)
  gpsjam_series.py    Série temporal e agregado por célula
  nacp_opensky.py     Extração de NACp/NIC do ADS-B cru via Trino (tem modo --amostra)
dados/
  bruto/              Downloads intactos (não versionado)
  processado/         Séries e agregados
graficos/             Saídas finais para a matéria
sideprojects/         Beat de segurança espacial: as outras quatro pautas da mesma família
```

`sideprojects/` reúne as pautas adjacentes — hijacking de ativos espaciais, spoofing,
comunicação satélite-a-satélite e defesa de estações terrenas. São mapas de partida, não
apuração feita. O jamming é a camada mais visível de um problema que vai da antena da
estação terrena ao enlace entre dois satélites.

Cada rascunho de seção traz, no próprio arquivo, a fonte de cada trecho, as decisões de
redação (para serem contestadas) e as pendências de apuração. Nada é escrito por
antecipação de um dado que ainda não existe.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

OpenSky exige conta gratuita para acesso histórico (Trino). Credenciais em `.env`
(ver `.env.example`) — não versionado.

## Coleta

```bash
python analise/gpsjam_fetch.py --descobrir 2024-03-15   # confirma o caminho dos arquivos
python analise/gpsjam_fetch.py --inicio 2022-02-01 --fim 2026-08-01
python analise/gpsjam_series.py

python analise/nacp_opensky.py --amostra                # confere o schema num único dia
python analise/nacp_opensky.py --caixa finnmark --inicio 2022-02-01 --fim 2026-08-01
python analise/nacp_opensky.py --caixa controle --inicio 2022-02-01 --fim 2026-08-01
```

A caixa de controle não é opcional. O resultado publicável é a diferença entre as duas
caixas — o valor absoluto de uma delas mede a idade da frota, não o jamming.

## Estado

| Frente | Onde está |
|---|---|
| Estrutura da matéria | ✅ 8 seções definidas |
| Verificação de fontes | ✅ 12 de 12 afirmações confirmadas em fonte identificada — **todas em fonte secundária**; abrir os primários segue obrigatório |
| Abertura (seção 0) | ✅ rascunho 1 |
| Cronologia (seção 1) | ✅ rascunho 1 |
| Números (seção 2) | ✅ rascunho 1 |
| Análise NACp (seção 3) | ⛔ depende da coleta |
| Altitude (seção 4) | ✅ rascunho 1 |
| Setores (seção 5) | ⛔ depende de entrevistas |
| Mitigação (seção 6) | 🔨 estrutura pronta, falta apurar status do eLoran na Noruega |
| Fecho (seção 7) | 🔨 lógica definida no esqueleto |
| Coleta de dados | ⛔ bloqueada neste ambiente (egress) |
| Entrevistas | ⛔ não iniciadas |

**O que trava a coleta:** este ambiente tem bloqueio de egress para `gpsjam.org`,
`opensky-network.org` e para os periódicos. Restam dois pontos por confirmar, ambos
marcados com ⚠ no código e resolvíveis em minutos numa máquina com rede aberta: o caminho
dos arquivos diários do GPSJAM (`--descobrir`) e os nomes de coluna no Trino (`--amostra`).
Nenhum dos dois muda o desenho da análise.

## Crédito obrigatório na publicação

O conjunto do GPSJAM é CC-BY: creditar **John Wiseman / gpsjam.org** e o **ADS-B Exchange**
como origem do ADS-B cru. A metodologia de detecção por NACp/NIC segue **Felux, Fol,
Figuet, Waltert & Olive (2024)**, *NAVIGATION* 71(3), DOI 10.33012/navi.657 — citar.
