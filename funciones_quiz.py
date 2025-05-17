def ejecutar_quiz_basico():
    puntaje = 0

    print("¿Cuál de los siguientes es una variable válida en Python?")
    print("1.) 2usuario")
    print("2.) usuario_principal")
    print("3.) usuario-principal")
    print("4.) usuario principal")

    try:
        respuesta = int(input("Ingresa la opción correcta (1-4): "))
        if respuesta == 2:
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print("Respuesta incorrecta.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

    print(f"Tu puntaje es {puntaje}")
def ejecutar_quiz_medio():
    puntaje = 0

    print("¿Qué ejecuta la siguiente función?")
    print("def saludo(nombre, mensaje='Hola'):")
    print("    print(f'{mensaje}, {nombre}')")
    print("\nEjemplo: saludo('Ana')")

    print("1.) Hola Ana")
    print("2.) mensaje, Ana")
    print("3.) Ana, Hola")
    print("4.) Error de compilación")

    try:
        respuesta = int(input("Ingresa la opción correcta (1-4): "))
        if respuesta == 1:
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print("Respuesta incorrecta.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
def ejecutar_quiz_experto():
    puntaje = 0

    print("¿Qué hace el siguiente código con decoradores?")
    print("def decorador(func):")
    print("    def envoltura():")
    print("        print('Antes de ejecutar la función')")
    print("        func()")
    print("        print('Después de ejecutar la función')")
    print("    return envoltura")
    print("")
    print("@decorador")
    print("def saludar():")
    print("    print('Hola mundo')")
    print("")
    print("saludar()")

    print("\nOpciones:")
    print("1.) Llama a saludar sin decorarla")
    print("2.) Ejecuta saludar() antes de decorador()")
    print("3.) Imprime mensajes antes y después de saludar()")
    print("4.) Solo imprime Hola mundo")

    try:
        respuesta = int(input("Ingresa la opción correcta (1-4): "))
        if respuesta == 3:
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print("Respuesta incorrecta.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
