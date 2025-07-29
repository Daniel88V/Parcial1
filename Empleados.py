empleados = {}
def agregar_empleados():
    print("Ingrese cuantos empleados desea agregar: ")
    cont = int(input())
    for i in range(cont):
        print(f"Empleado#{i+1}")
        codigo = input(f"Ingrese el codigo del empleado: ")
        if codigo in empleados:
            print("Error, este empleado ya fue registrado")
            return
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
        while True:
            try:
                productividad = int(input(f"Ingrese la calificacion de la productividad del empleado: "))
                if productividad < 0:
                    print("Error, la calificacion no puede ser negativa")
                    continue
                if productividad > 10:
                    print("Error, la calificacion maxima es 10")
                    continue
                break
            except ValueError:
                print("Error, por favor ingresa un valor valido")
        observacion_general = input(f"Ingrese la observacion general del empleado: ")
        telefono = input(f"Ingrese el telefono del empleado: ")
        correo = input(f"Ingrese el correo del empleado: ")
        empleados[codigo] = {
            "nombre": nombres,
            "apellido": apellidos,
            "departamento": departamento,
            "antiguedad": antiguedad,
            "desempeño": {
                "puntualidad": puntualidad,
                "trabajo_equipo": trabajo_equipo,
                "productividad": productividad,
            },
            "contacto": {
                "telefono": telefono,
                "correo": correo
            }
        }
def listado():
    print("------Listado de los empleados------")
    if empleados:
        for codigo, datos in empleados.items():
            print(f"Codigo: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Apellido: {datos['apellido']}")
            print(f"Departamento: {datos['departamento']}")
            print(f"Antiguedad: {datos['antiguedad']}")
            print(f"Punteo de puntualidad: {datos["desempeño"]['puntualidad']}")
            print(f"Punteo de trabajo en equipo: {datos["desempeño"]['trabajo_equipo']}")
            print(f"Punteo de productividad: {datos['desempeño']["productividad"]}")
            promedio = (datos['desempeño']['puntualidad'] + datos['desempeño']['trabajo_equipo'] + datos['desempeño']['productividad'])/3
            if promedio < 7:
               print("Desempeño: Mejorar")
            else:
                print("Desempeño: Satisfactorio")
    else:
        print("No hay empleados registrados")
def menu():
    print("======MENÚ PRINCIPAL======")
    print("1. Agregar empleado")
    print("2. Listado de empleados")
    print("3. Buscar empleado")
    print("4. Agregar observacion general")
    print("Seleccione una opcion: ")
    opcion = input()
    if opcion == "1":
        agregar_empleados()
    elif opcion == "2":
        listado()
if __name__ == "__main__":
    menu()