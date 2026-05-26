import requests

API_KEY = "SUA_CHAVE_TMDB"  # substitua pela sua chave da TMDB
filme = input("Digite o nome do filme: ")

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

        url_generos = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=pt-BR"
        resposta_generos = requests.get(url_generos, timeout=5)
        resposta_generos.raise_for_status()
        generos = resposta_generos.json()["genres"]

        nomes_generos = [g["name"] for g in generos if g["id"] in genero_ids]

        print("\n🎬 Informações do Filme:")
        print(f"Título: {titulo}")
        print(f"Gêneros: {', '.join(nomes_generos)}")
        print(f"Sinopse: {sinopse}")
    else:
        print("Nenhum filme encontrado.")

except requests.exceptions.RequestException as e:
    print("Erro na requisição:", e)
except KeyError:
    print("Resposta inesperada da API")
