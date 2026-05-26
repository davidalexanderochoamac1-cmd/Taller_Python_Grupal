# ================================
# EJERCICIO 1
# Analisis de Calificaciones
# ================================


def analizar_calificaciones(calificaciones):
    # Calcula el promedio de todas las notas ingresadas.
    promedio = sum(calificaciones) / len(calificaciones)
    # Identifica la nota mas alta del grupo.
    nota_alta = max(calificaciones)
    # Identifica la nota mas baja del grupo.
    nota_baja = min(calificaciones)
    return promedio, nota_alta, nota_baja


# Lista de calificaciones que se analizara.
notas = [4.5, 3.8, 5.0, 2.9, 4.2]
# Guarda el promedio, la nota mayor y la nota menor.
resultado = analizar_calificaciones(notas)

# Muestra la lista completa y el resumen del analisis.
print("📋 ----- Lista de calificaciones -----")
print("=" * 60)
print(notas)
print("=" * 60)

print("📊 El promedio grupal es:", round(resultado[0], 2))
print("-" * 60)
print("🏆 La nota mas alta es:", resultado[1])
print("-" * 60)
print("📉 La nota mas baja es:", resultado[2])
