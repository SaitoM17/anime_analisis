import requests

url = 'https://api.jikan.moe/v4/producers'

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        print('Petición exitosa')
        data = response.json()
        lista_data = data['data']
        print(lista_data)
    else:
        print(f'Error en la petición \nEstado: {response.status_code}')
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f'Error de conexión: {e}')