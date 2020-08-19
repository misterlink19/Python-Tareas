# Excelente, eres (hasta el momento) el unico que entendio como realizar este ejercicio.
def cambiar_caso(palabra):
    lista_palabra = list(palabra)

    for letra in range(len(lista_palabra)):
        if lista_palabra[letra] == lista_palabra[letra].upper():
            lista_palabra[letra] = lista_palabra[letra].lower()
        else:
            lista_palabra[letra] = lista_palabra[letra].upper()
    
    return "".join(lista_palabra)

print(cambiar_caso("adIos mUndO"))