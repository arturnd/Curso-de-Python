


import os
os.system('cls')

#n1=10
#n2=15
def somar(n1,n2,n3,n4):
    r=n1+n2+n3+n4

    print('Curso de Pythom')
    print('Curso de C#')
    print(r) #informa o conteudo de r
    print('r') #informa a string r

somar(15,47,67,78)
somar(78,105,89,45)
somar(332,109,78,22)



def txt(*t):
    print(t[0])
    print(t[1])
    print(t[2])

txt('casa','vila','hoje','céu')

def txt(*tx):
    for t in tx:
     print('\t',t)
     print(str(len(tx)))

txt('casa','vila','hoje','céu','carro')



#=================================================
def somar(*num):
    r=0
    for n in num :
          r+=n
          print(str(r)) #informa a soma
          print(str (len(num))) #informa os elementos


somar(332,109,78,22,986)
#---------------------------------------------
def carros(c):
    print(c,":Accord")

carros("Modelo")
#--------------------------------------------------
def carros(c='Golf'):
    print('Modelo:',c)
carros()
#----------------------------------------------------

val=[1,2,5,7,15,20]
def somar(num):
    r=0
    for n in num :
          r+=n
          print(str(r)) #informa a soma
          print('\t',str (len(num))) #informa os elementos


somar(val)