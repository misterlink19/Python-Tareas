#Programa de lista de compras de supermercado

listado_de_compras = list()
total = float();

parar = False

print("Bienvenido al supermercado!")

while  not parar:
    #Obtengo los valores de la compra
    nombre = (input("\nEscriba su compra: ").lower().capitalize())
    
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
        print("Lo siento, pero ese articulo ya esta en su lista de compras...")
        print("Intente de nuevo....")

print("\nSu compra fue:")
# Podrias utilizar algo como 
guiones = "-" * 50
# Es más consistente 
print(guiones)
print("Nombre","Cantidad","Precio","monto a pagar", sep="\t")
print(guiones)

for compra in listado_de_compras:
    total += float(compra["cantidad"]*compra["precio"])
    print ('{:<12s}{:<8d}\t{:<.2f}\t{:<.2f}'.format(compra["nombre"], compra["cantidad"] ,compra["precio"],float(compra["cantidad"]*compra["precio"])))

print(guiones)
print(f"\tEl total a pagar es: {total:.2f}")