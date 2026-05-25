# ================================
# EJERCICIO 2
# Lista de Compras Interactiva
# ================================

lista_compras = []

while True:
    print("\n1. Agregar item a la lista")
    print("2. Eliminar item de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        producto = input("Ingrese el producto: ")
        lista_compras.append(producto)
        print("Producto agregado correctamente.")
    elif opcion == "2":
        producto = input("Ingrese el producto a eliminar: ")

        if producto in lista_compras:
            lista_compras.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("El producto no existe en la lista.")
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
        print("Opcion invalida.")
