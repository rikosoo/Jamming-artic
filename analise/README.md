# Metodologia

## A ideia em uma frase

Aeronaves comerciais transmitem, junto com sua posição, uma declaração de quanta confiança
têm nela. Quando o GNSS é degradado, essa declaração cai. Milhares de aeronaves viram,
sem intenção, uma rede de sensores de interferência.

## Precedente: o que já foi feito, e o que não foi

**Felux, M., Fol, P., Figuet, B., Waltert, M., & Olive, X. (2024). "Impacts of global
navigation satellite system jamming on aviation." *NAVIGATION: Journal of the Institute of
Navigation*, 71(3). DOI 10.33012/navi.657** — este é o trabalho de referência. Usa NACp e
NIC de ADS-B, do OpenSky Network, para detectar e localizar interferência.

Duas coisas importam para nós:

1. **O método está publicado e revisado.** Não estamos inventando uma medida; estamos
   aplicando uma existente. Isso é o que sustenta a seção 3 da matéria contra a objeção
   de "jornalista brincando de cientista".
2. **A janela deles é fev–dez/2022, e as regiões são os países bálticos, o leste europeu
   junto ao mar Negro e o Mediterrâneo oriental.** O Ártico europeu não está lá, e nem os
   quatro anos seguintes. É exatamente aí que está o ineditismo desta reportagem.

⚠ **Pendente:** ler o PDF completo e conferir os limiares numéricos exatos que eles usam.
Se divergirem dos nossos, adotamos os deles e documentamos. O limiar não muda depois de
ver o resultado.

## Os campos

**NACp** — *Navigation Accuracy Category — position* — inteiro 0–11 na mensagem de
*operational status* (DO-260B, bits 77–80, emitida a cada ~2,5 s). Codifica o raio de
incerteza horizontal (EPU) que a aeronave está reportando:

| NACp | EPU |
|---|---|
| 11 | < 3 m |
| 10 | < 10 m |
| 9 | < 30 m |
| 8 | < 92,6 m (0,05 NM) |
| 7 | < 185,2 m (0,1 NM) |
| 6 | < 555,6 m (0,3 NM) |
| 5 | < 926 m (0,5 NM) |
| 1–4 | degradação crescente |
| 0 | desconhecido / ≥ 18,52 km |

**NIC** — *Navigation Integrity Category* — indicador irmão, de integridade em vez de
acurácia. É o que o GPSJAM usa. Coletamos os dois.

**Limiar adotado: NACp ≤ 7.** Não é escolha nossa: a FAA considera NACp abaixo de 8 fora
de conformidade para operação padrão. O corte é regulatório, e é a fronteira entre "GNSS
funcionando" e "esta aeronave já não pode voar aproximação RNP com esse dado". Conveniente
para a matéria: o limiar é exatamente o ponto onde a autoridade diz que o voo normal deixa
de ser possível.

## As duas fontes, e por que ambas

**GPSJAM.org** (John Wiseman) — agregado diário por célula H3, desde fev/2022, sob CC-BY,
derivado de ADS-B Exchange. Ele classifica cada célula pela fração de aeronaves com
navegação degradada em 24 h: **verde < 2%, amarelo 2–10%, vermelho > 10%**. O cálculo
subtrai uma aeronave da contagem degradada antes de dividir — de-noising deliberado, para
que um único transponder defeituoso não pinte uma célula inteira de vermelho.

> Crédito obrigatório na publicação: GPSJAM.org / John Wiseman (CC-BY), e ADS-B Exchange
> como origem do ADS-B cru.

Reproduzimos as duas frações (crua e com o −1) para poder cotejar nosso número com o mapa
dele. Divergência sistemática entre as duas é sinal de que a área tem poucas aeronaves por
célula — o que é bem provável no Ártico e precisa ser dito no texto.

**OpenSky Network** — ADS-B cru, tabela `operational_status_data4` (DO-260B) via Trino.
É daqui que sai a análise própria: permite cortar por altitude, que o agregado do GPSJAM
não permite. **Sem OpenSky não há G2, e sem G2 não há tese.**

## Área de estudo

Caixa principal — Finnmark e Península de Varanger:

```
lat  68,5 → 71,5 N      lon  22,0 → 32,0 E
```

Caixa de controle — mesma faixa de latitude, longe da fronteira russa (Lofoten/Vesterålen):

```
lat  67,5 → 69,5 N      lon  12,0 → 17,0 E
```

**Por que o controle importa:** NACp também cai por motivos banais — equipamento antigo,
aeronave específica, geometria de constelação em latitude alta. A caixa de controle absorve
tudo isso. O resultado publicável é a **diferença** entre as caixas, nunca o valor absoluto
de uma delas. Sem controle, o gráfico mede a idade da frota da Widerøe.

## Confundidores a tratar explicitamente

1. **Cobertura de receptores.** A rede ADS-B cresceu muito desde 2022. Mais receptores =
   mais aeronaves vistas, sobretudo em baixa altitude, que é onde a cobertura era pior.
   Isso pode **criar sozinho** a tendência de descida em altitude — que é justamente a
   nossa tese. *Este é o confundidor mais perigoso da matéria.* Mitigação: sempre a fração
   degradada dentro da mesma faixa de altitude e da mesma célula, nunca contagem bruta.
   E reportar, junto ao G2, o total de aeronaves observadas por faixa — se o denominador
   explodiu, o leitor tem de ver.
2. **Composição da frota.** Mudança na mistura de aeronaves altera o NACp médio sem
   jamming nenhum. Mitigação: agregar por aeronave-dia único e checar a estabilidade do
   conjunto de ICAO24 observados ao longo da série.
3. **Latitude alta.** Geometria de constelação é pior no Ártico. Por isso o controle está
   na mesma faixa de latitude.
4. **Aeronave em solo.** Também reporta. Filtrar `onground` e altitude mínima (150 m),
   senão a faixa 0–1000 m vira estacionamento de aeroporto.

## Saídas

- **G1** série mensal: fração de aeronaves-dia com NACp degradado — caixa principal *vs*
  controle, nas mesmas eixadas
- **G2** perfil de altitude: fração degradada por faixa (0–1000, 1000–3000, 3000–6000,
  6000–10000, >10000 m), comparando 2022–23 com 2025–26. *O gráfico da tese.*
- **G3** mapa de calor por célula H3, média do último ano

## Ordem de execução

```bash
python gpsjam_fetch.py --descobrir 2024-03-15     # confirmar o caminho dos arquivos
python gpsjam_fetch.py --inicio 2022-02-01 --fim 2026-08-01
python gpsjam_series.py

python nacp_opensky.py --amostra                  # conferir o schema num único dia
python nacp_opensky.py --caixa finnmark --inicio 2022-02-01 --fim 2026-08-01
python nacp_opensky.py --caixa controle --inicio 2022-02-01 --fim 2026-08-01
```

GPSJAM primeiro porque é barato e já dá a forma geral. Ele valida se vale gastar horas de
fila no OpenSky — e diz onde olhar.

## Estado atual: o que trava

O ambiente de desenvolvimento não tem acesso de rede a `gpsjam.org`, `opensky-network.org`
nem aos periódicos (bloqueio de egress). Isso deixa dois pontos por confirmar, ambos
marcados com ⚠ no código, ambos resolvíveis em minutos numa máquina com rede aberta:

1. O caminho exato dos arquivos diários do GPSJAM → `gpsjam_fetch.py --descobrir`
2. Os nomes exatos das colunas no Trino do OpenSky → `nacp_opensky.py --amostra`

Nenhum dos dois muda o desenho da análise. São plugues, não fundações.
