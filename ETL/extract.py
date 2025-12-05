import requests
import time

def extraccion_anime(num_paginas):
    anime_dic = {
        'mal_id': [],
        'titulo': [],
        'tipo': [],
        'episodios': [],
        'annio': [],
        'temporada': [],
        'clasificacion': [],
        'duracion': [],
        'sinopsis': [],
        'anime_rank': []
    }

    for pagina in range(1,num_paginas+1):
        url = f'https://api.jikan.moe/v4/anime?page={pagina}'

        try:
            response = requests.get(url)

            time.sleep(0.5)
            
            if response.status_code == 200:
                print('Petición exitosa')
                data = response.json()
                lista_data = data.get('data',[])
                
                for anime in lista_data:
                    lista_titulos = anime.get('titles')

                    if lista_titulos:
                        for titulo in lista_titulos:
                            titulo_ = titulo.get('title')
                            break
                    
                    mal_id = anime.get('mal_id')
                    tipo = anime.get('type')
                    episodios = anime.get('episodes')
                    annio = anime.get('year')
                    season = anime.get('season')
                    rating = anime.get('rating')
                    duracion = anime.get('duration')
                    synopsis = anime.get('synopsis')
                    rank_anime = anime.get('rank')

                    anime_dic['mal_id'].append(mal_id)
                    anime_dic['titulo'].append(titulo_)
                    anime_dic['tipo'].append(tipo)
                    anime_dic['episodios'].append(episodios)
                    anime_dic['annio'].append(annio)
                    anime_dic['temporada'].append(season)
                    anime_dic['clasificacion'].append(rating)
                    anime_dic['duracion'].append(duracion)
                    anime_dic['sinopsis'].append(synopsis)
                    anime_dic['anime_rank'].append(rank_anime)
        
            else:
                print(f'Error en la petición \nEstado: {response.status_code}')
                print(response.text)

        except requests.exceptions.RequestException as e:
            print(f'Error de conexión: {e}')

    return anime_dic

def extraccion_genero():
    genero_dic = {
        'genero_id': [],
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
                genero_dic['genero_id'].append(genero.get('mal_id'))
                genero_dic['nombre_genero'].append(genero.get('name'))
        
        else:
            print(f'Error en la petición \nEstado: {response.status_code}')
            print(response.text)

    except requests.exceptions.RequestException as e:
            print(f'Error de conexión: {e}')

    return genero_dic

def extraccion_estudios(num_paginas):
    studios_dic = {
        'mal_id': [],
        'nombre_studio': [],
        'favoritos': [],
        'establecido': []
    }
    for pagina in range(1,num_paginas+1):
        url = f'https://api.jikan.moe/v4/producers?page={pagina}'

        try:
            response = requests.get(url)

            time.sleep(0.5)
                
            if response.status_code == 200:
                print('Petición exitosa')
                data = response.json()
                lista_data = data.get('data',[])
                    
                for anime in lista_data:
                    studios_dic['mal_id'].append(anime.get('mal_id'))
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

def extraccion_popularidad(num_paginas):
    popularidad_dic = {
        'mal_id': [],
        'score': [],
        'scored_by': [],
        'miembros': [],
        'favoritos': [],
        'popularidad': []
    }

    for pagina in range(1,num_paginas+1):
        url = f'https://api.jikan.moe/v4/anime?page={pagina}'

        try:
            response = requests.get(url)

            time.sleep(0.5)
            
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

def extraccion_anime_genero(num_paginas):
    anime_genero_dic = {
        'mal_id': [],
        'genero_id': [],
    }

    for pagina in range(1,num_paginas+1):
        url = f'https://api.jikan.moe/v4/anime?page={pagina}'

        try:
            response = requests.get(url)

            time.sleep(0.5)
            
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

def extraccion_anime_estudio(num_paginas):
    anime_studio_dic = {
        'mal_id': [],
        'studio_id': [],
    }

    for pagina in range(1,num_paginas+1):
        url = f'https://api.jikan.moe/v4/anime?page={pagina}'

        try:
            response = requests.get(url)

            time.sleep(0.5)
            
            if response.status_code == 200:
                print('Petición exitosa')
                data = response.json()
                lista_data = data.get('data',[])
                
                for anime in lista_data:
                    anime_mal_id = anime.get('mal_id')
                    lista_studio = anime.get('studios')

                    if lista_studio:
                        for studio in lista_studio:
                            studio_id = studio.get('mal_id')
                            
                            # Agrega el par (Anime ID, Género ID) por cada iteración
                            anime_studio_dic['mal_id'].append(anime_mal_id)
                            anime_studio_dic['studio_id'].append(studio_id)
        
            else:
                print(f'Error en la petición \nEstado: {response.status_code}')
                print(response.text)

        except requests.exceptions.RequestException as e:
            print(f'Error de conexión: {e}')

    return anime_studio_dic