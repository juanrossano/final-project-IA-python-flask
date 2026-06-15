Usar en Git Bash o cualquier terminal compatible con Bash:

```bash
python -m pip install -r requirements.txt
```

o

```bash
python3 -m pip install -r requirements.txt
```

Ejecutar el servidor

```bash
flask --app server --debug run
```

En ingles

```python
from EmotionDetection.emotion_detection import emotion_detector
print(emotion_detector("I love this new technology."))
```

| Statement | Dominant Emotion |
| ----- | ----- |
| I am glad this happened | joy |
| I am really mad about this | anger |
| I feel disgusted just hearing about this | disgust |
| I am so sad about this | sadness |
| I am really afraid that this will happen | fear |

en despliegue

I love my life

En español

```python
from EmotionDetection.emotion_detection import emotion_detector
print(emotion_detector("Odio trabajar muchas horas"))
```

| Declaración | Emoción Dominante |
| ----- | ----- |
| Me alegra que esto haya sucedido | alegría |
| Estoy realmente enojado por esto | ira |
| Me siento disgustado solo de escuchar sobre esto | desagrado |
| Estoy tan triste por esto | tristeza |
| Tengo mucho miedo de que esto suceda | miedo |

en despliegue

I think I am having fun

Amo mi vida


Despliegue y pruebas

curl http://127.0.0.1:5000/

Metodo GET

curl "http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20am%20happy"


Metodo POST

curl -X POST http://127.0.0.1:5000/emotionDetector \
  -H "Content-Type: application/json" \
  -d '{"textToAnalyze":"I love my life"}'
