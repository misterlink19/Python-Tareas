
compras = list()

print("Bienvenido al supermercado!")

while "parar" not in compras:
    # Porque no simplemente rompias el bucle cuando la entrada era igual a 'parar'?
    compras.append(input("\nEscriba su compra aqui: "))
    print("Producto agregado.")

compras.pop() # Precisamente por esta razon debes cuidar la entrada a la lista 
print(f"Se agregaron: {len(compras)} elementos")
print("Su compra fue:")

for compra in compras:
    print(compra)

