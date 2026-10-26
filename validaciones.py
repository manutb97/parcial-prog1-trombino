def validar_cantidad_alumnos() -> int:
    """Pide la cantidad de alumnos y valida que el valor este entre 1 y 30"""
    print("Ingrese la cantidad total de alumnos")
    alumnos = int(input())

    while alumnos < 1 or alumnos > 30:
        print("Error en la carga. La cantidad de alumnos ingresada debe estar entre 1 y 30")
        alumnos = int(input("Por favor, ingrese una cantidad de alumnos valida: "))

    return alumnos


def validar_nota(numero_parcial: int) -> int:
    """Pide el tipo de parcial y valida que el valor este entre 1 y 10"""
    nota = int(input(f"Ingrese la nota del parcial {numero_parcial}: "))

    while nota < 0 or nota > 10:
        print("Error en la carga. La nota ingresada debe ser del 0 al 10")
        nota = int(input(f"Ingrese una nota valida para el parcial {numero_parcial}: "))

    return nota


def validar_nombre() -> str:
    """Pide nombre de alumno, valida que tenga 5 caracteres y contenga unicamente letras y espacios"""

    nombre_aprobado = False

    while not nombre_aprobado:
        nombre = input("Ingrese un nombre: ")

        if len(nombre) < 5:
            print("Se detecto un error. El nombre ingresado debe tener al menos 5 letras")
            continue

        letras_ingresadas_correctas = True

        for caracter in nombre:
            if not (("a" <= caracter <= "z") or ("A" <= caracter <= "Z") or (caracter == " ")):
                letras_ingresadas_correctas = False
                break

        if not letras_ingresadas_correctas:
            print("Se detecto un error. El nombre solo puede contener letras y espacios, sin numeros o simbolos")
        else:
            nombre_aprobado = True

    return nombre