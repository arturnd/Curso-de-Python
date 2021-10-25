clima='sol'
dinheiro=800
lugar=''



a=10
b=15
res=0
op='-'

if op=='+':
    res=a+b
elif op=='*':
    res=a*b
elif op=='-':
    res=a-b
elif op=='/':
    res=a/b
else: #else tem que ter a mesma estrutura do if e elif
    print('nao exite operaçao compativel')

print(str(a)+op+str(b)+'='+str(res))

if clima=='sol' and(dinheiro > 300 and dinheiro < 600):#2 condiçoes para verdadeiro
    lugar='clube'

else:
    lugar=('cinema')
print('vou ao',lugar)


if clima=='sol' or (dinheiro > 300 and dinheiro < 600):#apenas uma condição para verdadeiro
    lugar='clube'

else:
    lugar=('cinema')
print('vou ao',lugar)

#      AND                       OR
#    V  V  = V                F  F  = V
#    V  F  = F                V  F  = V
#    F  V  = F                F  F  = F
#    F  F  = F                V  V  = V