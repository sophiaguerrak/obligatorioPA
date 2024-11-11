import pandas as pd
from itertools import chain

preguntas_todas = pd.read_csv('trivia_questions.csv', delimiter=';')  # Cargamos las preguntas usando pandas

def capitalizar_input(func):
    """
    Decorador que capitaliza la primera letra de la respuesta del usuario.
    """
    def wrapper(*args, **kwargs):
        respuesta = func(*args, **kwargs)
        return respuesta.capitalize()  # Capitaliza la primera letra (todas las respuestas están en mayúscula). El resto de los caracteres se convierten a lowercase.
    return wrapper

@capitalizar_input
def obtener_respuesta_usuario():
    return input('Respuesta: ')

def hacer_pregunta(preguntas, puntaje):
    """
    Función recursiva que hace preguntas al usuario y actualiza el puntaje.

    Args:
        preguntas (DataFrame): CSV con las preguntas que no han sido preguntadas aun.
        puntaje (int): Puntaje acumulado del jugador.

    Devuelve:
        int: Puntaje final después de responder todas las preguntas.
    """
    if preguntas.empty:
        return puntaje
    pregunta = preguntas.iloc[0]
    mostrar_pregunta_opciones(pregunta)
    respuesta = obtener_respuesta_usuario()
    puntaje += verificar_respuesta(pregunta, respuesta)
    if verificar_respuesta(pregunta, respuesta) == 0:
        print('Incorrecto. La respuesta era: ' + pregunta['Correcta'])
    else:
        print('Correcto')
    return hacer_pregunta(preguntas.iloc[1:], puntaje)

verificar_respuesta = lambda pregunta, respuesta: 10 if respuesta == pregunta['Correcta'] else 0
# Lambda para verificar la respuesta, si es correcta agrega 10 al puntaje, si es incorrecta no agrega nada.

def mostrar_pregunta_opciones(pregunta):
    """
    Muestra la pregunta y las opciones de respuesta.

    Args:
        pregunta (Series): Una fila del DataFrame que contiene la pregunta y las opciones.

    Devuelve:
        None
    """
    opciones = list(chain([pregunta['Respuesta1'], pregunta['Respuesta2'], pregunta['Respuesta3']]))
    print('Pregunta: ' + pregunta['Pregunta'] + ' Opciones: ' + ', '.join(opciones))

def trivia(preguntas_todas):
    """
    Función principal del juego de trivia, selecciona 5 preguntas al azar y calcula el puntaje final.

    Args:
        preguntas_todas (DataFrame): DataFrame que contiene todas las preguntas disponibles.

    Devuelve:
        None
    """
    puntaje = 0
    preguntas = preguntas_todas.sample(n=5)
    
    puntaje_total = hacer_pregunta(preguntas, puntaje)
    print(f"Tu puntaje final es: {puntaje_total}/50")

trivia(preguntas_todas)
