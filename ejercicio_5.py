# ================================
# EJERCICIO 5
# Mini Sistema de Gestion de Inventario
# ================================

inventario = []


def agregar_producto():
    nombre = input("📦 Nombre del producto: ")
    precio = float(input("💲 Precio del producto: "))
    cantidad = int(input("🔢 Cantidad disponible: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("✅ Producto agregado correctamente.")


def realizar_venta():
    nombre = input("🛒 Producto vendido: ")
    cantidad_vendida = int(input("➖ Cantidad vendida: "))

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] = producto["cantidad"] - cantidad_vendida
                print("✅ Venta realizada correctamente.")
            else:
                print("⚠️ No hay suficiente cantidad disponible.")
            return

    print("❌ El producto no existe en el inventario.")


def mostrar_inventario():
    print("\n📋 Inventario actual:")

    if len(inventario) == 0:
        print("📭 El inventario esta vacio.")
    else:
        for producto in inventario:
            print("-------------------")
            print("📦 Nombre:", producto["nombre"])
            print("💲 Precio:", producto["precio"])
            print("🔢 Cantidad:", producto["cantidad"])


while True:
    print("\n🏪 SISTEMA DE INVENTARIO")
    print("1. ➕ Agregar producto")
    print("2. 🛍️ Realizar venta")
    print("3. 📦 Mostrar inventario")
    print("4. 🚪 Salir")

    opcion = input("👉 Seleccione una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        realizar_venta()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("👋 Programa finalizado.")
        break
    else:
        print("⚠️ Opcion invalida.")
