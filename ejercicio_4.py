# ================================
# EJERCICIO 4
# Conversor de Unidades
# ================================

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
    print("📏 Unidades disponibles: metros, pies, kilometros, millas, kilogramos y libras.")


def convertir(cantidad, origen, destino):
    if origen in conversiones:
        if destino in conversiones[origen]:
            return cantidad * conversiones[origen][destino]
        return "La unidad de destino no existe en el diccionario."
    return "La unidad de origen no existe en el diccionario."


mostrar_conversiones_disponibles()
print("")
cantidad = float(input("🔢 Ingrese la cantidad: "))
origen = input("📍 Ingrese la unidad de origen: ").lower()
destino = input("🎯 Ingrese la unidad de destino: ").lower()

resultado = convertir(cantidad, origen, destino)

print("✅ Resultado:", resultado)
