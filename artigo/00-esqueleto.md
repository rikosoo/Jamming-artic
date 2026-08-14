# Esqueleto da matéria

**Título de trabalho:** O céu sem GPS — como o jamming virou clima permanente no Ártico europeu

**Tese em uma frase:** O jamming de GNSS no Alto Norte deixou de ser incidente e virou
condição ambiental permanente; e ele está descendo em altitude, o que transfere o risco
da fase de cruzeiro para a fase de aproximação.

**Extensão-alvo:** 2.500–3.500 palavras + 3 gráficos originais.

**O que a matéria tem de novo:** o método existe e é revisado por pares — Felux et al.
(2024), *NAVIGATION* 71(3) — mas foi aplicado aos países bálticos, ao mar Negro e ao
Mediterrâneo oriental, na janela fev–dez/2022. O Ártico europeu não está lá, nem os quatro
anos seguintes. Somamos a isso o corte por altitude, que nenhum agregado público oferece.
Os números que circulam na imprensa são contagens de notificações — input administrativo,
sujeito a viés de reporte. NACp é medida física, vinda da própria aeronave.

---

## 0. Abertura (250–350 palavras)

**Cena:** setembro de 2025, Vardø. Um Dash-8 da Widerøe aborta o pouso.

O que a cena precisa entregar, em ordem:
- O momento concreto (aproximação, o que o piloto vê, o que a aeronave deixa de saber).
- A informação de que aquilo não foi excepcional: acontece quase diariamente.
- O gancho da tese: o que mudou não é a existência do jamming, é a altitude dele.

**A evitar:** abrir com estatística. A estatística é a seção 2, e ela pesa mais depois
que o leitor já viu uma aproximação abortada.

**Precisão obrigatória:** o pouso não foi abortado só por jamming. Foi jamming **somado a
teto baixo de nuvens** — sem visual, e sem GNSS, não sobra procedimento. Escrever isso
direito é o que separa a matéria do alarmismo, e não custa nada: a combinação é mais
assustadora que a causa única, porque é a combinação que se repete todo inverno ártico.

**Pendência de apuração:** relato em primeira pessoa de piloto que voa a rota
Tromsø–Kirkenes. Sem isso a abertura fica de segunda mão. Ver `entrevistas.md`.

---

## 1. Cronologia: 2017 → 2026 (400–500 palavras)

Não é lista. É a demonstração de três inflexões:

| Inflexão | Quando | O que muda |
|---|---|---|
| Aparecimento | set/2017 | Pilotos da Widerøe perdem GPS durante o Zapad-2017. Ainda é anomalia ligada a exercício. |
| Continuidade | outono/2022 | Jamming deixa de ser episódico e passa a contínuo — depois dos ataques de drones ucranianos a alvos dentro da Rússia. **Esta é a inflexão real, não fevereiro.** |
| Descida | 2024–2026 | Jamming forte sobre Varanger a 500 m. Deixa de ser fenômeno de alta altitude. |

O texto tem de deixar claro por que "aparecimento em 2017" importa: o fenômeno é anterior
à invasão. Isso derruba a leitura de causa única e obriga a falar de continuidade da
atividade de guerra eletrônica em Kola.

**A moldura Zapad.** A primeira observação coincide com o Zapad-2017; o aborto de Vardø
ocorre durante o Zapad-2025. Oito anos, o mesmo exercício, os dois extremos da série — é
uma moldura pronta e boa demais para desperdiçar. Mas ela carrega uma armadilha: sugere
que o jamming é episódico. **Não é, e essa é a tese.** Os exercícios são os picos visíveis;
o que mudou foi o vale entre eles. Abrir e fechar a seção com o par Zapad, e dizer isso
com todas as letras.

Detalhe factual em `cronologia-fatos.md`, com fonte por linha. Texto em `secao-1-cronologia.md`.

---

## 2. Os números — e por que os oficiais não bastam (400–500 palavras)

Duas famílias de dado, e a diferença entre elas é o argumento metodológico da matéria:

**(a) Notificações administrativas.** Finlândia: ~1.200 notificações de interferência de
GPS na aviação em um ano, contra 239 no ano anterior. Salto de ordem de grandeza.
Limitação a declarar explicitamente: contagem de notificações mede também a propensão a
notificar. Um aumento de 5x pode ser 5x mais jamming, ou mais consciência do problema,
ou mudança de procedimento de reporte. Provavelmente os três.

**(b) Telemetria.** É onde entra a análise própria — seção 3.

Aqui também entra a resposta institucional como fato: a Nkom planeja duas estações de
monitoramento adicionais em 2026. Um Estado que instala sensores é um Estado que já
concluiu que o fenômeno é permanente. Usar isso como evidência de mudança de regime,
não como nota de rodapé burocrática.

---

## 3. A análise própria: o que o NACp mostra (600–800 palavras) — NÚCLEO

Explicar em linguagem de leitor não-técnico, nesta ordem:

1. Toda aeronave transmite por ADS-B, junto com sua posição, um índice de quanta
   confiança ela tem naquela posição — o NACp (Navigation Accuracy Category — position).
2. Quando o receptor GNSS é degradado, o NACp cai. A aeronave está declarando, em aberto,
   que perdeu precisão.
3. Logo: milhares de aeronaves comerciais funcionam como uma rede de sensores de jamming
   que ninguém instalou de propósito. Existe metodologia publicada usando exatamente esse
   campo para medir extensão e frequência de eventos. Replicamos no Ártico.

**Gráficos (todos originais — ver `analise/`):**

- **G1 — Série temporal 2022→2026.** % de aeronaves com NACp degradado por mês,
  na caixa do Finnmark. Mostra a permanência: a linha nunca volta ao chão.
- **G2 — Perfil de altitude.** Degradação por faixa de altitude, comparando 2022–23 com
  2025–26. É o gráfico que sustenta a tese. Se a distribuição desceu, a tese está provada
  com dado próprio. Se não desceu, a tese muda e a matéria fica sobre outra coisa —
  registrar isso agora, antes de rodar, para não forçar o resultado.
- **G3 — Mapa de calor geográfico.** Onde. Gradiente esperado leste→oeste a partir da
  fronteira russa. Serve de checagem de sanidade: se a fonte é oriental, o gradiente aparece.

**Regra:** a análise roda antes desta seção ser escrita. Nenhuma frase aqui é redigida por
antecipação do resultado.

---

## 4. O argumento da altitude (400–500 palavras) — O CORAÇÃO DA TESE

Por que 500 m é categoricamente diferente de 10.000 m:

- **Em cruzeiro** o GNSS é conveniência. A aeronave tem inercial, tem VOR/DME, tem tempo.
  Perder GPS é incômodo e papelada.
- **Em aproximação** o GNSS é parte do procedimento. Aproximações RNP/GNSS existem
  exatamente onde não há infraestrutura terrestre — que é a definição de Vardø, Vadsø,
  Kirkenes: aeroportos pequenos, tempo ruim, terreno, pouca redundância em solo.
- **A margem** é o que encolhe: menos altitude, menos tempo, menos alternativas de
  aeroporto (o alternado mais próximo pode estar a centenas de km, também sob jamming).

O aborto de pouso em Vardø é a ilustração exata desse encadeamento. Usar aqui, e não na
abertura, o detalhe técnico do que falhou.

**O fecho da seção — e o achado da apuração.** A Nkom não descreve o jamming como ataque à
Noruega: descreve como transbordamento da autodefesa eletromagnética das bases de Kola,
feito com alta potência e sem consideração por vazar para o país vizinho. Kirkenes está a
~55 km de Pechenga. Daí decorre a frase mais dura da matéria, e ela é literalmente
verdadeira: **ninguém está mirando a rampa de aproximação de Vardø — e é exatamente por
isso que ninguém vai calibrá-la para poupá-la.** A degradação a 500 m não é decisão de
alguém; é a borda de um cobertor eletromagnético grande demais. Não há a quem apelar.

**Pendência:** confirmar com a Avinor/Widerøe quais aproximações nesses aeroportos são
GNSS-dependentes e o que resta de backup terrestre. Isso é o fato que fecha a seção.

---

## 5. Quem mais depende disso (400–500 palavras)

O jamming é tratado como problema de aviação porque a aviação tem sistema de notificação.
Os outros setores não têm — e por isso somem da estatística. Nomear os que somem:

- **Pesca.** Barra de Barents. Posicionamento, plotagem de redes, e sobretudo
  rastreamento obrigatório (VMS) e diários de bordo eletrônicos. Pergunta a apurar: o que
  acontece com a conformidade regulatória de um barco cujo sinal de posição some?
- **Aviação regional.** Não é só atraso: é a estrutura de transporte de comunidades onde o
  avião substitui a estrada. Cancelamento em Vardø não é inconveniência, é isolamento.
- **Agrimensura, construção, mineração.** RTK/GNSS de precisão é o mais frágil de todos —
  precisa de fase de portadora, cai antes de qualquer aviação notar.
- **Ambulância aérea e busca e salvamento.** O caso em que a degradação e a necessidade
  ocorrem no mesmo lugar e na mesma hora.

**Regra editorial:** cada setor entra com um número ou um nome. Nada de "também é afetado".

---

## 6. Mitigação: o que realmente funciona (400–500 palavras)

Em ordem crescente de custo e de eficácia:

- **Multi-constelação (GPS + Galileo + GLONASS + BeiDou).** Ajuda contra interferência de
  banda estreita, não contra jamming de banda larga. Barato, já embarcado, insuficiente.
- **Antena CRPA (controlled reception pattern antenna).** Anula espacialmente a direção do
  jammer. Funciona de verdade. Caro, pesado, historicamente militar — a pergunta jornalística
  é o que impede a certificação civil e quanto custaria numa frota Dash-8.
- **eLoran.** Terrestre, alta potência, baixa frequência — difícil de jammear por sua
  natureza física. O Reino Unido e a Coreia do Sul já se moveram nessa direção. Para a
  Noruega é decisão de Estado, não de operador. Status atual: apurar.
- **O que não é solução:** notificar. NOTAM não faz a aeronave saber onde está.

Fechar com a assimetria: mitigar custa milhões por frota; jammear custa um transmissor.

---

## 7. Fecho (200–250 palavras)

Voltar a Vardø. O ponto final não é "está piorando" — é que o sistema já se adaptou a
operar sob degradação permanente, e adaptação silenciosa é como um risco deixa de ser
contado.

E há o ponto que a apuração entregou: um ataque pode ser protestado, negociado, cessado.
Um transbordamento, não. Enquanto houver drones ameaçando Kola, haverá escudo eletrônico
sobre Kola; e enquanto houver escudo, a borda dele cai sobre o Finnmark. Não existe
interlocutor para esse problema — existe só a decisão norueguesa de conviver com ele ou
de pagar para se blindar.

A pergunta que fica: quantos abortos de pouso são normais antes de deixarem de ser notícia?

---

## Checklist antes de publicar

- [ ] Toda estatística tem link primário em `fontes.md`
- [ ] Os três gráficos são reprodutíveis a partir de `analise/` do zero
- [ ] Limitações metodológicas do NACp declaradas no corpo do texto, não em nota
- [ ] Pelo menos uma voz de piloto e uma de operador não-aviação (pesca)
- [ ] Direito de resposta / pedido de comentário: Nkom, Avinor, Traficom, Widerøe
- [ ] Nenhuma afirmação de atribuição (quem opera o jammer) além do que a fonte sustenta
