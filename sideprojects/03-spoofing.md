# 03 — Spoofing

**Pergunta central:** jamming apaga o sinal; spoofing mente. O que acontece com um sistema
de transporte inteiro quando a mentira é convincente o bastante para ser obedecida?

**Prioridade: primeira da fila.** Reaproveita integralmente o método, a pipeline e as fontes
da matéria do Ártico, e tem um conjunto de dados público, enorme e pouco explorado.

## Por que é uma matéria diferente de jamming, e não uma variação

Jamming produz uma ausência — a aeronave sabe que não sabe onde está, e degrada com
consciência. É o que o NACp registra: a máquina declarando desconfiança de si mesma.

Spoofing produz uma **certeza falsa**. O receptor não degrada: ele acredita. E age. Toda a
lógica de segurança de aviação e navegação — checagem cruzada, alerta, procedimento
alternativo — foi desenhada para lidar com perda de dado, não com dado convincente e errado.

Essa diferença tem consequência jornalística direta: **spoofing não aparece bem no NACp.**
Um receptor enganado pode reportar excelente precisão. A métrica que sustenta a matéria do
Ártico é parcialmente cega para esta pauta, e o texto tem de dizer isso. A detecção aqui é
outra: incoerência entre posição reportada e trajetória fisicamente possível, saltos de
posição, divergência entre GNSS e inercial, relógios errados.

## O que já é fato (a confirmar em primário)

- **Oriente Médio, a partir de 2023.** Pilotos começaram a reportar sistemas de navegação
  assumidos por sinais falsos, às vezes indicando posição a centenas de milhas do real.
  Em 2023, ao menos **20 aeronaves civis** teriam sido induzidas a voar próximo ao espaço
  aéreo iraniano sem autorização — o que é, além de risco de navegação, risco político.
- **Abril de 2024:** ataques de spoofing no Oriente Médio ultrapassaram, pela primeira vez,
  **1.500 voos afetados por dia**.
- **Efeitos em cascata dentro da aeronave:** o TAWS (sistema de alerta de terreno) pode
  interpretar mal a altitude e emitir alerta de "pull up"; há relatos de erro de
  temporização, saltos de posição e falhas de transponder. **Este é o parágrafo mais
  importante da pauta:** o spoofing não engana só o mapa, engana os sistemas que existem
  para salvar o voo quando o mapa falha.
- **Orientação operacional:** a OPSGROUP recomenda que tripulações reinicializem o sistema
  de GPS ao sair de uma área de spoofing. Uma recomendação assim, publicada, é a prova de
  que o problema deixou de ser teórico e virou procedimento.
- **Lado regulatório:** a EASA publicou material sobre spoofing como risco crescente à
  segurança de voo, com autoria ligada à autoridade civil norueguesa — o que costura esta
  pauta de volta à do Ártico.

## Os dados — e o furo que ninguém pegou

**AIS marítimo é o equivalente naval do ADS-B, e é mais escancarado.** Navios transmitem
posição continuamente, e o spoofing marítimo já produziu casos documentados de embarcações
"aparecendo" em portos onde não estavam, ou desenhando círculos impossíveis. Diferente da
aviação, boa parte do histórico de AIS é acessível.

O método que a matéria do Ártico já provou se transporta direto:

1. **Detecção por impossibilidade física**, não por índice declarado: velocidade implícita
   entre posições consecutivas acima do possível para a classe do navio; salto de posição;
   trajetória circular sobre terra firme.
2. **Caixa de controle** em região sem conflito, mesma época, mesmas rotas.
3. **Confundidor a domar antes de começar:** falha de receptor barato e erro de transcrição
   de AIS produzem exatamente o mesmo artefato que spoofing. A pergunta que decide a pauta é
   se a anomalia é **coletiva e geograficamente coerente** — muitos navios errando juntos,
   no mesmo lugar, é spoofing; um navio errando sozinho é equipamento ruim.

**Ângulo brasileiro possível:** costa brasileira, plataformas da Bacia de Campos e do
pré-sal, e o tráfego do Atlântico Sul. Existe anomalia de AIS aqui? A resposta provavelmente
é "pouca" — e uma matéria que mede e mostra que **não** há é jornalismo legítimo e raro,
desde que o texto não finja suspense.

## Fontes

Dados: AIS histórico, ADS-B (OpenSky, já configurado), GPSJAM. Documental: EASA, OPSGROUP,
ICAO, NOTAMs. Humanas: Jammertest em Andøya (setembro — é o lugar onde spoofing é feito
legalmente e estudado em aberto), pesquisadores de Stanford e do laboratório de GNSS que
publicam observações de spoofing, autoridade civil norueguesa.

## Pendências

1. Confirmar em primário todos os números acima — os "20 aeronaves", os "1.500 voos/dia",
   e o surto de abril de 2024. São de reportagem e de material de indústria.
2. Definir o recorte geográfico **antes** de olhar os dados. Oriente Médio, mar Negro e
   Báltico são os candidatos óbvios; escolher um e registrar a escolha em config.
3. Levantar a disponibilidade real de AIS histórico gratuito e seus limites de cobertura.
4. Verificar se o efeito no TAWS está documentado por autoridade ou só por relato de
   tripulação. A diferença decide se é manchete ou parágrafo.
