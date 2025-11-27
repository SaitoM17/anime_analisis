import requests

anime_dic = {
    'mal_id': [],
    'title': []
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
                mal_id = anime.get('mal_id')
                title_ingles = anime.get('title_english')
                
                anime_dic['mal_id'].append(mal_id)
                anime_dic['title'].append(title_ingles)
        else:
            print(f'Error en la petición \nEstado: {response.status_code}')
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f'Error de conexión: {e}')

print(anime_dic)