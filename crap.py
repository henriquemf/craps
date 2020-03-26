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
def roda_dados():
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    soma=dado1 + dado2
    return soma
def twelve(fichas1,fichas2):
    soma=roda_dados()
    if soma==12:
        print("Uau! Twelve! Você ganhou 30x o que apostou!")
        fichas1+=fichas2*30
        print("Você está com",fichas1,"fichas")
    else:
        print("Você perdeu! Que pena!")
        fichas1-=fichas2
        print("Você está com",fichas1,"fichas")
def field(fichas1,fichas2):
    soma=roda_dados()
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
def any_craps(fichas1,fichas2):
    soma=roda_dados()
    if soma==2 or soma==3 or soma==12:
        print("Boa! Any craps! Ganha 7x o que apostou!")
        fichas1+=fichas2*7
        print("Você está com",fichas1,"fichas")
    else:
        print("Você perdeu!")
        fichas1-=fichas2
        print("Você está com",fichas1,"fichas")
def pass_line_bet(fichas1,fichas2):
    soma=roda_dados()
    if soma==7 or soma==1:
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
def fase_point(fichas1,fichas2):
    soma=roda_dados()
    point=soma
    while soma!=7 or soma!=point:
        print("Vamos tentar de novo! Não deu 7 nem o Point!")
        point=soma
        soma=roda_dados()
    if soma==point:
        print("Parabéns! Você ganhou!")
        fichas1+=fichas2
        print("Você está com",fichas1,"fichas")
    elif soma==7:
        print("Você perdeu! Que pena!")
        fichas1-=fichas2
        print("Você está com",fichas1,"fichas")
pergunta=input("Você quer jogar Craps? ")
if pergunta=="não":
    print("Ok! Até a próxima!")
else:
    print("Vamos começar a jogar!")
    fichas1=50
    print("Você começa com 50 fichas!")
    aposta=int(input("Que tipo de aposta você quer? Digite 1 para Twelve, 2 para Any Craps e 3 para Field ou 4 para nenhuma dessas e que seja uma aposta normal"))
    fichas2=int(input("Quantas fichas quer apostar?"))
    if aposta==1:
        twelve(fichas1,fichas2)
    elif aposta==2:
        any_craps(fichas1,fichas2)
    elif aposta==3:
        field(fichas1,fichas2)
    elif aposta==4:
        pass_line_bet(fichas1,fichas2)