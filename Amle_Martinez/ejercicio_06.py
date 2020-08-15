
url="uasdvirtual.uasd.edu.do/diplomados/my"

#No funciona con url que empiecen sub-dominios extraños como es. u otros parecidos
def obtener_dominio_url(url):
    url_partes = url.split("/")

    if url_partes[1] == '':
        url_partes.pop(0)
        url_partes.remove('')

    dominio = url_partes[0].split(".")

    if "www" in dominio:
        dominio.pop(0)

    dominio = "." +".".join(dominio[1:])
    
    return(dominio)

print(obtener_dominio_url(url))