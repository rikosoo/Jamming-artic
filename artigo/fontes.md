# Registro de fontes

Três status: `✅ verificado` (confirmado em fonte identificável, com detalhe), `⚠ a verificar`
(afirmação em mão, fonte ainda não localizada), `❌ não sustentado`.

Nada com `⚠` vai para o texto publicado.

## Afirmações centrais

| # | Afirmação | Status | O que apurei |
|---|---|---|---|
| A1 | Jamming observado pela primeira vez no norte da Noruega em 2017 | ✅ | Mais preciso do que a formulação original: **7 a 20 de setembro de 2017**, pilotos da Widerøe reportaram perda de sinal GPS em espaço aéreo indo do extremo norte até cidades a ~600 km na costa oeste. Coincidiu com o **Zapad-2017**, com atividade na base de **Pechenga**, óblast de Múrmansk. Fontes: CSIS Aerospace Security (base "Arctic Circle GPS Jamming"), Barents Observer. |
| A2 | Aumento drástico desde a invasão de 2022 | ✅ | Confirmado, com nuance de data: o jamming **contínuo** começa no **outono de 2022**, depois do início dos ataques ucranianos de drones a alvos dentro da Rússia — não em fevereiro. A distinção importa: fev/2022 é a invasão, out/2022 é a mudança de comportamento eletromagnético. |
| A3 | Detectado quase diariamente, sobretudo em voos para Kirkenes, Vadsø e Vardø | ✅ | Confirmado. Aeroportos da área de Varanger: Vadsø, Vardø, Båtsfjord e Berlevåg, além de Kirkenes. Barents Observer ("praticamente todo dia"). |
| A4 | Widerøe Dash-8 abortou pouso em Vardø, set/2025 | ✅ | Detalhado: voo regional **vindo de Vadsø**, abortou o pouso em Vardø **ao meio-dia de uma sexta-feira**, e desviou para **Båtsfjord**. Causa: jamming **combinado com teto baixo de nuvens** — as duas coisas juntas é que inviabilizaram o pouso. Ocorreu durante o **Zapad-2025**. newsinenglish.no, 16/09/2025. ⚠ falta a data exata do voo e o número do voo. |
| A5 | Nkom registrou jamming forte sobre Varanger a 500 m | ✅ | Fonte nomeada: **Espen Slette, da Nkom**. Medições mais recentes indicam interferência a ~600 m. ⚠ conferir qual medição é de quando — 500 e 600 m circulam nas duas reportagens. |
| A6 | Nkom instalará 2 estações de monitoramento adicionais em 2026 | ✅ | Confirmado, e o contexto é melhor que a afirmação: **já existem três** estações dedicadas na região de fronteira. As duas novas cobrem lacunas — boa parte da **Península de Varanger** e trechos do **mar de Barents**. Motivo declarado: a interferência está sendo detectada cada vez mais fundo no espaço aéreo norueguês. GPS World, Telecompaper, Barents Observer. |
| A7 | Finlândia: ~1.200 notificações vs. 239 no ano anterior | ✅ | Preciso: **~1.200 notificações de interferência de GPS na aviação em 2024, contra 239 no ano anterior**, dentro da Finlândia. Some-se **~2.100 notificações de fora da Finlândia em 2024**. Fonte: Traficom (há estatística publicada em tieto.traficom.fi). |
| A8 | Metodologia publicada usa NACp de ADS-B para medir jamming | ✅ | **Felux, M., Fol, P., Figuet, B., Waltert, M., & Olive, X. (2024). "Impacts of global navigation satellite system jamming on aviation." *NAVIGATION*, 71(3). DOI 10.33012/navi.657.** NACp e NIC do OpenSky. Janela fev–dez/2022; regiões bálticas, mar Negro, Mediterrâneo oriental — **não** o Ártico. ⚠ ler o PDF para os limiares numéricos. |
| A9 | FAA considera NACp < 8 fora de conformidade | ✅ | Corrobora nosso limiar. ⚠ citar a fonte regulatória primária (AC 20-165 / DO-260B). |
| A10 | GPSJAM: faixas 2% e 10%, de-noising de −1, fonte ADS-B Exchange, CC-BY | ✅ | John Wiseman / gpsjam.org. Crédito obrigatório a ele e ao ADS-B Exchange. |
| **A11** | **O jamming não tem a Noruega como alvo — é transbordamento** | ✅ | **Nicolai Gerrard, da Nkom:** o que se vê sobre o leste do Finnmark é provável efeito de transbordamento da autodefesa eletromagnética russa de suas próprias instalações militares — o mesmo padrão visto em locais dentro da Rússia e no Báltico. Feito com alta potência e antenas irradiantes, **sem consideração** por vazar para países vizinhos. Kirkenes fica a ~55 km do vale de Pechenga, onde estão a 200ª Brigada de Fuzileiros Motorizados e a 61ª Brigada de Infantaria Naval. **Ver nota editorial abaixo — isto muda o enquadramento da matéria.** |
| A12 | Trident Juncture (2018) associado a episódio de jamming | ✅ | A base do CSIS destaca três exercícios com perda de sinal registrada, incluindo Zapad-2017 e o Trident Juncture da OTAN. Preenche a lacuna que estava aberta na cronologia. |

## Nota editorial: o enquadramento mudou

A apuração derrubou a leitura intuitiva de "a Rússia está atacando a aviação norueguesa".
A explicação da própria autoridade norueguesa (A11) é outra: a Noruega está **dentro do
raio de vazamento** da proteção eletrônica das bases da península de Kola. Ninguém está
mirando a rampa de aproximação de Vardø.

Isso não enfraquece a matéria — fortalece, e em três frentes:

1. **É mais defensável.** Não exige provar intenção, que é o ponto onde reportagens sobre
   guerra eletrônica costumam se esticar além da fonte.
2. **Torna o problema mais permanente, não menos.** Jamming como ataque pode ser negociado
   ou cessado. Jamming como efeito colateral de força-protection continua enquanto a
   ameaça de drones a Kola continuar — isto é, indefinidamente. Isso é exatamente a tese
   de "condição ambiental permanente", agora com mecanismo causal em vez de suposição.
3. **Afia o argumento da altitude.** Se ninguém está mirando a aproximação de Vardø, então
   ninguém vai calibrá-la para poupá-la. A degradação em 500 m não é escolha de alguém —
   é a borda de um cobertor eletromagnético grande demais. Não há a quem apelar.

**Consequência prática:** revisar as seções 4 e 7 do esqueleto para essa lógica. E manter
a regra de atribuição abaixo: mesmo com a Nkom nomeando a Rússia, o texto atribui citando
quem atribui.

## Fontes de dados

| Fonte | O que dá | Custo | Acesso |
|---|---|---|---|
| GPSJAM.org | Agregado diário por célula H3, desde 2022, CC-BY | grátis | HTTP |
| OpenSky Network | ADS-B cru com NACp/NIC (`operational_status_data4`), via Trino | grátis (conta) | conta |
| ADSB Exchange | ADS-B cru — origem do GPSJAM | grátis/tier | API |
| **CSIS Aerospace Security** | Base "Arctic Circle GPS Jamming": eventos de perda de sinal desde fins de 2017, montada a partir de reportagens regionais e autoridades. Metodologia **por evento**, não telemétrica — complementa a nossa, não compete | grátis | web |
| Traficom (FI) | Estatística publicada de interferência (tieto.traficom.fi) | grátis | portal |
| Nkom (NO) | Monitoramento de espectro; 3 estações + 2 em 2026 | grátis | site / pedido |
| Jammertest (Andøya) | Exercício aberto de jamming/spoofing, dados abertos | grátis | site |

## Veículos que já cobriram (para não repetir, e para achar as fontes humanas)

Barents Observer (a cobertura mais consistente e mais próxima), High North News, ArcticToday,
newsinenglish.no, GPS World, Telecompaper, Yle (lado finlandês).

**Pauta lateral aberta:** Barents Observer registrou interferência em espaço aéreo de
**Svalbard**. Se confirmado e recorrente, é um segundo teatro, muito mais longe de Kola —
e portanto muito mais difícil de explicar como transbordamento. Vale checar.

## Instituições para contato

- **Nkom** — Espen Slette (mediu os 500 m) e Nicolai Gerrard (a análise de transbordamento).
  São as duas fontes nomeadas mais importantes da matéria.
- **Avinor** — quais aproximações em Vardø/Vadsø/Kirkenes são GNSS-dependentes.
- **Widerøe** — o voo de Vardø; procedimento e treinamento sob jamming.
- **Traficom** — o número de 2024 e a metodologia de contagem.
- **Havarikommisjonen / NSIA** — houve relatório sobre Vardø?
- **FFI** — contexto técnico e histórico pré-2022.
- **Jammertest / Andøya** — dados e possível ida a campo em setembro.

## Nota sobre o ambiente de apuração

A verificação foi feita por busca web. O ambiente tem bloqueio de egress para as páginas
primárias (`gpsjam.org`, `opensky-network.org`, `navi.ion.org`, `traficom.fi`,
`thebarentsobserver.com` etc.) — nenhuma pôde ser aberta diretamente. As afirmações ✅
estão confirmadas em fonte identificada e com detalhe consistente entre veículos
independentes, **mas abrir o primário segue obrigatório antes de publicar**. Prioridade:
o PDF de Felux et al., a estatística da Traficom e as reportagens do Barents Observer que
carregam as citações nominais de Slette e Gerrard.

## Regra de atribuição

A matéria descreve fenômeno, geografia e efeito. Atribuição de origem aparece **como
citação de quem a faz** — e agora temos citação nominal da autoridade norueguesa, o que é
o melhor cenário possível. Inferência geográfica própria (o gradiente leste→oeste no G3) é
apresentada como o que é: inferência, do repórter.
