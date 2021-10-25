a=True
if a:# retorna True imprime 'curso de python'
    print('curso de python')
print('fim do progrma')

a=False# retorna False, vai direto para imprimir 'fim do programa'
if a:
    print('curso de python')
print('fim do progrma')

a=10
b=15
c=10
res=0
res1=0
op='+'

if a<b:
    print('curso de python')
print('fim do progrma')

if a>b:
    print('curso de python')
print('fim do progrma')

if a==b:
    print('curso de python')
print('fim do progrma')

if a==res:
    res=a+b
    print('soma de A,B:',res)
res1=a+c #dentro do escopo de if essa linha nao sera lida
print('soma de A,C:',res1)

if op=='+':
    res=a+b
    print('Soma de A,B:',res)
print('fim do progrma')

if op=='*':
    res=a*b
print(res)

if op=='-':
    res=a-b
print(str(a)+op+str(b)+'='+str(res))

if op=='/':
    res=a/b
print(res)

