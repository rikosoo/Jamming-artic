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
| A8 | Metodologia publicada usa NACp de ADS-B para medir jamming | ✅ | **Felux, M., Fol, P., Figuet, B., Waltert, M., & Olive, X. (2024). "Impacts of global navigation satellite system jamming on aviation." *NAVIGATION*, 71(3). DOI 10.33012/navi.657.** Usa NACp e NIC do OpenSky Network. Janela: fev–dez/2022. Regiões: bálticos, leste europeu junto ao mar Negro, Mediterrâneo oriental — **não** o Ártico. Pendência menor: ler o PDF e conferir os limiares numéricos exatos. |
| A9 | FAA considera NACp < 8 fora de conformidade para operação padrão | ✅ | Corrobora nosso limiar. Citar a fonte regulatória primária (AC 20-165 / DO-260B) antes de publicar. |
| A10 | GPSJAM: verde <2%, amarelo 2–10%, vermelho >10% de aeronaves degradadas em 24h; subtrai 1 do numerador como de-noising; fonte ADS-B Exchange; CC-BY | ✅ | John Wiseman / gpsjam.org. Crédito obrigatório na publicação, a ele e ao ADS-B Exchange. |

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

## Nota sobre o ambiente

A verificação acima foi feita a partir de busca web. O ambiente de desenvolvimento tem
bloqueio de egress para `gpsjam.org`, `opensky-network.org`, `navi.ion.org`, `mdpi.com`,
`insidegnss.com` e afins — nenhuma dessas páginas pôde ser aberta diretamente. As
afirmações marcadas ✅ estão confirmadas em fonte secundária confiável e com citação
completa; **abrir o primário continua sendo passo obrigatório antes de publicar**, em
especial o PDF de Felux et al., para os limiares numéricos.

## Nota sobre atribuição

Nenhuma fonte aberta atribui operação específica de jamming a uma unidade específica com
grau de certeza publicável. A matéria descreve fenômeno, geografia e efeito. Atribuição
só aparece como citação de quem a fez, nunca como voz do texto.
