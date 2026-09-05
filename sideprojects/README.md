# Sideprojects — o beat de segurança espacial

Cinco pautas adjacentes à matéria do Ártico. Não são cinco assuntos diferentes: são cinco
camadas do mesmo sistema, e o que as une é uma pergunta só —

> **A infraestrutura espacial civil foi construída sobre a suposição de que ninguém
> atacaria o sinal. Essa suposição acabou. O que ainda depende dela?**

O jamming no Finnmark é o caso mais visível porque tem aviões dentro. Mas ele é a camada
mais externa e mais barata de um problema que vai da antena da estação terrena até o
enlace entre dois satélites.

## As cinco pautas

| # | Pauta | Camada atacada | Estado |
|---|---|---|---|
| 01 | Hijacking de space assets | O satélite | 🔨 pauta montada |
| 02 | Jamming | O sinal descendente | ✅ **matéria em produção** — ver `../artigo/` |
| 03 | Spoofing | A verdade do sinal | 🔨 pauta montada |
| 04 | Comunicação satélite-a-satélite | O enlace em órbita | 🔨 pauta montada |
| 05 | Defesa de estações terrenas | O elo mais fraco | 🔨 pauta montada |

Ordem sugerida de execução: **03 → 05 → 01 → 04**.

Spoofing primeiro porque reaproveita integralmente o método e as fontes do Ártico, e
porque há um dado público enorme e pouco explorado. Estações terrenas depois, porque é a
mais concreta e a mais apurável no Brasil. Hijacking e satélite-a-satélite são as mais
difíceis: dependem de fontes técnicas e de leitura de documentação, não de dados abertos.

## O método, que é o mesmo em todas

O que fez a matéria do Ártico funcionar foi uma escolha metodológica, não um furo: **buscar
a medida física em vez da contagem administrativa**. Notificações medem o fenômeno somado à
nossa atenção ao fenômeno; telemetria mede o fenômeno. Toda pauta aqui deve ser testada por
essa pergunta antes de começar:

1. Existe um dado que a própria máquina emite, sem intermediação de quem reporta?
2. Existe um grupo de controle possível — outro lugar, outro período, outra frota?
3. Qual é o confundidor que poderia produzir sozinho o resultado que eu espero encontrar?

Se as três não tiverem resposta, a pauta é entrevista e documento, não análise de dados —
e isso precisa estar decidido antes, não depois de gastar semanas.

## A linha editorial

Estas são pautas de **prestação de contas e defesa**: o que está exposto, quem sabia, quem
é responsável, quanto custa consertar. Não são manuais.

Regra prática, e ela não é burocracia — é o que separa jornalismo de segurança de
publicidade para atacante:

- **Descrever a classe de vulnerabilidade, não o caminho.** "Um appliance de VPN mal
  configurado deu acesso ao segmento de gestão" é reportagem. Parâmetros, frequências
  operacionais, identificadores de comando e configurações específicas não são.
- **Divulgação responsável antes da publicação.** Se a apuração encontrar exposição real e
  ainda aberta, avisa-se o operador e a autoridade competente primeiro, com prazo. Isso é
  padrão da área e também é a única postura defensável se algo acontecer depois.
- **Não publicar o que só serve para repetir o ataque.** O teste: se um trecho não muda a
  compreensão do leitor sobre risco ou responsabilidade, mas ajudaria alguém a executar,
  ele sai.

Fora isso, tudo o que está aqui é público, documentado e frequentemente publicado pelos
próprios órgãos de defesa — quatro das cinco pautas se apoiam em material que governos e
centros de pesquisa divulgam justamente para que operadores se protejam.

## Fontes que servem a mais de uma pauta

| Fonte | Serve a | O que é |
|---|---|---|
| **SPARTA** (The Aerospace Corporation) | 01, 05 | Framework aberto de táticas e técnicas de ataque a sistemas espaciais — o equivalente do ATT&CK para o espaço. É o mapa conceitual de todo o beat. |
| **Hack-A-Sat / Moonlighter** (US Space Force) | 01 | Competição de segurança com satélite real em órbita, feito para ser atacado. Fonte de gente que fala. |
| **CYSAT** (conferência, Paris) | 01, 04, 05 | Onde pesquisadores demonstraram controle de um satélite da ESA em 2023. Pauta de campo. |
| **Jammertest** (Andøya, setembro) | 02, 03 | Maior exercício aberto de jamming/spoofing, dados abertos. |
| **OpenSky / ADSB Exchange / GPSJAM** | 02, 03 | Telemetria de aeronaves. Já em uso em `../analise/`. |
| **AIS (navegação marítima)** | 03 | O equivalente naval do ADS-B. Fonte principal da pauta de spoofing. |
| **EASA, OPSGROUP, ICAO** | 02, 03 | Alertas operacionais a tripulações — datam e localizam eventos. |
| **CCDCOE / EuRepoC** | 01, 05 | Repositórios de incidentes cibernéticos com análise jurídica. |

## Aviso sobre o estado deste material

Nenhuma pauta aqui foi apurada — são mapas de partida, montados a partir de busca web, com
o mesmo bloqueio de egress que afetou o projeto principal. Cada afirmação factual traz a
origem; **nada foi confirmado em fonte primária.** Tratar como hipótese de trabalho, e
verificar antes de escrever uma linha.
