

import random
num_p=10
num_h=5.2
num_d=1j
num_h= random.randrange(0,59)

x=num_p; print(type(x))
x1=num_h; print(type(x1))
x2=num_d; print(type(x2))
# Convertido de string para inteiro, para que haja a junçãp, nao e possivel unir inteiro(x) com funçao (type)
print('Valor:',str(x),'- Tipo '+ str(type(x)))
print('Valor:',str(x1),'- Tipo '+ str(type(x1)))
print('Valor:',str(x2),'- Tipo '+ str(type(x2)))
#Convertido de float para inteiro por int
x1= int (num_h)
print('Valor:',str(x1),'- Tipo '+ str(type(x1)))
#Conversão de int para Float
x= float(num_p)
print('Valor:',str(x),'- Tipo '+ str(type(x)))
#Cria numeros aleatorios com random.randrange
x=num_h
print('Valor:',str(x),'- Tipo '+ str(type(x)))

