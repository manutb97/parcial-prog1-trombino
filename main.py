from procesamiento import *

nombres = []
promedios = []
notas_parcial_1 = []
notas_parcial_2 = []

opcion = ""

while opcion != "0":
    print("\n===== NOTAFÁCIL =====")
    print("1. Cargar alumnos")
    print("2. Mostrar listado")
    print("3. Mostrar estadísticas")
    print("4. Ver ranking (ordenado)")
    print("5. Buscar alumno")
    print("6. Juegos con un nombre")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\n[Carga de datos]")
            nombre = input("Ingrese el nombre del alumno: ")
            n1 = float(input("Ingrese nota del parcial 1: "))
            n2 = float(input("Ingrese nota del parcial 2: "))
            prom = (n1 + n2) / 2

            nombres.append(nombre)
            notas_parcial_1.append(n1)
            notas_parcial_2.append(n2)
            promedios.append(prom)
            print("¡El alumno se ingresó con éxito!")

        case "2":
            print("\n[Listado de alumnos]")
            if len(nombres) == 0:
                print("No se encuentran alumnos cargados en el sistema.")
            else:
                print(f"Cantidad total de alumnos: {len(nombres)}")
                for i in range(len(nombres)):
                    print(f"- {nombres[i]} | Parcial 1: {notas_parcial_1[i]} | Parcial 2: {notas_parcial_2[i]} | Promedio: {promedios[i]}")

        case "3":
            print("\n[Estadísticas del curso]")
            if len(nombres) == 0:
                print("No se encuentran alumnos cargados para mostrar estadísticas.")
            else:
                prom_gen = promedio_general(promedios)
                print(f"Promedio general del curso: {prom_gen:.2f}")
                
                mejor_nombre, mejor_prom = promedio_alumno_mayor(nombres, promedios)
                print(f"Alumno con mayor promedio: {mejor_nombre} ({mejor_prom})")
                
                menor_nombre, menor_prom = promedio_alumno_menor(nombres, promedios)
                print(f"Alumno con menor promedio: {menor_nombre} ({menor_prom})")
                
                promocionados, aprobados, desaprobados = alumnos_por_promedio(promedios)
                print(f"Alumnos promocionados: {promocionados}")
                print(f"Alumnos aprobados: {aprobados}")
                print(f"Alumnos desaprobados: {desaprobados}")

        case "4":
            print("\n[Ranking de alumnos (ordenado)]")
            if len(nombres) == 0:
                print("No se encuentran alumnos en sistema para el ranking.")
            else:
                alumnos_ranking(nombres, promedios, notas_parcial_1, notas_parcial_2)
                print("¡Ranking realizado con éxito!")
                for i in range(len(nombres)):
                    print(f"{i+1}. {nombres[i]} - Promedio: {promedios[i]}")

        case "5":
            print("\n[Búsqueda de alumno]")
            if len(nombres) == 0:
                print("No se encuentran alumnos cargados en el sistema.")
            else:
                nombre_buscado = input("Ingrese el nombre del alumno que desea buscar: ")
                resultado = buscador_alumno(nombres, nombre_buscado, promedios, notas_parcial_1, notas_parcial_2)
                print(resultado)

        case "6":
            print("\n[Juegos con un nombre]")
            nombre_ingresado = input("Ingrese un nombre para analizar: ")
            vocales = cantidad_vocales(nombre_ingresado)
            invertido = nombre_invertido(nombre_ingresado)
            print(f"Cantidad de vocales: {vocales}")
            print(f"Nombre invertido: {invertido}")

        case "0":
            print("\nSaliendo de NOTAFÁCIL. ¡Hasta luego!")

        case _:
            print("\nOpción no válida. Por favor, ingrese un número del 0 al 6.")