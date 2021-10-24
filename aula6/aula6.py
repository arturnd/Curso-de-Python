
x="Curso de Python"
print(x)
print(x[0])
print(x[1:5])
print(x[0],x[2],x[4],x[6])
print(x[1],x[3],x[5],x[7])

print('Tamanho:',str (len(x)) )

x= '  Curso de Python  '
print(x)

print(x.strip())
print(x.rstrip())
print(x.lstrip())

print(x.lower())
print(x.upper())
print(x.upper().strip())
print(x.replace("Python","C#"))

x= 'Curso de Python'
a=x.split(" ")
print([a])
print(a[0])
print(a[1])
print(a[2])