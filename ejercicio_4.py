# ================================
# EJERCICIO 4
# Conversor de Unidades
# ================================

# Diccionario con los factores de conversion entre unidades.
conversiones = {
    "metros": {
        "pies": 3.28
    },
    "kilometros": {
        "millas": 0.62
    },
    "kilogramos": {
        "libras": 2.20
    }
}


def mostrar_conversiones_disponibles():
    # Informa las unidades disponibles para convertir.
    print("Unidades disponibles: metros, pies, kilometros, millas, kilogramos y libras.")


def convertir(cantidad, origen, destino):
    # Verifica primero si la unidad de origen existe.
    if origen in conversiones:
        # Luego valida si la unidad de destino esta definida para ese origen.
        if destino in conversiones[origen]:
            return cantidad * conversiones[origen][destino]
        return "La unidad de destino no existe en el diccionario."
    return "La unidad de origen no existe en el diccionario."


# Muestra las opciones y solicita los datos al usuario.
mostrar_conversiones_disponibles()
print("")
cantidad = float(input("Ingrese la cantidad: "))
origen = input("Ingrese la unidad de origen: ").lower()
destino = input("Ingrese la unidad de destino: ").lower()

# Ejecuta la conversion con los valores ingresados.
resultado = convertir(cantidad, origen, destino)

print("Resultado:", resultado)
