from funciones import(registrar_taller,
                      listar_taller,
                      buscar_taller,
                      actuaizar_taller,
                      eliminar_taller
                      )

talleres = []
opcion = 0


while opcion != 6:

    print("=== SISTEMA DE TALLERES ACADÉMICOS DUOC ===")
    print("1. Registrar taller")
    print("2. Listar talleres")
    print("3. Buscar taller")
    print("4. Actualizar taller")
    print("5. Eliminar taller")
    print("6. Salir")

    try:
        opcion = int(input("Ingrese una opcion: "))
    except:
        print("La opcion debe de ser numerica")
        continue

    if opcion == 1:
        registrar_taller(talleres)
    elif opcion == 2:
       listar_taller(talleres)
    elif opcion == 3:
        buscar_taller(talleres)
    elif opcion == 4:
        actuaizar_taller(talleres)
    elif opcion == 5:
        eliminar_taller(talleres)
    elif opcion == 6:
        print("Gracias por usar el sistema")