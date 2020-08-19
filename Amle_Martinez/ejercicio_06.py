
# url="uasdvirtual.uasd.edu.do/diplomados/my"
url = "prueba.hostname.com"

# Este ejercicio es mas manejable con expresiones regulares. 
# Tu conext era la url de ejemplo y al probarla no arroja la salida esperada. 

#No funciona con url que empiecen sub-dominios extraños como es. u otros parecidos
def obtener_dominio_url(url):
    url_partes = url.split("/")

    # En uno de los ejercicios anteriores utilizaste strip 
    # para eliminar los espacios en blanco, porque utilizar este metodo aquí?
    if url_partes[1] == '':
        url_partes.pop(0) # La sig sentencia es redundante
        url_partes.remove('') # ??

    dominio = url_partes[0].split(".")

    if "www" in dominio:
        dominio.pop(0)

    dominio = "." +".".join(dominio[1:])

    # Entiendo el enfoque que tomaste, pero no es el correcto, debes revisar el codigo
    
    return(dominio)

print(obtener_dominio_url(url))