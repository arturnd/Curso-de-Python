
import random
import os
os.system ('cls')

x=random.randrange(0,100)
x1=int(input('Digite um numero entre 1 e 100: '))
x2=1
while (x !=x1 ):

    if x1 > x:
        print('Erro, número menor que ',x1)
    elif x1 < x:
        print('Erro, número maior que ',x1)

    os.system('cls')

    x2 += 1
    x1=int(input('Digite um numero entre 1 e 100: '))


print('Parabéns, vc acertou o número é:', x1, 'em', x2, 'tentativas')




