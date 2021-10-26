
import os
os.system ('cls')

# inicializaçao da variavel de controle
#   while (teste logico)
#     comando 1
#     comando 2
#     .....
#     comando x
# controle, na variavel de inicialização de controle para não entrar em um loop infinito.
# inc, dec ou conttrole

carros=['golf','marajo','fusca','sandero','kombi','opala']
tam=len(carros)
i=0
while i<5:
  print(i,carros[i])
             #i=i+1
  i+=1

  if (i>=5):
    break

print('\nfim do loop')



