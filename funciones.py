def registrar_taller(talleres):
    print("---registro de taller---")
    try:
        codigo = int(input("Ingrese el codigo del taller: "))
        if codigo == " ":
            print("El código del taller no puede estar vacío.")
        elif codigo in talleres:
    except:
        ("Tiene que ingresar un numero entero") 
    nombre = input("Ingrese el nombre del taller: ")
    docente = input("Ingrese el nombre del docente responsable: ")
    try:
        cupo_m = int(input("Ingrese el cupo maximo de estudiantes: "))
        if cupo_m <= 0:
            print("El numero debe de ser un entero positivo")
        else:
            print("cupo registrado correctamente")
    except:
        print("Tiene que ingresar un numero entero positivo")

    taller = {"codigo_t":"codigo",
              "nombre_t":"nombre",
              "docente_t":"docente",
              "cupo":"cupo_m"}
    talleres.append(taller)

def listar_taller(talleres):
    print("...")

def buscar_taller(talleres):
    print("...")

def actuaizar_taller(talleres):
    print("...")

def eliminar_taller(talleres):
    print("...")