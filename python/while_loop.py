x=input("ingrese un numero para contar hasta: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1

"""
Usando una comprobación booleana para detener el bucle cuando la 
comprobación se evalúa como falsa

tener en cuenta que la key True es con T mayúscula

"""
x=input("ingrese un numero para contar hasta: ")
x=int(x)
y=1
while True: 
    print(y)
    y=y+1
    if y>x:
        break