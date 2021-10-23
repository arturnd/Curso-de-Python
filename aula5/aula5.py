

import random # Import necessario para reconhecer o random
num_p=10
num_h=5.2
num_d=1j
num_h= random.randrange(0,59)
num_gh= [ #list / Array
            random.randrange(0,59),
            random.randrange(0,59),
            random.randrange(0,59),
            random.randrange(0,59),
            random.randrange(0,59),
            random.randrange(0,59)
         ]

x=num_p; print(type(x))
x1=num_h; print(type(x1))
x2=num_d; print(type(x2))
# Convertido de string para inteiro, para que haja a junção, nao e possivel unir inteiro(x) com funçao (type)
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

x=num_gh
#Cria numeros aleatorio sem loop
print('Valor 1:',str(x[0]),'- Tipo '+ str(type(x[0])))
print('Valor 2:',str(num_gh[1]),'- Tipo '+ str(type(num_gh[1])))
print('Valor 3:',str(num_gh[2]),'- Tipo '+ str(type(num_gh[2])))
print('Valor 4:',str(num_gh[3]),'- Tipo '+ str(type(num_gh[3])))
print('Valor 5:',str(num_gh[4]),'- Tipo '+ str(type(num_gh[4])))
print('Valor 6:',str(num_gh[5]),'- Tipo '+ str(type(num_gh[5])))
