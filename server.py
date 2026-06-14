from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Detector de emociones")
app.json.sort_keys = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detection():
    if request.method == 'POST':
        if request.is_json:
            datos_json = request.get_json()
            texto = datos_json.get("textToAnalyze")
        else:
            texto = request.form.get('textToAnalyze', '')
    elif request.method == "GET":
        texto = request.args.get('textToAnalyze', '')
    else:
        return( "Error en el requerimiento", 200)

    respuesta = emotion_detector(texto)
    if respuesta['dominant_emotion'] is None:
        return "No se ha reconocido ninguna emoción! "
    return jsonify(respuesta), 200

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)
