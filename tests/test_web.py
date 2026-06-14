import json
import urllib.parse
import urllib.request

BASE_URL = "http://127.0.0.1:5000/emotionDetector"


def probar_get(texto):
    print(f"\n--- Probando GET con: '{texto}' ---")
    # Codificamos el texto correctamente para la URL (convierte espacios en %20, etc.)
    texto_codificado = urllib.parse.quote(texto)
    url = f"{BASE_URL}?text={texto_codificado}"

    try:
        with urllib.request.urlopen(url) as response:
            resultado = response.read().decode("utf-8")
            print("Respuesta del Servidor:")
            print(json.dumps(json.loads(resultado), indent=4))
    except Exception as e:
        print(f"Error en la petición GET: {e}")


def probar_post(texto):
    print(f"\n--- Probando POST con: '{texto}' ---")
    data = json.dumps({"text": texto}).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL, data=data, headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            resultado = response.read().decode("utf-8")
            print("Respuesta del Servidor:")
            print(json.dumps(json.loads(resultado), indent=4))
    except Exception as e:
        print(f"Error en la petición POST: {e}")


if __name__ == "__main__":
    # Ejecuta las pruebas
    probar_get("I am happy")
    probar_post("I love my life")
