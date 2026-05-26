import requests

API_KEY = "SUA_CHAVE_TMDB"
filme = "Inception"
url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={filme}&language=pt-BR"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()

    if dados["results"]:
        filme_info = dados["results"][0]
        titulo = filme_info["title"]
        sinopse = filme_info["overview"]
        genero_ids = filme_info["genre_ids"]

        print(f"🎬 Título: {titulo}")
        print(f"📖 Sinopse: {sinopse}")
        print(f"🎭 Gêneros (IDs): {genero_ids}")
    else:
        print("Nenhum filme encontrado.")

except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
except KeyError:
    print("Resposta inesperada da API")
