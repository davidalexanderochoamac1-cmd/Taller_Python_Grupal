# ================================
# EJERCICIO 3
# Agenda de Contactos
# ================================


def agregar_contacto(agenda):
    # Pide los datos del contacto y los guarda en la agenda.
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el numero de telefono: ")
    agenda[nombre] = telefono
    print("Contacto agregado correctamente.")


def buscar_contacto(agenda):
    # Solicita un nombre y revisa si existe en el diccionario.
    nombre = input("Ingrese el nombre a buscar: ")

    if nombre in agenda:
        print("\n","El número de telefono de", nombre + ":", agenda[nombre])
    else:
        print("\n","El contacto no existe.")


def mostrar_contactos(agenda):
    # Recorre la agenda completa para mostrar cada registro.
    print("\nLista de contactos:")

    if len(agenda) == 0:
        print("\n","La agenda esta vacia.")
    else:
        for nombre, telefono in agenda.items():
            print(nombre, "|", telefono)

# Diccionario principal donde se almacenan los contactos.
agenda = {}

# Mantiene el menu activo hasta que el usuario elija salir.
while True:
    print("\nAGENDA DE CONTACTOS")
    print("1. Anadir un nuevo contacto")
    print("2. Buscar el telefono de un contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    opcion = input("\n","Seleccione una opcion: ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        mostrar_contactos(agenda)
    elif opcion == "4":
        # Cierra el programa.
        print("\n","Programa finalizado.")
        break
    else:
        print("\n","Opcion invalida.")
