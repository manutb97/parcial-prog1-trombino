from typing import List


# Calcula el promedio general haciendo la suma de todoslos valores y diviendolos por el total
def promedio_general(promedios: List) -> float:
    """Devuelve el promedio general del curso luego de calcularlo"""
    suma_total = 0
    cantidad = len(promedios)

    for i in range(cantidad):
        suma_total = suma_total + promedios[i]

    return suma_total / cantidad


# Se encarga de recorrer las listas buscando el promedio mas alto y guardando el nombre que corresponde
def promedio_alumno_mayor(nombres: List, promedios: List):
    """Busca el promedio del alumno mas alto y su nombre"""

    mejor_promedio = promedios[0]
    mejor_nombre = nombres[0]

    for i in range(len(promedios)):
        if promedios[i] > mejor_promedio:
            mejor_promedio = promedios[i]
            mejor_nombre = nombres[i]

    return mejor_nombre, mejor_promedio


# Busca en las listas el promedio mas bajo y lo guarda en el respectivo nombre
def promedio_alumno_menor(nombres: List, promedios: List):
    """Busca el promedio del alumno mas bajo y su nombre"""

    menor_promedio = promedios[0]
    menor_nombre = nombres[0]

    for i in range(len(promedios)):
        if promedios[i] < menor_promedio:
            menor_promedio = promedios[i]
            menor_nombre = nombres[i]

    return menor_nombre, menor_promedio


# Lista a los alumnos segun la nota final de cada uno en promocion, parobados o desaprobados
def alumnos_por_promedio(promedios: List):
    """Realiza un recuento de cuantos alumnos, promocionan, aprueban o desaprueban"""

    alumnos_promocion = 0
    alumnos_aprobado = 0
    alumnos_desaprobado = 0

    for i in range(len(promedios)):
        if promedios[i] >= 6:
            alumnos_promocion = alumnos_promocion + 1
        elif promedios[i] >= 4:
            alumnos_aprobado = alumnos_aprobado + 1
        else:
            alumnos_desaprobado = alumnos_desaprobado + 1

    return alumnos_promocion, alumnos_aprobado, alumnos_desaprobado


# Metodo burbuja: ordena de mayor a menor y mueve en paralelo todas las listas vinculadas
def alumnos_ranking(nombres: List, promedios: List, notas_parcial_1: List, notas_parcial_2: List):
    """Organiza a los alumnos por ranking del mejor al peor promedio, aplicando metodo burbuja"""

    total_alumnos = len(promedios)

    for i in range(total_alumnos - 1):
        for j in range(total_alumnos - 1 - i):
            if promedios[j] < promedios[j + 1]:
                # Intercambiamos los promedios y tambien los datos en las listas paralelas
                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                notas_parcial_1[j], notas_parcial_1[j + 1] = notas_parcial_1[j + 1], notas_parcial_1[j]
                notas_parcial_2[j], notas_parcial_2[j + 1] = notas_parcial_2[j + 1], notas_parcial_2[j]


# Recorre cada letra del nombre para sumar la cantidad de vocales
def cantidad_vocales(nombre: str):
    """Cuenta la cantidad de vocales que tiene el nombre que se ingresa"""

    vocales = 0

    for letra in nombre:
        if letra in "aeiouAEIOU":
            vocales = vocales + 1

    return vocales


# Da vuelta el texto de nombre
def nombre_invertido(nombre: str):
    """Devuelve el nombre a la inversa de forma tradicional"""
    invertido = ""
    for i in range(len(nombre) - 1, -1, -1):
        invertido = invertido + nombre[i]
    return invertido


# Busca el alumno por coincidencia de nombre y devuelve la informacion en conjunto
def buscador_alumno(nombres: List, nombre_ingresado: str, promedios: List, notas_parcial_1: List, notas_parcial_2: List):
    """Busca a un alumno segun nombre ingresado y si lo encuentra, devuelve sus datos"""

    for i in range(len(nombres)):
        if nombres[i] == nombre_ingresado:
            return f"Alumno: {nombres[i]} | Promedio: {promedios[i]} | Parcial 1: {notas_parcial_1[i]} | Parcial 2: {notas_parcial_2[i]}"

    return "Se detecto un error, el alumno ingresado no existe"