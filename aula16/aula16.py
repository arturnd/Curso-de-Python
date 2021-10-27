carro=['caravan','camaro','accord','focus','argos'] #array/list

carros=[['modelo','argos'],
        ['fabricante','gm'],
        ['ano','2019']
        ]
print(carros[0][0])
print(carros[0][1])
print(carros[1][0])
print(carros[1][1])
print(carros[2][0])
print(carros[2][1])

for l,c in carros:
    print(' linha  |',l+'   |'+c,'\n') # virgula separa e + "soma"
# l é linha, c é coluna e são padrao de matrizes

carro[2]='face'; print(carro)
for x in carro:
    print(x)

print(carro[3])
print(carro[0:4])
print(carro)

#---------------------------------------------------------------------

carros=[['modelo','argos'],
        ['fabricante','gm'],
        ['ano',2019]
        ]
carros [2][1]=2016
carros.append(['cor','prata']) #adiciona elemento a list


print(carros[0][0])
print(carros[0][1])
print(carros[1][0])
print(carros[1][1])
print(carros[2][0],'\t\n')
print(carros[2][1])
print(carros[3][0])
print(carros[3][1])




for l,c in carros:
    print(' linha  |', l, ' |',str(c))
