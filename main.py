
from menu import mostrar_menu
import datetime
from funciones_quiz import ejecutar_quiz_basico, ejecutar_quiz_medio, ejecutar_quiz_experto
import random
import numpy as np
import json
import os

def borrar_datos(nombre_archivo):
    try:
        os.remove(nombre_archivo)  # Eliminar el archivo
        print(f"Datos del usuario borrados exitosamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombre_archivo}. No hay datos para borrar.")
    except Exception as e:
        print(f"Error al borrar los datos: {e}")

def guardar_datos(nombre_usuario, puntajes, historial_quizzes):
    # Excluir la primera fila (encabezados) al guardar
    historial_a_guardar = historial_quizzes[1:].tolist() if historial_quizzes.shape[0] > 1 else []

    datos = {
        "nombre": nombre_usuario,
        "puntajes": puntajes,
        "historial": [
            [
                entry[0],
                entry[1].isoformat() if isinstance(entry[1], datetime.datetime) else entry[1],
                entry[2],
                entry[3],
                entry[4]
            ]
            for entry in historial_a_guardar
        ]
    }
    try:
        with open("datos_usuario.json", "w") as f:
            json.dump(datos, f, indent=4)
        print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
def cargar_datos():
    try:
        with open("datos_usuario.json", "r") as f:
            datos = json.load(f)
            nombre_usuario = datos.get("nombre", "Usuario")
            puntajes = datos.get("puntajes", [])
            historial_serializado = datos.get("historial", [])
            historial_quizzes = np.array([["Usuario", "Fecha/Hora", "Nivel", "Puntaje", "Total Preguntas"]]) # Inicializar con encabezados
            if historial_serializado:
                historial_data = [[entry[0], datetime.datetime.fromisoformat(entry[1]), entry[2], entry[3], entry[4]] for entry in historial_serializado]
                historial_quizzes = np.vstack((historial_quizzes, np.array(historial_data, dtype=object)))
            return nombre_usuario, puntajes, historial_quizzes
    except FileNotFoundError:
        return "Usuario", [], np.array([["Usuario", "Fecha/Hora", "Nivel", "Puntaje", "Total Preguntas"]])
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Se usarán datos predeterminados.")
        return "Usuario", [], np.array([["Usuario", "Fecha/Hora", "Nivel", "Puntaje", "Total Preguntas"]])
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return "Usuario", [], np.array([["Usuario", "Fecha/Hora", "Nivel", "Puntaje", "Total Preguntas"]])     
def main():

    nombre_Usuario, puntajes, historial_quizzes = cargar_datos()

    if nombre_Usuario == "Usuario":  # Verificar si es el nombre predeterminado
        nombre_Usuario = input("Bienvenido, ingrese su nombre de usuario: ")

    print(f"Bienvenido, {nombre_Usuario}!")
    num_quizzes = len(puntajes)  # Inicializar num_quizzes basado en los datos cargados
    preguntas_incorrectas = []

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione la opción deseada [1-8]: "))
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

            preguntas_incorrectas_nivel=[]

            if nivel == 1:
                print("Entraste al cuestionario básico de Python ¡Prepárate!")
                print("A continuación te realizaremos una serie de preguntas las cuales determinarán si tu nivel de Python es el que indicaste " \
                      "o si perteneces a un nivel más avanzado. Dichas preguntas te darán un puntaje y poco a poco irán aumentando su dificultad.")
                puntaje, preguntas_incorrectas_nivel = ejecutar_quiz_basico()
                puntajes.append(puntaje)
                num_quizzes+= 1

                total_preguntas_basico = len([
                    {"pregunta": "¿Cuál de los siguientes es una variable válida en Python?", "opciones": ["1.) 2usuario", "2.) usuario_principal", "3.) usuario-principal", "4.) usuario principal"], "respuesta_correcta": 2, "explicacion": "Una variable en Python debe comenzar con una letra o un guión bajo."}
                    # ... (Añade aquí todas las preguntas del nivel básico que tienes en funciones_quiz.py)
                ])
                historial_quizzes = np.append(historial_quizzes,
                                             [[nombre_Usuario, datetime.datetime.now(), "Básico", puntaje, total_preguntas_basico]],
                                             axis=0)
                preguntas_incorrectas.extend(preguntas_incorrectas_nivel)
                puntajes.append(puntaje)

            elif nivel == 2:
                print("Entraste al cuestionario medio de Python ¡Prepárate!")
                print("A continuación te realizaremos una serie de preguntas las cuales determinarán si tu nivel de Python es el que indicaste " \
                      "o si perteneces a un nivel más avanzado. Dichas preguntas te darán un puntaje y poco a poco irán aumentando su dificultad.")
                puntaje, preguntas_incorrectas_nivel = ejecutar_quiz_medio()
                puntajes.append(puntaje)
                num_quizzes+= 1

                total_preguntas_medio = len([
                    {"pregunta": "¿Qué ejecuta la siguiente función?\n"
                                "def saludo(nombre, mensaje='Hola'):\n"
                                "    print(f'{mensaje}, {nombre}')\n\n"
                                "Ejemplo: saludo('Ana')", "opciones": ["1.) Hola Ana", "2.) mensaje, Ana", "3.) Ana, Hola", "4.) Error de compilación"], "respuesta_correcta": 1, "explicacion": "La función utiliza un argumento por defecto para 'mensaje', así que imprimirá 'Hola, Ana'."}
                    # ... (Añade aquí todas las preguntas del nivel medio)
                ])
                historial_quizzes = np.append(historial_quizzes,
                                             [[nombre_Usuario, datetime.datetime.now(), "Medio", puntaje, total_preguntas_medio]],
                                             axis=0)
                preguntas_incorrectas.extend(preguntas_incorrectas_nivel)
                puntajes.append(puntaje)

            elif nivel == 3:
                print("Entraste al cuestionario experto de Python ¡Prepárate!")
                print("A continuación te realizaremos una serie de preguntas las cuales determinarán si tu nivel de Python es el que indicaste " \
                      "o si perteneces a un nivel más avanzado. Dichas preguntas te darán un puntaje y poco a poco irán aumentando su dificultad.")
                puntaje, preguntas_incorrectas_nivel = ejecutar_quiz_experto()
                puntajes.append(puntaje)
                num_quizzes+= 1

                total_preguntas_experto = len([
                    {"pregunta": "¿Qué hace el siguiente código con decoradores?\n\n"
                                "def decorador(func):\n"
                                "    def envoltura():\n"
                                "        print('Antes de ejecutar la función')\n"
                                "        func()\n"
                                "        print('Después de ejecutar la función')\n"
                                "    return envoltura\n\n"
                                "@decorador\n"
                                "def saludar():\n"
                                "    print('Hola mundo')\n\n"
                                "saludar()", "opciones": ["1.) Llama a saludar sin decorarla", "2.) Ejecuta saludar() antes de decorador()", "3.) Imprime mensajes antes y después de saludar()", "4.) Solo imprime Hola mundo"], "respuesta_correcta": 3, "explicacion": "El decorador 'decorador' modifica el comportamiento de 'saludar' para imprimir mensajes antes y después de su ejecución."}
                    # ... (Añade aquí todas las preguntas del nivel experto)
                ])
                historial_quizzes = np.append(historial_quizzes,
                                             [[nombre_Usuario, datetime.datetime.now(), "Experto", puntaje, total_preguntas_experto]],
                                             axis=0)
                preguntas_incorrectas.extend(preguntas_incorrectas_nivel)
                puntajes.append(puntaje)

            else:
                print("Nivel no válido.")
        
        elif opcion == 2:
            print(f"Mostrando estadísticas de jugador {nombre_Usuario}")
            if num_quizzes >0:
                puntaje_total = sum(puntajes)  # Se calcula el puntaje promedio
                print(f"Número de quizzes completados: {num_quizzes}")
                print(f"Puntaje promedio: {puntaje_total}")
            else:
                print("Aún no has completado ningún quiz")
            # Aquí puedes poner la función que muestre estadísticas si la agregas

        elif opcion == 3:
            print(f"Mostrando historial del jugador {nombre_Usuario}")
            # Aquí puedes poner la función que muestre historial si la agregas
            if historial_quizzes.shape[0] > 1:  # Verificar si hay más de la fila de encabezado
                for registro in historial_quizzes[1:]:  # Iterar desde la segunda fila
                    print(f"Nivel: {registro[2]}, Puntaje: {registro[3]}/{registro[4]}, Fecha: {registro[1]}")
            else:
                print("No hay historial de quizzes para mostrar.")

        elif opcion == 4:
            nombre_Usuario = input("Ingrese el nuevo nombre de usuario: ")
            print(f"Nombre cambiado a {nombre_Usuario}")

        elif opcion == 5:
            print(f"Iniciando práctica personalizada para {nombre_Usuario}")
            print("Seleccione el nivel de dificultad:")
            print("1. Nivel Básico de Python")
            print("2. Nivel Medio de Python")
            print("3. Nivel Experto de Python")
            try:
                nivel = int(input("Seleccione un nivel: "))
                num_preguntas = int(input("Ingrese el número de preguntas para la práctica: "))
            except ValueError:
                print("Por favor, ingrese números válidos.")
                continue

            if nivel == 1:
                ejecutar_quiz_basico(num_preguntas=num_preguntas)  # Llamada a la función con el número de preguntas
            elif nivel == 2:
                ejecutar_quiz_medio(num_preguntas=num_preguntas)
            elif nivel == 3:
                ejecutar_quiz_experto(num_preguntas=num_preguntas)
            else:
                print("Nivel no válido.")

        elif opcion == 6:
            print("Repitiendo preguntas incorrectas...")
            if not preguntas_incorrectas:
                print("No respondiste ninguna pregunta incorrectamente.")
            else:
                if nivel==1:
                    ejecutar_quiz_basico(preguntas_incorrectas=preguntas_incorrectas)
                elif nivel==2:
                    ejecutar_quiz_medio(preguntas_incorrectas=preguntas_incorrectas)
                elif nivel==3:
                    ejecutar_quiz_experto(preguntas_incorrectas=preguntas_incorrectas)    
        elif opcion==7:
            print("Saliendo del programa, guardando datos...")
            guardar_datos(nombre_Usuario, puntajes, historial_quizzes)  # Pasar los tres argumentos
            print("¡Adiós!")
            break
        elif opcion == 8:  # Nueva opción para borrar datos
            print("¿Estás seguro de que deseas borrar todos los datos? (si/no): ")
            confirmacion = input().lower()
            if confirmacion == "si":
                borrar_datos("datos_usuario.json")
                # Opcional: Reiniciar las variables en memoria
                nombre_Usuario = ""
                puntajes = []
                num_quizzes = 0
                historial_quizzes = np.array([["Usuario", "Fecha/Hora", "Nivel", "Puntaje", "Total Preguntas"]])
                preguntas_incorrectas = []
            else:
                print("Operación cancelada. Los datos no han sido borrados.")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
