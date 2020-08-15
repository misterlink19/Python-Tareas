
def es_palíndromo (palabra1,palabra2):
    if palabra1 == palabra2[::-1]:
        return True
    else:
        return False

print(es_palíndromo("amor","roma"))