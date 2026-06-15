"""
Trabajo practico fin

Tarea detectar emociones usando la API de IBM Watson NLP.

Curso Desarrollo de aplicaciones de IA con Python y Flask
Coursera / IBM Skills Network
"""

import json
import requests

EMOTION_API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

EMOTION_API_HEADERS = {
    "Content-Type": "application/json",
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
}

def objeto_emociones():
    """Objeto base para respuesta o tratamiento."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(texto_a_analizar):
    """
    Analiza y detecta emociones en un texto usando la API IBM Watson NLP.

    Args:
        text_to_analyze (str): Texto conteniendo un mensaje o frase.

    Devuelve:
        dict: Un diccionario con los valores asignado por la API
              y la emocion principal calculada.
              Contempla los errores de recibir valores nulos o vacios
              y la respuesta con fallos de la API.
    """
    # Return None values for empty or None input
    objeto_resultado = objeto_emociones()
    if texto_a_analizar is None or not str(texto_a_analizar).strip():
        return objeto_resultado

    mensaje = {"raw_document": {"text": texto_a_analizar}}
    respuesta = requests.post(
        EMOTION_API_URL,
        json=mensaje,
        headers=EMOTION_API_HEADERS,
        timeout=10,
    )
    resultado = json.loads(respuesta.text)

    if respuesta.status_code == 200:
        puntajes = resultado['emotionPredictions'][0]['emotion']
        emocion = max(puntajes, key=puntajes.get)
        objeto_resultado["anger"] = puntajes.get('anger')
        objeto_resultado["fear"] = puntajes.get('fear')
        objeto_resultado["joy"] = puntajes.get('joy')
        objeto_resultado["sadness"] = puntajes.get('sadness')
        objeto_resultado["disgust"] = puntajes.get('disgust')
        objeto_resultado["dominant_emotion"] = emocion
    elif respuesta.status_code == 400:
        return objeto_resultado

    return objeto_resultado
