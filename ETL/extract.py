import requests
import pandas as pd

def extraccion_anime():
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
                    anime_dic['titulo_japones'].append(anime.get('title_japanese'))
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

    return anime_dic

def extraccion_genero():
    genero_dic = {
        'genre_id': [],
        'nombre_genero': [],
    }

    url = f'https://api.jikan.moe/v4/genres/anime'

    try:
        response = requests.get(url)
            
        if response.status_code == 200:
            print('Petición exitosa')
            data = response.json()
            lista_data = data.get('data',[])
                
            for genero in lista_data:
                genero_dic['genre_id'].append(genero.get('mal_id'))
                genero_dic['nombre_genero'].append(genero.get('name'))
        
        else:
            print(f'Error en la petición \nEstado: {response.status_code}')
            print(response.text)

    except requests.exceptions.RequestException as e:
            print(f'Error de conexión: {e}')

    return genero_dic

def extraccion_studios():
    studios_dic = {
        'mal_id': [],
        'nombre_studio': [],
        'favoritos': [],
        'establecido': []
    }

    url = f'https://api.jikan.moe/v4/producers'

    try:
        response = requests.get(url)
            
        if response.status_code == 200:
            print('Petición exitosa')
            data = response.json()
            lista_data = data.get('data',[])
                
            for anime in lista_data:
                studios_dic['mal_id'].append(anime.get('mal_id'))
                lista_titulos = anime.get('titles')
                studios_dic['favoritos'].append(anime.get('favorites'))
                studios_dic['establecido'].append(anime.get('established'))

                nombre_principal = None
                lista_titulos = anime.get('titles')
                
                # Verificamos si la lista de títulos existe y no está vacía
                if lista_titulos and len(lista_titulos) > 0:
                    # Elegimos SOLO el primer título de la lista
                    nombre_principal = lista_titulos[0].get('title')
                
                # Añadimos el título (o None si no se encontró) UNA SOLA VEZ
                studios_dic['nombre_studio'].append(nombre_principal)
        
        else:
            print(f'Error en la petición \nEstado: {response.status_code}')
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f'Error de conexión: {e}')

    return studios_dic

def extraccion_popularidad():
    popularidad_dic = {
        'mal_id': [],
        'score': [],
        'scored_by': [],
        'miembros': [],
        'favoritos': [],
        'popularidad': []
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
                    popularidad_dic['mal_id'].append(anime.get('mal_id'))
                    popularidad_dic['score'].append(anime.get('score'))
                    popularidad_dic['scored_by'].append(anime.get('scored_by'))
                    popularidad_dic['miembros'].append(anime.get('members'))
                    popularidad_dic['favoritos'].append(anime.get('favorites'))
                    popularidad_dic['popularidad'].append(anime.get('popularity'))
        
            else:
                print(f'Error en la petición \nEstado: {response.status_code}')
                print(response.text)

        except requests.exceptions.RequestException as e:
            print(f'Error de conexión: {e}')

    return popularidad_dic

def extraccion_anime_genero():
    anime_genero_dic = {
        'mal_id': [],
        'genero_id': [],
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
                    anime_mal_id = anime.get('mal_id')
                    lista_genero = anime.get('genres')

                    if lista_genero:
                        for genero in lista_genero:
                            genero_id = genero.get('mal_id')
                            
                            # Agrega el par (Anime ID, Género ID) por cada iteración
                            anime_genero_dic['mal_id'].append(anime_mal_id)
                            anime_genero_dic['genero_id'].append(genero_id)
        
            else:
                print(f'Error en la petición \nEstado: {response.status_code}')
                print(response.text)

        except requests.exceptions.RequestException as e:
            print(f'Error de conexión: {e}')

    return anime_genero_dic

tabla_n_m = extraccion_anime_genero()
df_link_genres = pd.DataFrame(tabla_n_m)
print(extraccion_anime_genero())

print('\n--- Resultado con Lógica N:M ---')
print(f'Longitud de mal_id (total de filas): {len(df_link_genres["mal_id"])}')
print(f'Número de animes únicos: {df_link_genres["mal_id"].nunique()}')