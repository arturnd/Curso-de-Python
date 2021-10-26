import os

carros=[]
carro=input('Digite o nome do carro: ')
i=0
while carro !='-1':
    carros.append(carro)
    carro = input('Digite o nome do carro: ')


os.system('cls')

for x in carros:
    print(x)

print('fim do loop')