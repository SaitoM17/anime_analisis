import requests

url = 'https://api.jikan.moe/v4/anime'

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        print('Petición exitosa')
        data = response.json()
        lista_data = data.get('data',[])
        # print(lista_data)
        for anime in lista_data:
            mal_id = anime.get('mal_id')
            title_ingles = anime.get('title_english')
            print(f"Título: {mal_id}")
            print(f"Año: {title_ingles}")
            print("---") # Separador para claridad
    else:
        print(f'Error en la petición \nEstado: {response.status_code}')
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f'Error de conexión: {e}')