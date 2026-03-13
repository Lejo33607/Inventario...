#                                                           Inventario y eso.

# Solicitar nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar y validar el precio
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio.")

# Solicitar y validar la cantidad
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero para la cantidad.")

# Calcular el costo total
costo_total = precio * cantidad

# Mostrar resultados en consola
print("\n----- RESUMEN DEL PRODUCTO -----")
print("Producto:", nombre)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Costo total:", costo_total)

