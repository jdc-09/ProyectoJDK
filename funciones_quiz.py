import time
import random

def obtener_respuesta_valida():
    while True:
        try:
            respuesta = int(input("Ingresa la opción correcta (1-4): "))
            if 1 <= respuesta <= 4:
                return respuesta
            else:
                print("Opción no válida. Por favor, ingresa un número del 1 al 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def ejecutar_quiz_basico(num_preguntas=None, preguntas_incorrectas=None):
    puntaje = 0
    tiempo_inicio = time.time()
    tiempo_limite = 10 * (num_preguntas if num_preguntas is not None else 1)

    preguntas_nivel = [
        {
            "pregunta": "¿Cuál de los siguientes es una variable válida en Python?",
            "opciones": ["1.) 2usuario", "2.) usuario_principal", "3.) usuario-principal", "4.) usuario principal"],
            "respuesta_correcta": 2,
            "explicacion": "Una variable en Python debe comenzar con una letra o un guión bajo."
        }
        # ... (Más preguntas básicas)
    ]

    preguntas_seleccionadas = []
    if preguntas_incorrectas is None:
        if num_preguntas is None:
            preguntas_seleccionadas = preguntas_nivel
            tiempo_limite = 10 * len(preguntas_seleccionadas)
        else:
            preguntas_seleccionadas = random.sample(preguntas_nivel, min(num_preguntas, len(preguntas_nivel)))
            tiempo_limite = 10 * num_preguntas
    else:
        preguntas_seleccionadas = [preguntas_nivel[i] for i in preguntas_incorrectas if i < len(preguntas_nivel)]
        tiempo_limite = 10 * len(preguntas_seleccionadas)

    preguntas_incorrectas_al_nivel = []

    for i, pregunta in enumerate(preguntas_seleccionadas):
        print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)

        tiempo_transcurrido_inicio_pregunta = time.time() - tiempo_inicio
        if tiempo_transcurrido_inicio_pregunta >= tiempo_limite:
            print("¡Se acabó el tiempo!")
            break  # Salir del bucle de preguntas inmediatamente

        respuesta_usuario = obtener_respuesta_valida()

        tiempo_transcurrido_fin_respuesta = time.time() - tiempo_inicio
        if tiempo_transcurrido_fin_respuesta >= tiempo_limite:
            print("¡Se acabó el tiempo!")
            break  # Salir del bucle de preguntas inmediatamente después de que se intente obtener la respuesta

        if respuesta_usuario == pregunta['respuesta_correcta']:
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era la opción {pregunta['respuesta_correcta']}.")
            if preguntas_incorrectas is None:
                preguntas_incorrectas_al_nivel.append(preguntas_nivel.index(pregunta))
            print(pregunta.get('explicacion', 'No hay explicación disponible.'))

    print(f"\nQuiz completado. Tu puntaje es: {puntaje}/{len(preguntas_seleccionadas)}")
    return puntaje, preguntas_incorrectas_al_nivel


def ejecutar_quiz_medio(num_preguntas=None, preguntas_incorrectas=None):
    puntaje = 0
    tiempo_inicio = time.time()
    tiempo_limite = 15 * (num_preguntas if num_preguntas is not None else 1) # Aumentar tiempo límite

    preguntas_nivel = [
        {
            "pregunta": "¿Qué ejecuta la siguiente función?\n"
                        "def saludo(nombre, mensaje='Hola'):\n"
                        "    print(f'{mensaje}, {nombre}')\n\n"
                        "Ejemplo: saludo('Ana')",
            "opciones": ["1.) Hola Ana", "2.) mensaje, Ana", "3.) Ana, Hola", "4.) Error de compilación"],
            "respuesta_correcta": 1,
            "explicacion": "La función utiliza un argumento por defecto para 'mensaje', así que imprimirá 'Hola, Ana'."
        },
        # ... (Más preguntas medias)
    ]

    preguntas_seleccionadas = []
    if preguntas_incorrectas is None:
        if num_preguntas is None:
            preguntas_seleccionadas = preguntas_nivel
            tiempo_limite = 15 * len(preguntas_seleccionadas)
        else:
            preguntas_seleccionadas = random.sample(preguntas_nivel, min(num_preguntas, len(preguntas_nivel)))
            tiempo_limite = 15 * num_preguntas
    else:
        preguntas_seleccionadas = [preguntas_nivel[i] for i in preguntas_incorrectas if i < len(preguntas_nivel)]
        tiempo_limite = 15 * len(preguntas_seleccionadas)

    preguntas_incorrectas_al_nivel = []

    for i, pregunta in enumerate(preguntas_seleccionadas):
        print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)

        tiempo_transcurrido_inicio_pregunta = time.time() - tiempo_inicio
        if tiempo_transcurrido_inicio_pregunta >= tiempo_limite:
            print("¡Se acabó el tiempo!")
            break  # Salir del bucle de preguntas inmediatamente

        respuesta_usuario = obtener_respuesta_valida()

        tiempo_transcurrido_fin_respuesta = time.time() - tiempo_inicio
        if tiempo_transcurrido_fin_respuesta >= tiempo_limite:
            print("¡Se acabó el tiempo!")
            break  # Salir del bucle de preguntas inmediatamente después de que se intente obtener la respuesta

        if respuesta_usuario == pregunta['respuesta_correcta']:
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era la opción {pregunta['respuesta_correcta']}.")
            if preguntas_incorrectas is None:
                preguntas_incorrectas_al_nivel.append(preguntas_nivel.index(pregunta))
            print(pregunta.get('explicacion', 'No hay explicación disponible.'))

    print(f"\nQuiz completado. Tu puntaje es: {puntaje}/{len(preguntas_seleccionadas)}")
    return puntaje, preguntas_incorrectas_al_nivel

def ejecutar_quiz_experto(num_preguntas=None, preguntas_incorrectas=None):
    puntaje = 0
    tiempo_inicio = time.time()
    tiempo_limite = 20 * (num_preguntas if num_preguntas is not None else 1) # Aumentar tiempo límite

    preguntas_nivel = [
        {
            "pregunta": "¿Qué hace el siguiente código con decoradores?\n\n"
                        "def decorador(func):\n"
                        "    def envoltura():\n"
                        "        print('Antes de ejecutar la función')\n"
                        "        func()\n"
                        "        print('Después de ejecutar la función')\n"
                        "    return envoltura\n\n"
                        "@decorador\n"
                        "def saludar():\n"
                        "    print('Hola mundo')\n\n"
                        "saludar()",
            "opciones": ["1.) Llama a saludar sin decorarla", "2.) Ejecuta saludar() antes de decorador()", "3.) Imprime mensajes antes y después de saludar()", "4.) Solo imprime Hola mundo"],
            "respuesta_correcta": 3,
            "explicacion": "El decorador 'decorador' modifica el comportamiento de 'saludar' para imprimir mensajes antes y después de su ejecución."
        },
        # ... (Más preguntas expertas)
    ]

    preguntas_seleccionadas = []
    if preguntas_incorrectas is None:
        if num_preguntas is None:
            preguntas_seleccionadas = preguntas_nivel
            tiempo_limite = 20 * len(preguntas_seleccionadas)
        else:
            preguntas_seleccionadas = random.sample(preguntas_nivel, min(num_preguntas, len(preguntas_nivel)))
            tiempo_limite = 20 * num_preguntas
    else:
        preguntas_seleccionadas = [preguntas_nivel[i] for i in preguntas_incorrectas if i < len(preguntas_nivel)]
        tiempo_limite = 20 * len(preguntas_seleccionadas)

    preguntas_incorrectas_al_nivel = []

    for i, pregunta in enumerate(preguntas_seleccionadas):
        print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(opcion)

        tiempo_transcurrido_inicio_pregunta = time.time() - tiempo_inicio
        if tiempo_transcurrido_inicio_pregunta >= tiempo_limite:
            print("¡Se acabó el tiempo!")
            break  # Salir del bucle de preguntas inmediatamente

        respuesta_usuario = obtener_respuesta_valida()

        tiempo_transcurrido_fin_respuesta = time.time() - tiempo_inicio
        if tiempo_transcurrido_fin_respuesta >= tiempo_limite:
            print("¡Se acabó el tiempo!")
            break  # Salir del bucle de preguntas inmediatamente después de que se intente obtener la respuesta

        if respuesta_usuario == pregunta['respuesta_correcta']:
            print("¡Respuesta correcta!")
            puntaje += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era la opción {pregunta['respuesta_correcta']}.")
            if preguntas_incorrectas is None:
                preguntas_incorrectas_al_nivel.append(preguntas_nivel.index(pregunta))
            print(pregunta.get('explicacion', 'No hay explicación disponible.'))

    print(f"\nQuiz completado. Tu puntaje es: {puntaje}/{len(preguntas_seleccionadas)}")
    return puntaje, preguntas_incorrectas_al_nivel
