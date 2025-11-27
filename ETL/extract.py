import requests

anime_dic = {
    'mal_id': [],
    'titulo': [],
    'titulo_ingles': [],
    'titulo_japones': [],
    'tipo': [],
    'episodios': [],
    'annio': [],
    'temporada': [],
    'clasifificacion': [],
    'duracion': [],
    'sipnosis': [],
    'anime_rank': []
}

for pagina in range(1,3):
    url = f'https://api.jikan.moe/v4/anime?page={pagina}'

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            print('Petición exitosa')
            data = response.json()
            lista_data = data.get('data',[])
            
            for anime in lista_data:
                anime_dic['mal_id'].append(anime.get('mal_id'))
                anime_dic['titulo'].append(anime.get('title'))
                anime_dic['titulo_ingles'].append(anime.get('title_english'))
                anime_dic['titulo_ingles'].append(anime.get('title_japanese'))
                anime_dic['tipo'].append(anime.get('type'))
                anime_dic['episodios'].append(anime.get('episodes'))
                anime_dic['temporada'].append(anime.get('season'))
                anime_dic['clasifificacion'].append(anime.get('rating'))
                anime_dic['duracion'].append(anime.get('duration'))
                anime_dic['sipnosis'].append(anime.get('synopsis'))
                anime_dic['anime_rank'].append(anime.get('rank'))
    
        else:
            print(f'Error en la petición \nEstado: {response.status_code}')
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f'Error de conexión: {e}')

print(anime_dic)