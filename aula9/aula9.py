carros=["corsa","c3","hb20","fit","s10"]
print(carros)
print(carros[3])
print(carros[0])
print(carros[-1],carros[-3])

carros[3]='fusion'
print(carros)

carros.append('face')
carros.append('meriva')
carros.append('fit')
print(carros)
# informa quantidade de itens na list
print(len(carros))

print (str((len(carros))) + " carroas na lista")

carros.remove('meriva')
carros.remove('fit')
print(carros)

carros.pop() #tira o ultimo da lista
print(carros)

carros.pop(2) #tira o objeto indicado na lista
print(carros)

del carros [2] #apaga o objeto indicado na lista
print(carros)

carros2=list(carros)
print ('Total de carros copiados da lista 1 para lista 2:',len (carros2))

carros3=['fusca','uno','c4','brasilia']
carros4=carros3+carros
print(carros4)
print ('Total de carros copiados da lista 4:',len (carros4))