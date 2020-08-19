#Programa de lista de compras de supermercado

listado_de_compras = list()

parar = False

print("Bienvenido al supermercado!")

while  not parar:
    #Obtengo los valores de la compra
    # No es necesario usar lower si usas str.capitalize()
    nombre = (input("\nEscriba su compra: ").lower().capitalize()) 
    
    # No necesitas usar any() para comprobar la existencia de un valor para la clave "nombre"
    # La idea aqui era mostrar un anuncio para que el usuario cambiara el nombre del articulo
    if not any(compras["nombre"] == nombre for compras in listado_de_compras):
        cantidad = (input("Escriba su cantida: "))
        precio = (input("Escriba su precio: "))

        #Los almaceno en un dicc. y luego los agrego a una lista
        compra = {"nombre" : nombre, "cantidad":int(cantidad), "precio": float(precio)}
        listado_de_compras.append(compra)

        print("Producto agregado.")

        if input("\nQuiere agregar otro item?(s/n) ").upper() == "N":
            parar = True
    else:
        # En el peor de los casos debiste sobre escribir los valores de cantidad, precio y monto, no negarlos
        print("Lo siento, pero ese articulo ya esta en su lista de compras...")
        print("Intente de nuevo....")

#Mostrando la cantidad de elementos agregados a la lista de compras    
print(f"\nHubieron {len(listado_de_compras)} elementos agregados ")

print("\nSu compra fue:")

print("Nombre","Cantidad","Precio","monto a pagar", sep="\t")

for compra in listado_de_compras:
    print ('{:<12s}{:<8d}\t{:<.2f}\t{:<.2f}'.format(compra["nombre"], compra["cantidad"] ,compra["precio"],float(compra["cantidad"]*compra["precio"])))
