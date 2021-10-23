
j=5
k= input ("Digite um valor aqui: ")
print("Variavel j inteiro: ",(j),type(j))
print("Digitado :",k)
print("Variavel k string ",(type(k)))

x=1; print(type(x)) #inteiro
x="1"; print(type(x)) #string
x=1.5; print(type(x)) #float
x=True; print(type(x)) #bool
n1=3;n2=6;x=complex(n1,n2); print(type(x))#complexo
print("Parte Real: ",(x.real));print('Parte Imag: ',(x.imag))
x=["carro","navio","aviao","trem"]; print(type(x)) #list / array
print("posicao 1: ",x[0]);  print("posicao 2: ",x[1]);print("posicao 3: ",x[2]);print("posicao 4: ",x[3]);
x=("carro","navio","aviao","trem"); print(type(x)) # tuple nao se altera o conteudo se usa () e list altera o conteudo usa []
x=range (0,10,1); print(type(x)) # range cria um list nesse caso de 0 a 10 de 1 em 1
x={
    "terrestre":"carro",
    "maritimo":"navio",
    "aereo":"aviao"
}; print(type(x)) #dict
print("Valores",x["terrestre"],x['maritimo'],x['aereo'])
x={5,7,8,6,4,5,7,2,1,1,3,3,6,8,5};print(type(x)) #set
print((x))
x=frozenset({5,7,8,6,4,5,7,2,1,1,3,3,6,8,5});print(type(x)) #bloqueia o set
