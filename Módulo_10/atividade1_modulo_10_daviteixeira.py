import requests

API_KEY = "d6075d548c107294a8cfcd0969b5f3c8"
cidade = "São Paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()

    temperatura = dados["main"]["temp"]
    condicao = dados["weather"][0]["description"]

    print(f"🌡️ Temperatura atual em {cidade}: {temperatura}°C")
    print(f"☁️ Condições climáticas: {condicao}")

except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
except KeyError:
    print("Resposta inesperada da API")
