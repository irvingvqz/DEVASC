"""
El programa sigue corriendo hasta que el usuario ingrese el comando quit q
- Los break siempre deben de estar dentro de un bucle.
"""
while True:
    x=input("ingrese un numero para contar hasta: ")
    if x=='q' or x=='quit':
        break
    x=int(x)
    y=1
    while True: 
        print(y)
        y=y+1
        if y>x:
            break