
x= "Curso de Python"
res= "Python" in x
res1="c#" in x
print(res)
print(res1)

res= "Python"  not in x
res1="c#" not in x
print(res)
print(res1)

res= "python" in x # p minisculo
res1="Python" in x
print(res)
print(res1)

texto= "curso de php"
palavra="php"
#python diferencia variavel inicial entre maiscula e miniscula
#python a ordem dos comamdos tbm diferencia, res= texto.upper() resultado diferente
res= palavra.upper() in texto.upper()
print(res)

x= "Curso de Python /"
f=" Curso de C#"

res= x + f
print(res)
print(x+f)
print(x,f)

dia=15
mes="janeiro"
ano=2021
cidade="Sao paulo"
cidade1="Curitiba"

print(dia,str.upper(mes),ano,str.upper(cidade) )
print(str (dia)," "+str.upper(mes)," "+str (ano)," "+str.upper(cidade1) )

data= "{},{} de {} {}\n{}"
print(data.format (cidade,dia,mes,ano,f))
data= "{},{} de {} {}\n\"{}\""
print(data.format (cidade1,dia,mes,ano,f))

# \"  \t  \n  \'  \r  \b