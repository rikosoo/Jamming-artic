# 04 — Comunicação satélite-a-satélite

**Pergunta central:** as constelações estão migrando o tráfego para enlaces ópticos entre
satélites, fora do alcance de qualquer antena terrestre. Isso resolve o problema de
interferência — ou apenas o move para onde ninguém consegue observá-lo?

**Prioridade: última.** É a mais técnica, a mais dependente de fonte especializada e a que
tem menos dado aberto. Mas é a que envelhece melhor: é a arquitetura para onde o setor está
indo.

## A contradição que é a pauta

Nas duas frases seguintes, ambas correntes na literatura do setor, está a matéria inteira:

> "Enlaces ópticos entre satélites têm segurança aumentada, já que não podem ser
> interceptados nem sofrer jamming."

> "Feixes ópticos são estreitos e difíceis de interceptar do solo — o que não os torna
> imunes a risco cibernético, spoofing, comprometimento de terminal, falha de roteamento
> ou risco de cadeia de suprimentos."

A primeira é verdadeira sobre **física** e falsa sobre **sistemas**. Um feixe laser entre
dois satélites em LEO é, de fato, muito difícil de interceptar ou abafar do chão: é
estreito, direcional e aponta para cima. Mas o enlace não é o sistema. O terminal óptico é
software, o roteamento é software, o apontamento é software, e nada disso deixa de ser
atacável por o meio ser luz.

**A tese provisória:** a migração para óptico não elimina a superfície de ataque — ela a
desloca do espectro para o código, e do observável para o invisível. Hoje qualquer pessoa
com um receptor de rádio de US$ 30 pode confirmar que há jamming no Finnmark. Ninguém, de
fora do operador, pode verificar o que acontece entre dois satélites.

**E é isso que deveria assustar um jornalista:** não a vulnerabilidade, mas o fim da
verificação independente. Todo este projeto — a matéria do Ártico inclusive — só existe
porque aeronaves transmitem em aberto uma declaração sobre a própria precisão. Uma
arquitetura sem esse equivalente é uma arquitetura sobre a qual só o dono pode fazer
afirmações.

## O que já é fato (a confirmar em primário)

- **A SpaceX equipa os Starlink com terminais laser**, com o objetivo declarado de reduzir a
  dependência de estações terrenas. O plano previa quatro enlaces ópticos por satélite,
  ligando cada um a dois satélites do mesmo plano orbital e dois de planos adjacentes.
- **Arquitetura em duas redes:** uma de rádio, ligando usuários, gateways e satélites; outra
  óptica, ligando satélites entre si. Os crosslinks permitem rotear tráfego pelo espaço em
  vez de obrigar cada conexão a descer no gateway mais próximo.
- Há mercado maduro de terminais ópticos para LEO — vários fornecedores com produto de
  prateleira. Ou seja: não é exclusividade de um operador, é o padrão emergente.

## Ângulos apuráveis

1. **Quem consegue auditar?** Se o tráfego não desce, que autoridade nacional tem
   visibilidade sobre o que trafega, e sob que jurisdição? Um pacote que entra em São Paulo,
   sobe, cruza cinco satélites e desce em Lisboa passou por onde, legalmente? Esta é
   provavelmente a melhor matéria do conjunto e não exige nenhum dado técnico secreto —
   exige regulador respondendo pergunta difícil. **ANATEL é fonte obrigatória.**
2. **Resiliência real.** Se crosslinks reduzem a dependência de estações terrenas, reduzem
   também o efeito de um ataque como o do KA-SAT (pauta 01)? Ou concentram o risco no
   software de roteamento? Pergunta para engenheiro, não para assessoria.
3. **O apontamento.** Manter dois terminais alinhados a milhares de km é um problema de
   controle que depende de conhecer a própria posição e atitude — que depende de GNSS.
   **Se a pauta 02 e esta se encontram em algum lugar, é aqui.** Vale confirmar com fonte
   técnica se degradação de GNSS afeta aquisição de enlace óptico. Se afetar, o beat inteiro
   fecha num círculo e vira uma matéria só.
4. **Soberania.** O Brasil depende crescentemente de conectividade LEO estrangeira, inclusive
   em serviço público e em região remota. Que garantias existem, contratualmente, sobre
   continuidade e sobre inspeção?

## Fontes

Documental: papers sobre laser inter-satellite links em constelações Starlink (há literatura
aberta, inclusive no arXiv), catálogos de fornecedores de terminais ópticos, registros
regulatórios de operação no Brasil. Humanas: pesquisadores de redes espaciais, ANATEL,
operadores de gateway no Brasil, CYSAT.

## Pendências

1. Confirmar a configuração atual dos crosslinks Starlink — o "quatro terminais" é de
   material mais antigo e pode ter mudado.
2. Localizar as duas frases contraditórias em fontes citáveis e nomeadas. **A matéria
   depende de poder atribuir as duas.** Sem isso, viram espantalho.
3. Checar se existe algum mecanismo público de verificação de enlace óptico — se existir,
   a tese central desta pauta cai, e é melhor descobrir agora.
4. Perguntar à ANATEL sobre jurisdição de tráfego roteado em órbita. A resposta, qualquer
   que seja, é matéria.
