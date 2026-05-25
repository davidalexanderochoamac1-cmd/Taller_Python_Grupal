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

print("-----📋Lista de calificaciones-----")
print("=" * 60)
print(notas)
print("=" * 60)

print("El Promedio grupal es :", round(resultado[0], 2))
print("-" * 60)
print("La Nota mas alta es :", resultado[1])
print("-" * 60)
print("La Nota mas baja es :", resultado[2])
