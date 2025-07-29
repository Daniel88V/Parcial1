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