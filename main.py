from menu import mostrar_menu
from funciones_quiz import ejecutar_quiz_basico, ejecutar_quiz_medio, ejecutar_quiz_experto

def main():

    nombre_Usuario = input("Bienvenido, ingrese su nombre de usuario: ")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione la opción deseada [1-5]: "))
        except ValueError:
            print("Por favor, ingrese un número del 1 al 5")
            continue

        if opcion == 1:
            print(f"Inicializando quiz para {nombre_Usuario}")
            print("Bienvenido al curso express de aprendizaje Python")
            print("Selecciona el nivel que deseas aprender")
            print("1. Nivel Básico de Python")
            print("2. Nivel Medio de Python")
            print("3. Nivel Experto de Python")
            try:
                nivel = int(input("Selecciona un nivel: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if nivel == 1:
                print("Entraste al cuestionario básico de Python ¡Prepárate!")
                print("A continuación te realizaremos una serie de preguntas las cuales determinarán si tu nivel de Python es el que indicaste " \
                      "o si perteneces a un nivel más avanzado. Dichas preguntas te darán un puntaje y poco a poco irán aumentando su dificultad.")
                ejecutar_quiz_basico()

            elif nivel == 2:
                print("Entraste al cuestionario medio de Python ¡Prepárate!")
                print("A continuación te realizaremos una serie de preguntas las cuales determinarán si tu nivel de Python es el que indicaste " \
                      "o si perteneces a un nivel más avanzado. Dichas preguntas te darán un puntaje y poco a poco irán aumentando su dificultad.")
                ejecutar_quiz_medio()

            elif nivel == 3:
                print("Entraste al cuestionario experto de Python ¡Prepárate!")
                print("A continuación te realizaremos una serie de preguntas las cuales determinarán si tu nivel de Python es el que indicaste " \
                      "o si perteneces a un nivel más avanzado. Dichas preguntas te darán un puntaje y poco a poco irán aumentando su dificultad.")
                ejecutar_quiz_experto()
            else:
                print("Nivel no válido.")
        
        elif opcion == 2:
            print(f"Mostrando estadísticas de jugador {nombre_Usuario}")
            # Aquí puedes poner la función que muestre estadísticas si la agregas

        elif opcion == 3:
            print(f"Mostrando historial del jugador {nombre_Usuario}")
            # Aquí puedes poner la función que muestre historial si la agregas

        elif opcion == 4:
            nombre_Usuario = input("Ingrese el nuevo nombre de usuario: ")
            print(f"Nombre cambiado a {nombre_Usuario}")

        elif opcion == 5:
            print("Saliendo del programa, Adiós")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
