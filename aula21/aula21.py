

val=[1,2,5,7,15,20]
def somar(num):
    r=0
    for n in num :
          r+=n
          print(str(r)) #informa a soma
          print('\t',str (len(num))) #informa os elementos
print(val)

#------------------------------------------------------------

val=[1,2,5,7,15,20,34,89,65]
def somar(num):
     r=0
     for n in num :
      r+=n

     #return ('Vazio') #Só pode um return no escopo, isto é, seguido
     return (r)  #Sem return informa None

print(somar(val))

def valorval (num):
    for v in num:
        print(v)

valorval(val)

r=somar(val)

print('A soma da list:',val,'é',str(somar(val)))
print(r)