
# Toma en cuenta las recomendaciones anteriores. 
# El uso de slice y un index inverso está bien para este caso de uso,
# pero debes comprender cuando no lo sea

# Este ejercicio se resolvia con una fuc de una linea en su cuerpo
def es_palíndromo (palabra1,palabra2):
    return palabra1 == palabra2[::-1]

print(es_palíndromo("amor","roma"))