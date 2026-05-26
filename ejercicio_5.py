# ================================
# EJERCICIO 5
# Mini Sistema de Gestion de Inventario
# ================================

# Lista donde se almacenan todos los productos registrados.
inventario = []


def agregar_producto():
    # Solicita los datos del producto y crea su registro.
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad disponible: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")


def realizar_venta():
    # Pide el nombre del producto vendido y la cantidad a descontar.
    nombre = input("Producto vendido: ")
    cantidad_vendida = int(input("Cantidad vendida: "))

    # Busca el producto dentro del inventario.
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            # Comprueba si hay unidades suficientes antes de restar.
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] = producto["cantidad"] - cantidad_vendida
                print("Venta realizada correctamente.")
            else:
                print("No hay suficiente cantidad disponible.")
            return

    print("El producto no existe en el inventario.")


def mostrar_inventario():
    # Muestra la informacion de cada producto almacenado.
    print("\nInventario actual:")

    if len(inventario) == 0:
        print("El inventario esta vacio.")
    else:
        for producto in inventario:
            print("-------------------")
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Cantidad:", producto["cantidad"])


# Mantiene disponible el menu principal del sistema.
while True:
    print("\nSISTEMA DE INVENTARIO")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        realizar_venta()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        # Termina la ejecucion del programa.
        print("Programa finalizado.")
        break
    else:
        print("Opcion invalida.")
