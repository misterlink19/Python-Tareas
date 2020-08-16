# Programa de lista de compras de supermercado

compra = dict()
listado_de_compras = list()

nombre_costoso = str()
costoso = float()

nombre_economico = str()
economico = float()

total = 0
parar = False

# Se abre el archivo en modo r, para manejar su lectura
with open("Lista_de_compras.txt","r") as archivo:
    if archivo.read(1):
        contador = 0
        # Recorremos las lineas del archivo para obtener las informaciones de los productos
        for lineas in archivo:
            
            if contador == 4:
                cadena = lineas.split()    
                
                if "-------------------------------------------------------" in cadena:
                    contador +=1
                    continue
                else:
                    c = 0
                    # Se usa un for para pasar por cade elemento de la lista,
                    # porque python lanza el error de range out index si no se hace de esta manera. 
                    # antes lo intentaba a usar key:cadena[indice] y no dejaba.
                    for l in cadena:
                        if c == 0:
                            compra = {"nombre": l}
                            c +=1
                        elif c == 1:
                            compra.update({"cantidad" : int(l)})
                            c +=1
                        elif c == 2:
                            compra.update({"precio": float(l)})
                            break  
                    listado_de_compras.append(compra)    
            # Estos 2 elif, son para obtener los productos costosos
            # y economicos de manera mas sencilla
            elif contador == 6:
                cadena = lineas[29:]
                cadena = cadena.split()
                
                nombre_costoso = cadena[0]
                costoso = float(cadena[-1])
                contador += 1
            
            elif contador == 7:
                cadena = lineas[31:]
                cadena = cadena.split()
                
                nombre_economico = cadena[0]
                economico = float(cadena[-1])
                contador += 1
            else:
                contador += 1
        
def busca_producto(nombre_producto):
    try:
        global listado_de_compras
        for producto in listado_de_compras:
           if producto["nombre"] == nombre_producto:
               print("Producto encontrado!")
               return producto    
    except:
        print("\nProducto no encontrado...\n")
        raise

def agrega_producto(producto):
    if type(producto) == dict:
        global listado_de_compras
        global costoso
        global economico
        global nombre_costoso
        global nombre_economico

        if not any(articulo["nombre"] == producto["nombre"] for articulo in listado_de_compras):
            
            # Cambiando los tipos de datos de cantidad y precio
            producto["cantidad"] = int(producto["cantidad"])
            producto["precio"] = float(producto["precio"])

            if producto["precio"] >= costoso:
                costoso = precio
                nombre_costoso = nombre 
        
            if producto["precio"] <= economico:
                economico = precio
                nombre_economico = nombre

            listado_de_compras.append(producto)

            print("Producto agregado")
        else:
            print("Lo siento, pero ese articulo ya esta en su lista de compras...")
    else:
        print("Error, faltan datos sobre el producto")

def elimina_producto(nombre_de_producto):
    try:
        contador = 0
        global listado_de_compras
        for producto in listado_de_compras:
            if producto["nombre"] == nombre_de_producto:
                global costoso
                global economico
                global nombre_costoso
                global nombre_economico
                
                costoso = -9999999.99
                economico = 9999999.99

                listado_de_compras.pop(contador)

                for producto in listado_de_compras:
                    if producto["precio"] >= costoso:
                        costoso = producto["precio"]
                        nombre_costoso = producto["nombre"] 
            
                    if producto["precio"] <= economico:
                        economico = producto["precio"]
                        nombre_economico = producto["nombre"]

                print("\nProducto eliminado!\n")
                
            contador += 1
    except:
        print("Ese Producto no existe...")
        raise


def guarda_cambios():

    global listado_de_compras
    global costoso
    global economico
    global nombre_costoso
    global nombre_economico
    global total

    archivo = open("Lista_de_compras.txt","w+")
    
    archivo.write("Su compra fue:\n")
    archivo.write("-------------------------------------------------------\n")
    archivo.write("Nombre\t"+"Cantidad\t\t"+"Precio\t"+"monto a pagar\n")
    archivo.write("-------------------------------------------------------\n")

    for compra in listado_de_compras:
        total += float(compra["cantidad"]*compra["precio"])
        archivo.writelines ( '{:<12s}{:<8d}\t{:<.2f}\t{:<.2f}\n'.format(compra["nombre"], compra["cantidad"] ,compra["precio"],float(compra["cantidad"]*compra["precio"])))

    archivo.write("-------------------------------------------------------\n")
    archivo.write(f"\tEl total a pagar es: {total:.2f}\n")
    archivo.write(f"El producto mas costoso fue: {nombre_costoso} que cuesta {costoso}\n")
    archivo.write(f"El producto mas economico fue: {nombre_economico} que cuesta {economico}\n")

    # Mensaje pensado para que salga cuando sea utilizado fuera en otro programa.
    # print("Lista guardada en un archivo txt, llamado 'Lista_de_compras' \n")
    archivo.close()

while  not parar:
    print("\nBienvenido al supermercado!")
    print("--------------------------------------------")
    print("1.-Agregar producto")
    print("2.-Buscar producto")
    print("3.-Eliminar producto")
    print("4.-Salir")
    print("--------------------------------------------")
    
    opcion = input("Eliga una opcion: ")
    
    if opcion == "1":
        # Obtengo los valores de la compra
        nombre = (input("\nEscriba su compra: ").lower().title())
        cantidad = int(input("Escriba su cantida: "))
        precio = float((input("Escriba su precio: ")))
         
        producto ={"nombre" : nombre, "cantidad":cantidad, "precio": precio}

        agrega_producto(producto)

        input("Pulse cualquier tecla para continuar")
        print("\n\n")

    elif opcion == "2":
        nombre = (input("\nEscriba el nombre a buscar: ").lower().title())
        producto = busca_producto(nombre)
        print("El producto: \n", producto.values())
        input("Pulse cualquier tecla para continuar")
        print("\n\n")

    elif opcion == "3":
        nombre = (input("\nEscriba el nombre a eliminar: ").lower().title())
        
        elimina_producto(nombre)

        input("Pulse cualquier tecla para continuar")
        print("\n\n")

    elif opcion == "4":
        input("Pulse cualquier tecla para continuar")
        print("\n\n")

        parar = True
    
    else:
        print("Error, esa opcion no existe\n\n")

guarda_cambios()

print("\nSu compra fue:")
print("-------------------------------------------------------")
print("Nombre","Cantidad","Precio","monto a pagar", sep="\t")
print("-------------------------------------------------------")

for compra in listado_de_compras:   
    print ('{:<12s}{:<8d}\t{:<.2f}\t{:<.2f}'.format(compra["nombre"], compra["cantidad"] ,compra["precio"],float(compra["cantidad"]*compra["precio"])))

print("-------------------------------------------------------")
print(f"\tEl total a pagar es: {total:.2f}")

print(f"El producto mas costoso fue: {nombre_costoso} que cuesta {costoso}")
print(f"El producto mas economico fue: {nombre_economico} que cuesta {economico}\n")
print("Lista guardada en un archivo txt, llamado 'Lista_de_compras' \n")