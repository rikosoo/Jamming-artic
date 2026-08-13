# Registro de fontes

Três status: `✅ verificado` (link primário aberto e conferido), `⚠ a verificar`
(afirmação em mão, fonte primária ainda não localizada), `❌ não sustentado`.

Nada com `⚠` vai para o texto publicado.

## Afirmações centrais

| # | Afirmação | Status | Fonte primária necessária |
|---|---|---|---|
| A1 | Jamming observado pela primeira vez no norte da Noruega em 2017 | ⚠ | Relatório Nkom ou Forsvarets forskningsinstitutt (FFI) |
| A2 | Aumento drástico desde fev/2022 | ⚠ | Série da Nkom, ou GPSJAM (nossa própria) |
| A3 | Detectado quase diariamente, sobretudo em voos para Kirkenes, Vadsø e Vardø | ⚠ | Nkom / Avinor / entrevista com piloto |
| A4 | Widerøe Dash-8 abortou pouso em Vardø, set/2025 | ⚠ | Widerøe, Avinor, ou autoridade norueguesa de investigação (NSIA/Havarikommisjonen) |
| A5 | Nkom registrou jamming forte sobre Varanger a 500 m | ⚠ | Publicação/medição da Nkom |
| A6 | Nkom instalará 2 estações de monitoramento adicionais em 2026 | ⚠ | Nkom (orçamento ou comunicado) |
| A7 | Finlândia: ~1.200 notificações vs. 239 no ano anterior | ⚠ | Traficom |
| A8 | Metodologia publicada usa NACp de ADS-B para medir jamming | ⚠ | Achar o paper e citar formalmente — é a base metodológica da seção 3 |

## Fontes de dados

| Fonte | O que dá | Custo | Acesso |
|---|---|---|---|
| GPSJAM.org | Mapas diários agregados por célula H3, desde 2022 | grátis | HTTP direto |
| OpenSky Network | ADS-B cru, inclui NACp; histórico via Trino | grátis (conta) | conta acadêmica/pessoal |
| ADSB Exchange | ADS-B cru, sem filtro | grátis/tier | API |
| Jammertest (Andøya) | Dados de exercício real, política aberta | grátis | site do evento |
| Traficom (FI) | Notificações de interferência | grátis | portal / pedido |
| Nkom (NO) | Monitoramento de espectro | grátis | site / pedido de acesso |

## Instituições para contato (direito de resposta e apuração)

- **Nkom** — autoridade de comunicações norueguesa. Dona da medição dos 500 m e das
  estações de 2026. Fonte principal.
- **Avinor** — operador aeroportuário. Quais aproximações são GNSS-dependentes.
- **Widerøe** — operador do voo de Vardø. Procedimento sob jamming, treinamento.
- **Traficom** — autoridade finlandesa. Origem do número 1.200 vs 239.
- **Havarikommisjonen / NSIA** — se houve relatório de incidente sobre Vardø.
- **FFI** — pesquisa de defesa norueguesa. Contexto técnico e histórico pré-2022.
- **Jammertest / Andøya** — acesso a dados e possível pauta de campo em setembro.

## Nota sobre atribuição

Nenhuma fonte aberta atribui operação específica de jamming a uma unidade específica com
grau de certeza publicável. A matéria descreve fenômeno, geografia e efeito. Atribuição
só aparece como citação de quem a fez, nunca como voz do texto.
