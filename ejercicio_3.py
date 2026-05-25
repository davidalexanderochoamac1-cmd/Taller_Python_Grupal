# ================================
# EJERCICIO 3
# Agenda de Contactos
# ================================


def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el numero de telefono: ")
    agenda[nombre] = telefono
    print("Contacto agregado correctamente.")


def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre a buscar: ")

    if nombre in agenda:
        print("Telefono de", nombre + ":", agenda[nombre])
    else:
        print("El contacto no existe.")


def mostrar_contactos(agenda):
    print("\nLista de contactos:")

    if len(agenda) == 0:
        print("La agenda esta vacia.")
    else:
        for nombre, telefono in agenda.items():
            print(nombre, ":", telefono)


agenda = {}

while True:
    print("\n1. Anadir un nuevo contacto")
    print("2. Buscar el telefono de un contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        mostrar_contactos(agenda)
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opcion invalida.")
