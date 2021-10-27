
l_carros=['fusca','pageiro','s18']
t_carros=('fusca','pageiro','s18')
for x in l_carros:
    l_carros[2]='sandero' #lista[] aceita adiçao, tupla() nao se edita
    t_carros.count(t_carros)

    print(x)

print(t_carros)
for x in t_carros:
        print(x)
lt_carros=list(t_carros)
lt_carros[2]="face"
print(lt_carros);print(type(lt_carros))

lt_carros=tuple(lt_carros); print (type(lt_carros))
print(lt_carros)