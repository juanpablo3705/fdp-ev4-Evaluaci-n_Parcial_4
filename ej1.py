# funcion mostrar menú:
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

# funcion leer opcion:
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            if (opcion >= 1) and (opcion <= 6):
                return opcion
            else:
                print("Error, debe ingresar una opción del 1 al 6.")
        except ValueError:
            print("Error, debe ingresar sólo números del 1 al 6, no letras.")

# funcion validar nombre:
def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    else:
        return True
    
# funcion validar edad:
def validar_edad(edad):
    if edad > 0:
        return True
    else:
        return False
    
# funcion validar nota:
def validar_nota(nota):
    if (nota >= 1) and (nota <= 7):
        return True
    else:
        return False
    
# funcion 1 agregar estudiante:
def agregar_estudiante(coleccion):
    while True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if validar_nombre(nombre):
            break
        else:
            print("Error, el nombre no puede estar vacío ni ser sólo espacios en blanco.")
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if validar_edad(edad):
                break
            else:
                print("Error, la edad debe ser un número entero mayor que cero.")
        except ValueError:
            print("Error, la edad debe ser un número entero mayor que cero, no letras.")
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante: "))
            if validar_nota(nota):
                break
            else:
                print("Error, la nota debe ser un número decimal entre 1.0 y 7.0.")
        except ValueError:
            print("Error, la nota debe ser un número decimal entre 1.0 y 7.0, no letras.")
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "aprobado": False
    }
    coleccion.append(estudiante)
    print(f"Estudiante {nombre} agregado con éxito.")

# funcion 2 buscar indice:
def buscar_indice(coleccion, nombre):
    for indice in range(len(coleccion)):
        if coleccion[indice]["nombre"] == nombre:
            return indice
    return -1

# funcion 4 actualizar estados:
def actualizar_estados(coleccion):
    for estudiante in coleccion:
        if estudiante["nota"] >= 4:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False

# programa principal:
coleccion = []
while True:
    mostrar_menu()
    opcion_elegida = leer_opcion()
    match opcion_elegida:
        case 1:
            agregar_estudiante(coleccion)
        case 2:
            if len(coleccion) == 0:
                print("Error, no hay estudiantes ingresados.")
            else:
                nombre = input("Ingrese el nombre del estudiante a buscar: ")
                posicion = buscar_indice(coleccion, nombre)
                if posicion == -1:
                    print(f"Error, estudiante {nombre} no encontrado.")
                else:
                    print("¡Estudiante encontrado!")
                    print(f"Nombre: {nombre}.")
                    print(f"Edad: {coleccion[posicion]['edad']}.")
                    print(f"Nota: {coleccion[posicion]['nota']}")
        case 3:
            if len(coleccion) == 0:
                print("Error, no hay estudiantes ingresados.")
            else:
                nombre = input("Ingrese el nombre del estudiante a eliminar de la lista: ")
                posicion = buscar_indice(coleccion, nombre)
                if posicion == -1:
                    print(f"Error, estudiante {nombre} no encontrado.")
                else:
                    del(coleccion[posicion])
                    print(f"Estudiante {nombre} eliminado de la lista con éxito.")
        case 4:
            if len(coleccion) == 0:
                print("Error, no hay estudiantes ingresados.")
            else:
                actualizar_estados(coleccion)
                print("Estados de aprobación de los estudiantes actualizados con éxito.")
        case 5:
            if len(coleccion) == 0:
                print("Error, no hay estudiantes ingresados.")
            else:
                actualizar_estados(coleccion)
                print("=== LISTA DE ESTUDIANTES ===")
                for estudiante in coleccion:
                    if estudiante["aprobado"]:
                        estado = "APROBADO"
                    else:
                        estado = "REPROBADO"
                    print(f"Nombre: {estudiante['nombre']}.")
                    print(f"Edad: {estudiante['edad']}.")
                    print(f"Nota: {estudiante['nota']}.")
                    print(f"Estado: {estado}.")
                    print("********************************************")
        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto.")
            break