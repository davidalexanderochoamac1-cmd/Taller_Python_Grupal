# ================================
# EJERCICIO 1
# Analisis de Calificaciones
# ================================


def analizar_calificaciones(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    nota_alta = max(calificaciones)
    nota_baja = min(calificaciones)
    return promedio, nota_alta, nota_baja


notas = [4.5, 3.8, 5.0, 2.9, 4.2]
resultado = analizar_calificaciones(notas)

print("Promedio:", round(resultado[0], 2))
print("Nota mas alta:", resultado[1])
print("Nota mas baja:", resultado[2])
