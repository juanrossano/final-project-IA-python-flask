import json
import urllib.parse
import urllib.request
from urllib.error import HTTPError

BASE_URL = "http://127.0.0.1:5000/emotionDetector"


def _print_response_body(body_text):
    try:
        print("Respuesta del Servidor:")
        print(json.dumps(json.loads(body_text), indent=4))
    except Exception:
        # No es JSON, imprimir crudo
        print("Respuesta del Servidor (raw):")
        print(body_text)


def probar_get(texto):
    print(f"\n--- Probando GET con: '{texto}' ---")
    texto_codificado = urllib.parse.quote(texto)
    url = f"{BASE_URL}?textToAnalyze={texto_codificado}"

    try:
        with urllib.request.urlopen(url) as response:
            resultado = response.read().decode("utf-8")
            _print_response_body(resultado)
    except HTTPError as e:
        cuerpo = e.read().decode("utf-8")
        print(f"Error en la petición GET: {e}")
        if cuerpo:
            _print_response_body(cuerpo)
    except Exception as e:
        print(f"Error en la petición GET: {e}")


def probar_post(texto):
    print(f"\n--- Probando POST con: '{texto}' ---")
    data = json.dumps({"textToAnalyze": texto}).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL, data=data, headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            resultado = response.read().decode("utf-8")
            _print_response_body(resultado)
    except HTTPError as e:
        cuerpo = e.read().decode("utf-8")
        print(f"Error en la petición POST: {e}")
        if cuerpo:
            _print_response_body(cuerpo)
    except Exception as e:
        print(f"Error en la petición POST: {e}")


if __name__ == "__main__":
    # Ejecuta las pruebas
    probar_get("I am happy")
    probar_post("I love my life")
    probar_get("I think I am having fun")
    probar_post("I think I am having fun")
    probar_get("")
    probar_post("")
   
