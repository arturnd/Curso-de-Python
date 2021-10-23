num1=num2=res=0
canal1="CBF Cursos"

def cn():
    global canal
    canal="cursos castro"
    print(canal)
    print("\tVariavel Global, nome da variavel canal")
cn ()

def cn():
    print(canal1)
    print("\tVariavel Local nome da variavel canal1")
cn()


def cn():
    global canal2
    canal2 = "castro"
    print(canal2)
print("\n\tAqui nao foi exibido castro porque a cn() nao foi fechado")




