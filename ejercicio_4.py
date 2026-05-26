# ================================
# EJERCICIO 4
# Conversor de Unidades
# ================================

# Diccionario con factores de conversion en ambos sentidos.
conversiones = {
    "metros": {
        "pies": 3.28
    },
    "pies": {
        "metros": 1 / 3.28
    },
    "kilogramos": {
        "libras": 2.20
    },
    "libras": {
        "kilogramos": 1 / 2.20
    }
}


def convertir(cantidad, origen, destino):
    # Verifica si la unidad de origen existe en el diccionario.
    if origen in conversiones:
        # Verifica si la unidad de destino existe dentro de esa unidad de origen.
        if destino in conversiones[origen]:
            return cantidad * conversiones[origen][destino]
        return "La unidad de destino no existe en el diccionario."
    return "La unidad de origen no existe en el diccionario."


# Repite el menu hasta que el usuario decida salir.
while True:
    print("\n📏 CONVERSOR DE UNIDADES")
    print("1. 📐 Metros a pies")
    print("2. 📏 Pies a metros")
    print("3. ⚖️ Kilogramos a libras")
    print("4. 🏋️ Libras a kilogramos")
    print("5. 🚪 Salir")

    opcion = input("👉 Seleccione una opcion: ")

    if opcion == "1":
        origen = "metros"
        destino = "pies"
    elif opcion == "2":
        origen = "pies"
        destino = "metros"
    elif opcion == "3":
        origen = "kilogramos"
        destino = "libras"
    elif opcion == "4":
        origen = "libras"
        destino = "kilogramos"
    elif opcion == "5":
        print("👋 Programa finalizado.")
        break
    else:
        print("⚠️ Opcion invalida.")
        continue

    # Solicita la cantidad, realiza la conversion y muestra el resultado.
    cantidad = float(input(f"🔢 Ingrese la cantidad en {origen}: "))
    resultado = convertir(cantidad, origen, destino)
    print(f"✅ Resultado: {round(resultado, 2)} {destino}")
