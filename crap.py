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
def roda_dados():             #Função de roda os dados e retorna a soma deles
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    soma=dado1 + dado2
    return soma
def twelve(fichas1,fichas2):   #Função que determina a aposta Twelve
    soma=roda_dados()
    fichas2=int(input("Você selecionou Twelve, quanto quer apostar? "))
    print("A soma deu: ",soma)
    if soma==12:
        print("Uau! Twelve! Você ganhou 30x o que apostou!")
        fichas1+=fichas2*30
        print("Você está com",fichas1,"fichas")
    else:
        print("Você perdeu! Que pena!")
        fichas1-=fichas2
        print("Você está com",fichas1,"fichas")
def field(fichas1,fichas2):     #Função que determina a posta Field
    soma=roda_dados()
    fichas2=int(input("Você selecionou Field, quanto quer apostar? "))
    print("A soma deu: ",soma)
    if soma==5 or soma==6 or soma==7 or soma==8:
        print("Que pena! Você perdeu")
        fichas1-=fichas2
        print("Você está com",fichas1,"fichas")
    elif soma==3 or soma==4 or soma==9 or soma==10 or soma==11:
        print("Você ganhou!")
        fichas1+=fichas2
        print("Você está com",fichas1,"fichas")
    elif soma==2:
        print("Boa! A soma deu 2! Ganha o dobro!")
        fichas1+=fichas2*2
        print("Você está com",fichas1,"fichas")
    elif soma==12:
        print("Field! Você tirou 12 e recebe o triplo!")
        fichas1+=fichas2*3
        print("Você está com",fichas1,"fichas")
def any_craps(fichas1,fichas2):   #Função que determina a aposta Any Craps
    soma=roda_dados()
    fichas2=int(input("Você selecionou Any Craps, quanto quer apostar? "))
    print("A soma deu: ",soma)
    if soma==2 or soma==3 or soma==12:
        print("Boa! Any craps! Ganha 7x o que apostou!")
        fichas1+=fichas2*7
        print("Você está com",fichas1,"fichas")
    else:
        print("Você perdeu!")
        fichas1-=fichas2
        print("Você está com",fichas1,"fichas")
def pass_line_bet(fichas1,fichas2):   #Função que determina a aposta Pass Line Bet
    soma=roda_dados()
    fichas2=int(input("Você selecionou Pass Line Bet, quanto quer apostar? "))
    print("A soma deu: ",soma)
    if soma==7 or soma==11:
        print("Você ganhou!")
        fichas1+=fichas2
        print("Você está com",fichas1,"fichas")
    elif soma==2 or soma==3 or soma==12:
        print("CRAPS! Você perdeu!")
        fichas1-=fichas2
        print("Você está com",fichas1,"fichas")
    elif soma==4 or soma==5 or soma==6 or soma==8 or soma==9 or soma==10:
        print("POINT! Você vai para a fase Point!")
        fase_point(fichas1,fichas2)
def fase_point(fichas1,fichas2):     #Função que determina a fase Point
    aposta=int(input("Como você quer prosseguir? Para Twelve digite 1, para Any Craps digite 2, para Field digite 3 e, para continuar no Point, digite 4 "))
    if aposta==1:
        entrar_point=False
        twelve(fichas1,fichas2)
    elif aposta==2:
        entrar_point=False
        any_craps(fichas1,fichas2)
    elif aposta==3:
        entrar_point=False
        field(fichas1,fichas2)
    elif aposta==4:
        entrar_point=True
        while entrar_point:
            soma=roda_dados()
            point=soma
            while soma!=7 or soma!=point and entrar_point:
                print("A soma deu: ",soma,"e o Point foi de: ",point)
                print("Vamos tentar de novo! Não deu 7 nem o Point!")
                aposta=int(input("Como você quer prosseguir? Para Twelve digite 1, para Any Craps digite 2, para Field digite 3 e, para continuar no Point, digite 4: "))
                if aposta==1:
                    twelve(fichas1,fichas2)
                    entrar_point=False
                elif aposta==2:
                    any_craps(fichas1,fichas2)
                    entrar_point=False
                elif aposta==3:
                    field(fichas1,fichas2)
                    entrar_point=False
                elif aposta==4:
                    entrar_point=True
                point=soma
                soma=roda_dados()
            if point==soma:
                print("A soma deu: ",soma,"e o Point foi de: ",point)
                print("Parabéns! Você ganhou!")
                fichas1+=fichas2
                print("Você está com",fichas1,"fichas")
                entrar_point=False
            elif soma==7:
                print("A soma deu: ",soma,"e o Point foi de: ",point)
                print("Você perdeu! Que pena!")
                fichas1-=fichas2
                print("Você está com",fichas1,"fichas")
                entrar_point=False
fichas1=50
pergunta=input("Você quer jogar Craps? ")
if pergunta=="não":
    print("Ok! Até a próxima!")
else:
    craps=True
    while craps:
        print("Vamos começar a jogar!")
        print("Você começa com",fichas1,"fichas!")
        aposta=int(input("Que tipo de aposta você quer? Digite 1 para Twelve, 2 para Any Craps e 3 para Field ou 4 para Pass Line Bet: "))
        fichas2=0
        if aposta==1:
            twelve(fichas1,fichas2)
        elif aposta==2:
            any_craps(fichas1,fichas2)
        elif aposta==3:
            field(fichas1,fichas2)
        elif aposta==4:
            pass_line_bet(fichas1,fichas2)
        pergunta=input("Você quer jogar novamente? ")
        if pergunta=="não":
            print("Ok! Obrigado por jogar!")
            craps=False
        elif pergunta=="sim":
            craps=True 