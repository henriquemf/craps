#Programa para simular o jogo de cassino Craps
#Fase Come out e Pass Line Bet: Se a soma dos dados der 7 ou 11, ele ganha e recebe as que apostou de volta + o mesmo valor de fichas que apostou
#Ainda nessa fase, se a soma der 2,3 ou 12 (craps), ele perde tudo que apostou
#Se a soma der 4,5,6,8,9,10, o jogo passa para a fase Point
#Na fase Point, a aposta feita continua valendo, o valor tirado anteriormente se torna o Point e para ganhar precisa
#tirar novamente o mesmo valor do Point
#Se ele acertar o mesmo valor do Point, ele ganha e recebe o que apostou de volta + o mesmo que apostou
#Se ele tirar 7 na fase Point ele perde tudo que ele apostou
#Se, na fase Point, ele tirar qualquer outro número que não 7 ou o Point, ele continua jogando até um veredito
#Quando acabar, volta para a fase Come Out
#Field=essa aposta pode rolar em qualquer parte do jogo. Se a soma der 5,6,7,8 ele perde, se for 3,4,9,10 ou 11 ele ganha o mesmo que apostou + o que já tinha apostado
#Se a soma for 2 em Field, ele ganha o que apostou + o dobro e, se sair 12, ele ganha o que apostou + o triplo
#Any Craps= Qualquer fase do jogo. Se a soma der 2,3 ou 12 ele ganha o que apostou + 7 vezes o que apostou, caso caia algo diferente, ele perde a aposta
#Twelve=Qualquer fase do jogo. Se a soma der 12, ele ganha o que apostou + 30x o que apostou, caso caia outra soma, ele perde a aposta
import random
pergunta=input("Você quer jogar Craps?")
craps=True
if pergunta=="não":
    craps=False
    print("Ok!Até mais!")
soma=0
while craps:
    contador=0
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    soma=dado1 + dado2
    fichas1=50
    fichas2=int(input("Quantas fichas você quer apostar? "))
    if fichas1==0:
        print("Acabaram suas fichas, tchau!")
        craps=False
    elif fichas2>fichas1:
        fichas2=int(input("Você não pode apostar mais do que tem. Quanto quer apostar? "))
    elif soma==7 or soma==11:
        print("Parabéns, você venceu!")
        fichas1=fichas2+fichas1
        pergunta=input("Você quer jogar novamente?")
        contador+=1
        if pergunta=="não":
            craps=False
    elif soma==2 or soma==3 or soma==12:
        print("CRAPS! Você perdeu!")
        fichas1=fichas1-fichas2
        pergunta=input("Você quer jogar novamente?")
        contador+=1
        if pergunta=="não":
            craps=False
    elif soma==4 or soma==5 or soma==6 or soma==8 or soma==9 or soma==10:
        point=True
        print("Você está indo para a fase Point")
        contador+=1
        while point:
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            soma=[0]*contador
            while soma[contador-1]!=7 or soma[contador-1]!=soma[contador-2]:
                point=True
                print("Vamos tentar de novo!")
                contador+=1
            if soma==7:
                print("Você perdeu!")
                point = False
                fichas1=fichas1-fichas2
                pergunta=input("Você quer jogar novamente?")
                if pergunta=="não":
                    craps=False
            elif soma[contador-1]==soma[contador-2]:
                print("Você ganhou!")
                fichas1=fichas1+fichas2
                point=False
                pergunta=input("Você quer jogar novamente?")
                if pergunta=="não":
                    craps=False
print("Obrigado, por jogar!")
print(fichas1)