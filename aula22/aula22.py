

soma=lambda a,b:a+b
r=soma (6,9)
print(soma(7,15))
print(r) #o resultado da lambda precisa ser lançado em uma variavel
mult=lambda  a,b,c:(a+b)*c
r1=mult (6,9,5)
print(r1)
print((lambda a,b,c,d:(a+c)*(b+d))(3,4,5,3))

r=lambda x,func: x+func(x) #func não é função do sistema, nesse caso é nomeação de argumento da lambda
res=r(2,  lambda x:x*x)
print(res)

res=r(2, lambda x:x+x)
print(res)