# ================================
# EJERCICIO 2
# Lista de Compras Interactiva
# ================================

lista_compras = []

print("="*60)
print("CALIFICACION LISTAS📋")
print("="*60)

while True:
    print("\n➕ 1. Agregar item a la lista")
    print("➖ 2. Eliminar item de la lista")
    print("👁️  3. Ver la lista completa")
    print("💨 4. Salir")

    print("=" * 50)
    opcion = input("🔘 Seleccione una opcion: ")

    if opcion == "1":
        producto = input("Ingrese el producto: ")
        lista_compras.append(producto)
        print(f"✅ El Producto {producto} fue agregado correctamente ")
    elif opcion == "2":
        producto = input("Ingrese el producto a eliminar: ")

        if producto in lista_compras:
            lista_compras.remove(producto)
            print(f"🔴 El Producto {producto} fue eliminado correctamente.")
        else:
            print(f"🆘 El producto {producto} no existe en la lista.")
    elif opcion == "3":
        print("\nLista de compras:")

        if len(lista_compras) == 0:
            print("La lista esta vacia.")
        else:
            for producto in lista_compras:
                print(producto)
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opcion invalida. INTENTE DE NUEVO")
