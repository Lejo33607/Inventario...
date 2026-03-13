###                                                                                              Inventario y eso.

# Listas para guardar la información de los productos
nombres = []
precios = []
cantidades = []

# Preguntar cuántos productos se van a registrar
numero_productos = int(input("¿Cuántos productos desea registrar? "))

for i in range(numero_productos):

    print("Producto", i + 1)

    # Nombre del producto
    nombre = input("Ingrese el nombre del producto: ")
    nombres.append(nombre)

    # Precio del producto 
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            precios.append(precio)
            break
        except ValueError:
            print("Ingrese un número válido porfi.")

    # Cantidad del producto
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            cantidades.append(cantidad)
            break
        except ValueError:
            print("Ingrese un número entero porfi.")

# Mostrar inventario
print("--Inventario--")

for i in range(numero_productos):

    costo_total = precios[i] * cantidades[i]

    print(
        f"Producto: {nombres[i]} | Precio: {precios[i]} | Cantidad: {cantidades[i]} | Total: {costo_total}"
    )
