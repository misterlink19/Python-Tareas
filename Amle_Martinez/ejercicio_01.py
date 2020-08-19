def cuenta_palabras(palabra):
    # Buen detalle al eliminar los espacios de los lados, pero no tiene sentido en tu codigo 
    # split tomara el spacio como caracter de division 
    # En teoria esta es la respuesta, me hubise gustado que recorrieras el string 
    # y agotaras la mayor manipulacion de str posible. De todos modos, buen trabajo.  
    palabra = palabra.strip().split()
    return len(palabra)

palabra = "Verificando que aqui hay 6 palabras"

print(cuenta_palabras(palabra)) 