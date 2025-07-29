empleados = {}
def agregar_empleados():
    print("Ingrese cuantos empleados desea agregar: ")
    cont = int(input())
    for i in range(cont):
        print(f"Empleado#{i+1}")
        codigo = input(f"Ingrese el codigo del empleado: ")
        if codigo in empleados:
            print("Error, este empleado ya fue registrado")
            break
        nombres= input(f"Ingrese el nombre del empleado(si el empleado posee dos nombres ingrese ambos): ")
        apellidos = input(f"Ingrese los apellidos del empleado: ")
        departamento = input(f"Ingrese el departamento del empleado: ")
        while True:
            try:
                antiguedad = int(input(f"Ingrese los años que el empleado lleva trabajando en la empresa: "))
                if antiguedad < 0:
                    print("Error, los años no pueden ser negativos")
                    continue
                break
            except ValueError:
                print("Error, por favor ingresa un valor valido")
        while True:
            try:
                puntualidad = int(input(f"Ingrese la calificacion en la puntualidad del empleado: "))
                if puntualidad < 0:
                    print("Error, la calificacion no puede ser negativa")
                    continue
                if puntualidad > 10:
                    print("Error, la calificacion maxima es 10")
                    continue
                break
            except ValueError:
                print("Error, por favor ingresa un valor valido")
        while True:
            try:
                trabajo_equipo = int(input(f"Ingrese la calificacion de trabajo equipo del empleado: "))
                if trabajo_equipo < 0:
                    print("Error, la calificacion no puede ser negativa")
                    continue
                if trabajo_equipo > 10:
                    print("Error, la calificacion maxima es 10")
                    continue
                break
            except ValueError:
                print("Error, por favor ingresa un valor valido")