# ================================
# EJERCICIO 2
# Lista de Compras Interactiva
# ================================

# Lista donde se guardan los productos ingresados por el usuario.
lista_compras = []

print("=" * 60)
print("🛒 LISTA DE COMPRAS")
print("=" * 60)

# Repite el menu hasta que el usuario decida salir.
while True:
    print("\n1. ➕ Agregar item a la lista")
    print("2. ➖ Eliminar item de la lista")
    print("3. 📋 Ver la lista completa")
    print("4. 🚪 Salir")

    print("=" * 50)
    opcion = input("👉 Seleccione una opcion: ")

    if opcion == "1":
        # Agrega un nuevo producto al final de la lista.
        producto = input("📝 Ingrese el producto: ")
        lista_compras.append(producto)
        print(f"✅ El producto {producto} fue agregado correctamente.")
    elif opcion == "2":
        # Solicita el producto que se desea quitar.
        producto = input("🗑️ Ingrese el producto a eliminar: ")

        # Solo elimina el producto si ya existe en la lista.
        if producto in lista_compras:
            lista_compras.remove(producto)
            print(f"✅ El producto {producto} fue eliminado correctamente.")
        else:
            print(f"❌ El producto {producto} no existe en la lista.")
    elif opcion == "3":
        # Muestra todos los productos almacenados.
        print("\n📋 Lista de compras:")

        if len(lista_compras) == 0:
            print("📭 La lista esta vacia.")
        else:
            for producto in lista_compras:
                print("•", producto)
    elif opcion == "4":
        # Finaliza la ejecucion del programa.
        print("👋\n Saliendo de consola........")
        break
    else:
        # Informa cuando la opcion no coincide con el menu.
        print("⚠️ Opcion invalida. Intente de nuevo.")
