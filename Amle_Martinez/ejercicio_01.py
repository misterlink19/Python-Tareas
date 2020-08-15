def cuenta_palabras(palabra):
    palabra = palabra.strip().split()
    return len(palabra)

palabra = "Verificando que aqui hay 6 palabras"

print(cuenta_palabras(palabra)) 