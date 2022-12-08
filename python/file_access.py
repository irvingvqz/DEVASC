"""
open(name, [mode]
"r" - leer el archivo(modo predeterminado si se omite el modo).
"w" - escribir sobre el archivo, remplazando el contenido del archivo.  
"a" - adjuntar al archivo.
"""


file=open ("abrir.txt", "r")
for item in file:
    print(item)
file.close()

"""
python agrega lineas en blanco entre el contenido, se quitan con el 
método strip()
"""
file=open ("abrir.txt", "r")
for item in file:
    item=item.strip()
    print(item)
file.close()
