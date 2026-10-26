from procesamiento import *
from validaciones import validar_nombre, validar_nota

nombres = []
promedios = []
notas_parcial_1 = []
notas_parcial_2 = []
cantidad = 0

opcion = ""

while opcion != "0":
    print("\n===== NOTAFACIL =====")
    print("1. Cargar alumnos")
    print("2. Mostrar listado")
    print("3. Mostrar estadisticas")
    print("4. Ver ranking (ordenado)")
    print("5. Buscar alumno")
    print("6. Juegos con un nombre")
    print("0. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("\n[Carga de datos]")
        nombre = validar_nombre()  # Usa tu función que valida letras y espacios
        n1 = validar_nota(1)       # Valida que la nota 1 esté entre 0 y 10
        n2 = validar_nota(2)       # Valida que la nota 2 esté entre 0 y 10
        prom = (n1 + n2) / 2

        nombres = nombres + [nombre]
        notas_parcial_1 = notas_parcial_1 + [n1]
        notas_parcial_2 = notas_parcial_2 + [n2]
        promedios = promedios + [prom]
        
        cantidad = cantidad + 1
        print("El alumno se ingreso con exito!")

    elif opcion == "2":
        print("\n[Listado de alumnos]")
        if cantidad == 0:
            print("No se encuentran alumnos cargados en el sistema.")
        else:
            print(f"Cantidad total de alumnos: {cantidad}")

            for i in range(cantidad):
                print(f"- {nombres[i]} | Parcial 1: {notas_parcial_1[i]} | Parcial 2: {notas_parcial_2[i]} | Promedio: {promedios[i]}")

    elif opcion == "3":
        print("\n[Estadísticas del curso]")
        if cantidad == 0:
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

    elif opcion == "4":
        print("\n[Ranking de alumnos (ordenado)]")
        if cantidad == 0:
            print("No se encuentran alumnos en sistema para el ranking.")
        else:
            alumnos_ranking(nombres, promedios, notas_parcial_1, notas_parcial_2)
            print("¡Ranking realizado con exito!")
            for i in range(cantidad):
                print(f"{i+1}. {nombres[i]} - Promedio: {promedios[i]}")

    elif opcion == "5":
        print("\n[Búsqueda de alumno]")
        if cantidad == 0:
            print("No se encuentran alumnos cargados en el sistema.")
        else:
            nombre_buscado = input("Ingrese el nombre del alumno que desea buscar: ")
            resultado = buscador_alumno(nombres, nombre_buscado, promedios, notas_parcial_1, notas_parcial_2)
            print(resultado)

    elif opcion == "6":
        print("\n[Juegos con un nombre]")
        nombre_ingresado = input("Ingrese un nombre para analizar: ")
        vocales = cantidad_vocales(nombre_ingresado)
        invertido = nombre_invertido(nombre_ingresado)
        print(f"Cantidad de vocales: {vocales}")
        print(f"Nombre invertido: {invertido}")

    elif opcion == "0":
        print("\nSaliendo de NOTAFACIL. Hasta luego!")

    else:
        print("\nOpcion no valida. Por favor, ingrese un numero del 0 al 6.")