# Metodologia

## A ideia em uma frase

Aeronaves comerciais transmitem, junto com sua posição, uma declaração de quanta confiança
têm nela. Quando o GNSS é degradado, essa declaração cai. Milhares de aeronaves viram,
sem intenção, uma rede de sensores de interferência.

## O campo: NACp

**NACp** — *Navigation Accuracy Category — position* — é um inteiro de 0 a 11 transmitido
na mensagem de *operational status* do ADS-B (DO-260B). Ele codifica o raio de contenção
horizontal (EPU/HFOM) que o sistema de navegação da aeronave está reportando:

| NACp | EPU |
|---|---|
| 11 | < 3 m |
| 10 | < 10 m |
| 9 | < 30 m |
| 8 | < 92.6 m (0.05 NM) |
| 7 | < 185.2 m (0.1 NM) |
| 6 | < 555.6 m (0.3 NM) |
| 5 | < 926 m (0.5 NM) |
| 1–4 | degradação crescente |
| 0 | desconhecido / ≥ 18.52 km |

**Operação em voo normal:** NACp ≥ 8 (tipicamente 9–10, GNSS saudável).
**Critério de degradação adotado:** `NACp ≤ 7`. É o limiar usado na literatura porque
separa "GNSS funcionando" de "a aeronave já não pode voar aproximação RNP com esse dado".

> ⚠ Verificar contra o paper de referência (`artigo/fontes.md` A8) antes de publicar. Se o
> paper usar outro limiar, adotamos o dele e documentamos a diferença. O limiar não é
> escolhido depois de ver o resultado.

## Área de estudo

Caixa principal — Finnmark e Península de Varanger:

```
lat  68.5 → 71.5 N
lon  22.0 → 32.0 E
```

Caixa de controle — mesma latitude, longe da fronteira russa (Lofoten/Vesterålen):

```
lat  67.5 → 69.5 N
lon  12.0 → 17.0 E
```

**Por que o controle importa:** NACp também cai por motivos banais — equipamento antigo,
aeronave específica, receptor ruim, geometria de satélites em latitude alta. A caixa de
controle absorve tudo isso. O sinal que interessa é a **diferença** entre as caixas, não o
valor absoluto de nenhuma delas. Sem controle, o gráfico mede a idade da frota.

## Confundidores a tratar explicitamente

1. **Composição da frota.** Se a mistura de aeronaves mudou entre 2022 e 2026, o NACp médio
   muda sem jamming nenhum. Mitigação: agregar por aeronave-dia único, e checar a
   estabilidade do conjunto de ICAO24 observados.
2. **Cobertura de receptores.** A rede OpenSky/ADS-B cresceu. Mais receptores = mais
   aeronaves vistas, inclusive em baixa altitude. Isso pode *criar* sozinho a tendência de
   descida de altitude — que é justamente a nossa tese. **Este é o confundidor mais
   perigoso da matéria.** Mitigação: normalizar por total de aeronaves observadas na mesma
   faixa de altitude e mesma célula, e reportar a fração degradada, nunca a contagem bruta.
3. **Latitude alta.** Geometria de constelação é pior no Ártico. Por isso o controle está
   na mesma faixa de latitude.
4. **Viés de sobrevivência em baixa altitude.** Aeronave em solo ou taxiando também
   reporta. Filtrar `on_ground` e altitude mínima.

## Saídas

- `G1` série mensal: fração de aeronaves-dia com NACp degradado, caixa principal vs controle
- `G2` perfil de altitude: fração degradada por faixa (0–1000, 1000–3000, 3000–6000,
  6000–10000, >10000 m), comparando 2022–23 com 2025–26
- `G3` mapa de calor por célula H3, média do último ano

## Ordem de execução

```bash
python gpsjam_fetch.py --inicio 2022-02-01 --fim 2026-08-01
python gpsjam_series.py
python nacp_opensky.py --caixa finnmark --inicio 2022-02-01 --fim 2026-08-01
```

GPSJAM primeiro porque é barato e já dá a forma geral. Ele valida se vale gastar horas de
consulta no OpenSky — e onde olhar.
