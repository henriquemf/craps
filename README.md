# EP 1 - Craps

## Integrantes: 
- Henrique Martinelli Frezzatti
- Lívia Sayuri Makuta

## Objetivo:
O objtivo principal desse projeto é simular uma versão simplificada do jogo de apostas Craps em Python.

## Como funciona?
O jogo começa na fase `Come Out`, em que é selecionado as apostas, sendo elas Pass Line Bet, Twelve, Any Craps e Field.

São rodados 2 dados, não viciados e numerados de 1 a 6, e a soma entre eles é o que determina quando se ganha ou se perde uma aposta.

Regras:
- Caso o jogador selecione a fase Pass Line Bet, se a soma dos dados der 7 ou 11, ele ganha e recebe as que apostou de volta + o mesmo valor de fichas que apostou. Se a soma der 2,3 ou 12 (o que chamamos de Craps), ele perde tudo que apostou. Se a soma der 4,5,6,8,9,10, o jogo passa para a fase Point.

- Na fase Point, a aposta feita continua valendo, a soma tirado anteriormente se torna o Point e para ganhar precisa tirar novamente o mesmo valor do Point. Se ele acertar o mesmo valor do Point, ele ganha e recebe o que apostou de volta mais o mesmo que apostou. Se ele tirar 7 na fase Point ele perde tudo que ele apostou. Caso não dê nem 7 e nem Point, a rodada continua valendo até ter um veredito final.

- Na aposta Field, a qual pode acontecer em qualquer parte do jogo, se a soma der 5,6,7,8 ele perde, se for 3,4,9,10 ou 11 ele ganha o mesmo que apostou + o que já tinha apostado. Se a soma for 2 em Field, ele ganha o que apostou mais o dobro e, se sair 12, ele ganha o que apostou mais o triplo.

- Na aposta Any Craps, a qual pode acontecer em qualquer parte do jogo, se a soma der 2,3 ou 12 ele ganha o que apostou mais 7 vezes o que apostou, caso caia algo diferente, ele perde a aposta.

- Na aposta Twelve, a qual pode acontecer em qualquer parte do jogo, se a soma der 12, ele ganha o que apostou mais 30 vezes o que apostou, caso caia outra soma, ele perde a aposta.

- Caso o jogador faça uma aposta durante o andamento ou antes de entrar na fase Point, ele sai dessa fase e vai para a aposta, a qual acontece independentemente da fase Point.
