"""
Servidor Flask para aplicacion de deteccion de emociones

Trabajo practico
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Detector de emociones")
app.json.sort_keys = False

@app.route('/')
def index():
    """Renderiza la pagina principal."""
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detection():
    """
    Endpoint para procesar la solicitud

    Acepta ambos GET y POST con el parametro 'textToAnalyze'.

    Devuelve:
        str: Formatea la respuesta con la identificacion de la emocion 
        por parte del servicio con un tratamiento de errores.
    """
    if request.method == 'POST':
        if request.is_json:
            datos_json = request.get_json()
            frase = datos_json.get("textToAnalyze")
        else:
            frase = request.form.get('textToAnalyze', '')
    elif request.method == "GET":
        frase = request.args.get('textToAnalyze', '')
    else:
        return( "Error en el requerimiento", 200)

    if not frase or not str(frase).strip():
        return "Invalid text! Please try again!", 400

    respuesta = emotion_detector(frase)

    if respuesta['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    return respuesta, 200

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)
