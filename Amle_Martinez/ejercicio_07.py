
compras = list()

print("Bienvenido al supermercado!")

while "parar" not in compras:
    compras.append(input("\nEscriba su compra aqui: "))
    print("Producto agregado.")

compras.pop()
print(f"Se agregaron: {len(compras)} elementos")
print("Su compra fue:")

for compra in compras:
    print(compra)

