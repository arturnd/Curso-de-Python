
#chave/key - valor/value

carro={
       'Fabricante':'Honda',
       'Modelo':'Accord',
       'Ano':'2020'
       }
carro['Estado']='Sao Paulo'

carro.pop('Estado')  #del carro['Estado']
carro['Modelo']='HRV'      # alteração sempre no elemento correspondente nunca no mesmo
fab=carro['Fabricante']
fab1=carro.get('Fabricante') #Matriz diferencia minuscula de maiuscula
print(carro)
print(carro['Modelo'])
print(fab)
print(fab1)
print(carro['Ano'])

if 'Modelo' in  carro:
       print('Sim,Modelo é uma chave')

print('Qual o tamanho do dictory:',str(len(carro)))

for x in carro:
       print('\n',x) # mostra chave
       print(carro[x]) #mostra valores

for c,v in carro.items():
       print('\n',c+':'+v)

carro.clear() # limpa o directiony

