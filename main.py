def mostrar_menu():

    print("Menú Principal")
    print("1. Iniciar Quiz")
    print("2. Ves estadisticas")
    print("3. Ver historial")
    print("4. Cambiar nombre")
    print("5. Salir")

def main():
    nombre_Usuario=input("Bienvenido Ingrese su nombre de usuario ")

    while True:
        mostrar_menu()
        opcion=int(input("Seleccione la opción deseada [1-5]"))

        if opcion==1:
                print(f"Inicializando quiz para {nombre_Usuario}")
                print("Bienvenido al curso express de aprendizaje python")
                print("Selecciona el nivel que deseas aprender")
                print("1. Nivel Básico de pyhton")
                print("2. Nivel medio de pyhton")
                print("3. Nivel experto de pyhton")
                opcion=int(input("Selecciona una opcion"))

                if opcion==1:
                       print("Entraste al cuestionario basico de python ¡Preparate!")
                       print("A continuación te realizaremos una serie de preguntas las cuales determinaran si tu nivel de python es el que indicaste " \
                       "o si perteneces a un nivel mas avanzado, dichas preguntas te daran un puntaje y poco a poco iran aumentando su dificultad.")
               
               
               
                elif opcion==2:
                       print("Entraste al cuestionario medio de python ¡Preparate!")
                elif opcion==3:
                       print("Entraste al cuestionario experto de python ¡Preparate!")
                #Inicializar el Quiz
                #funciones para gestionar las preguntas
        elif opcion==2:
                print(f"Mostrando estadisticas de jugador {nombre_Usuario}")
                #Mostrar estadisticas en pantalla
                #
        elif opcion==3:
                print(f"Mostrando estadisticas del jugador {nombre_Usuario}")
                #Mostrar historial del jugador
        elif opcion==4:
                print(f"Cambiando nombre del usuario a {nombre_Usuario}")
                #Cambiar el nombre de usuario 
        elif opcion==5:
                print("Saliendo del programa, Adiós")
                break
        else:
                print("Opción no válida")

main()
            

