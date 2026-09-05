# 05 — Defesa de estações terrenas

**Pergunta central:** o ativo caro está em órbita, mas o ponto frágil está num galpão com
cerca e um link de internet. Quem cuida dele?

**Prioridade: segunda da fila.** É a mais concreta, a mais apurável no Brasil e a que tem o
melhor material público de apoio.

## Por que é o elo mais fraco

Um satélite custa centenas de milhões, é redundante, é blindado contra radiação e é
inalcançável fisicamente. A estação terrena que fala com ele é um prédio, com funcionários,
fornecedores, contratos de manutenção, VPN e computadores rodando software desatualizado.

**O caso KA-SAT (pauta 01) é a demonstração exata disso** e serve às duas matérias: não se
atacou nada em órbita. Segundo a análise técnica, explorou-se um appliance de VPN mal
configurado para alcançar o segmento de gestão da rede, e a partir dali se destruíram
modems no chão — com transbordamento para ~5.800 turbinas eólicas na Alemanha. O ativo
espacial nunca foi tocado, e o serviço morreu do mesmo jeito.

Essa é a frase da matéria: **não é preciso alcançar o espaço para derrubar um serviço
espacial.**

## As camadas de exposição, que organizam a apuração

1. **Física.** Onde ficam as estações, quem entra, o que se vê do lado de fora. Antenas de
   grande porte são visíveis por imagem de satélite e frequentemente mal protegidas —
   várias estão em terreno aberto, algumas com localização publicada em documento
   regulatório. Apurável sem sair da mesa, e depois com visita.
2. **De rede.** O segmento de gestão, o acesso remoto, os fornecedores com credencial. Foi
   por aqui que caiu o KA-SAT.
3. **De cadeia de suprimentos.** Quem fabrica o modem, quem atualiza o firmware, quem tem
   chave de assinatura. É o vetor mais difícil de reportar e o mais subestimado.
4. **De governança.** Quem é legalmente responsável quando uma estação terrena comercial
   opera um enlace de serviço público essencial? Há requisito de segurança em contrato?
   Há auditoria? Quem fiscaliza?

A camada 4 é onde mora a matéria brasileira, e é a única que não depende de nenhuma
informação sensível — depende de contrato, edital e regulador.

## O ângulo brasileiro, que é forte

O Brasil tem estações terrenas ligadas a serviço essencial: monitoramento da Amazônia
(INPE), comunicações estratégicas de defesa (SGDC), meteorologia, telecom em região remota,
e agora gateways de constelações LEO estrangeiras operando em território nacional.

Perguntas que se fazem com LAI e com telefone, não com técnica:

- Quantos gateways de constelações estrangeiras operam no Brasil, e onde? A ANATEL autoriza
  — logo existe lista.
- Que requisitos de segurança cibernética constam das autorizações? Há inspeção?
- Quem responde por um incidente em gateway estrangeiro em solo brasileiro? Operador,
  ANATEL, Comando de Defesa Cibernética?
- O monitoramento da Amazônia depende de qual cadeia terrestre, e ela tem redundância? Uma
  interrupção de alguns dias em época de queimada tem consequência mensurável — e essa é a
  matéria com cara de Brasil, não de resenha de relatório estrangeiro.
- Já houve incidente reportado? O pedido formal, respondido ou negado, já rende texto.

## Fontes

**SPARTA** (The Aerospace Corporation) é o mapa: framework aberto de táticas e técnicas
contra sistemas espaciais, criado para que operadores se defendam. Serve para estruturar a
apuração e para dar vocabulário preciso ao texto — e o fato de existir, mantido por uma
FFRDC do setor de defesa americano, é por si só a prova de que a ameaça é tratada como
corrente.

Além dele: **CCDCOE** e **EuRepoC** (incidentes catalogados, com leitura jurídica),
**CYSAT** e a **Aerospace Village** da DEF CON (comunidade que fala), análise técnica do
AcidRain, e no Brasil — ANATEL, AEB, INPE, Ministério da Defesa, e os contratos públicos.

## Pendências

1. Levantar na ANATEL a lista de estações/gateways autorizados e a base normativa.
2. Ler o SPARTA e escolher, dele, as três ou quatro técnicas que estruturam a reportagem —
   sem transformar o texto em glossário.
3. Confirmar em primário a cadeia do KA-SAT (VPN → segmento de gestão → wiper nos modems) e
   o número das turbinas.
4. Mapear a dependência terrestre do monitoramento da Amazônia. É o ângulo que dá
   consequência local e tira a matéria do registro geopolítico abstrato.

## A linha

Vale repetir aqui, porque é a pauta em que a tentação é maior: **localização e detalhe de
proteção física de instalação crítica não se publicam** só porque são obteníveis. O critério
é o do `README.md` — se um trecho não muda a compreensão do leitor sobre risco e
responsabilidade, mas ajudaria alguém a agir, ele sai. Exposição encontrada e ainda aberta
vai primeiro ao operador e à autoridade, com prazo, antes da publicação.
