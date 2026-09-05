# 01 — Hijacking de space assets

**Pergunta central:** o que é preciso, hoje, para que alguém que não é o dono passe a dar
ordens a um satélite — e por que a resposta é mais barata do que o público imagina?

## O ângulo que evita a ficção científica

A imagem popular é a de alguém "invadindo um satélite" pelo espaço. A realidade documentada
é mais prosaica e mais grave: **quase nunca se ataca o satélite. Ataca-se quem fala com
ele.** O satélite é o ativo; a superfície de ataque é terrestre e administrativa —
credenciais, cadeia de fornecedores, o segmento de gestão da rede.

Isso reorganiza a pauta. Não é uma matéria sobre órbita. É uma matéria sobre governança de
acesso a um ativo de bilhões de dólares que não pode receber visita técnica.

## O que já é fato (a confirmar em primário)

**Viasat / KA-SAT, 24 de fevereiro de 2022** — o caso canônico. No dia da invasão da
Ucrânia, um ataque deixou modems KA-SAT inoperantes na Ucrânia. Segundo a SentinelLabs, o
vetor foi um malware batizado de **AcidRain**, um wiper para ELF MIPS que destrói o sistema
de arquivos de modems e roteadores. O acesso teria vindo da exploração de um **appliance de
VPN mal configurado**, que deu entrada ao segmento de gestão "confiável" da rede.

Dois detalhes fazem a matéria:

1. **O transbordamento.** ~5.800 turbinas eólicas da Enercon, na Alemanha, ficaram sem
   comunicação de monitoramento remoto. Ninguém quis atacar energia eólica alemã. É o mesmo
   padrão da matéria do Ártico — o dano relevante foi o que vazou do alvo.
2. **A atribuição formal.** EUA, Reino Unido, UE e aliados atribuíram o ataque à Rússia,
   especificamente ao GRU e à unidade conhecida como Sandworm (Unit 74455). Ter atribuição
   estatal formal é raro e é o que torna esta pauta publicável sem malabarismo.

**CYSAT 2023, Paris** — pesquisadores demonstraram tomar controle de um satélite da ESA
(o **OPS-SAT**, projetado justamente para ser experimentado). Nuance obrigatória, e é ela
que separa reportagem de alarme: os pesquisadores **receberam acesso à carga útil**; um
atacante real precisaria de credenciais válidas, acesso à carga e capacidade de subir
software. Não foi invasão remota do nada — foi demonstração de o que acontece *depois* que
o acesso existe.

**Hack-A-Sat / Moonlighter** — a Space Force pôs em órbita um satélite feito para ser
alvo de competição de segurança. Existe, portanto, uma comunidade pública que faz isso com
autorização, e ela fala.

**SPARTA** (The Aerospace Corporation) — framework aberto que cataloga táticas e técnicas
de comprometimento de sistemas espaciais, análogo ao ATT&CK. É a espinha conceitual da
pauta e a prova de que o setor já trata isso como problema corrente, não hipotético.

## O ângulo brasileiro

O que o Brasil opera, e quem responde por isso: SGDC (o satélite geoestacionário de defesa
e comunicações estratégicas), a constelação Amazônia-1 e os satélites do INPE, os
enlaces do sistema de monitoramento da Amazônia. Perguntas apuráveis:

- Quem tem autoridade de comando sobre cada um, e onde ficam fisicamente esses centros?
- Há requisito de segurança cibernética em contrato de operação? Auditoria independente?
- O Brasil tem doutrina publicada para comprometimento de ativo espacial? Quem seria
  acionado — Comando de Defesa Cibernética, ANATEL, AEB, Ministério da Defesa?
- Já houve incidente? A pergunta feita formalmente já é matéria, respondida ou não.

## Fontes de dados

Não há telemetria aberta aqui — esta é pauta de documento e fonte humana. Substitutos úteis:
SPARTA (mapa de técnicas), CCDCOE e EuRepoC (incidentes catalogados com análise jurídica),
relatórios da SentinelLabs e afins, atas e apresentações de CYSAT e da Aerospace Village
(DEF CON), contratos e editais públicos de operação de satélite.

## Pendências

1. Ler a análise técnica original do AcidRain e a cronologia da CCDCOE.
2. Confirmar o número das turbinas Enercon e a redação exata da atribuição aliada.
3. Confirmar os termos exatos do experimento OPS-SAT com a ESA — a nuance do acesso prévio
   é o que impede a matéria de virar sensacionalismo, e precisa estar certa.
4. Mapear os operadores brasileiros e fazer os pedidos via LAI.

## A linha

Descrever classe de vulnerabilidade e cadeia de responsabilidade. Nunca caminho executável,
nunca identificadores operacionais. Se a apuração encontrar exposição aberta, divulgação
responsável ao operador e à autoridade antes de publicar. Ver `README.md`.
