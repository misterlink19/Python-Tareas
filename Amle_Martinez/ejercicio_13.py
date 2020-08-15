#Programa de lista de compras de supermercado

listado_de_compras = list()
total = float();

costoso = float(-99999999999)
nombre_costoso = ""
parar = False

print("Bienvenido al supermercado!")

while  not parar:
    #Obtengo los valores de la compra
    nombre = (input("\nEscriba su compra: ").lower().capitalize())
    
    if not any(compras["nombre"] == nombre for compras in listado_de_compras):
        cantidad = (input("Escriba su cantida: "))
        precio = float((input("Escriba su precio: ")))

        if precio >= costoso:
            costoso = precio
            nombre_costoso = nombre 

        #Los almaceno en un dicc. y luego los agrego a una lista
        compra = {"nombre" : nombre, "cantidad":int(cantidad), "precio": precio}
        listado_de_compras.append(compra)

        print("Producto agregado.")

        if input("\nQuiere agregar otro item?(s/n) ").upper() == "N":
            parar = True
    else:
        print("Lo siento, pero ese articulo ya esta en su lista de compras...")
        print("Intente de nuevo....")

print("\nSu compra fue:")
print("-------------------------------------------------------")
print("Nombre","Cantidad","Precio","monto a pagar", sep="\t")
print("-------------------------------------------------------")

for compra in listado_de_compras:
    total += float(compra["cantidad"]*compra["precio"])
    print ('{:<12s}{:<8d}\t{:<.2f}\t{:<.2f}'.format(compra["nombre"], compra["cantidad"] ,compra["precio"],float(compra["cantidad"]*compra["precio"])))

print("-------------------------------------------------------")
print(f"\tEl total a pagar es: {total:.2f}")

print(f"El producto mas costoso es: {nombre_costoso} que cuesta {costoso}\n")