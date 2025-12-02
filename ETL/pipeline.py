import pandas as pd
import extract

def extraccion_data(num_paginas):

    lista_df_raw = []

    data_animes_raw = extract.extraccion_anime(num_paginas)
    data_generos_raw = extract.extraccion_genero()
    data_estudios_raw = extract.extraccion_estudios(num_paginas)
    data_popularidad_raw = extract.extraccion_popularidad(num_paginas)
    data_anime_generos_raw = extract.extraccion_anime_genero(num_paginas)
    data_anime_estudios_raw = extract.extraccion_anime_estudio(num_paginas)

    lista_df_raw = [
                    pd.DataFrame(data_animes_raw),
                    pd.DataFrame(data_generos_raw),
                    pd.DataFrame(data_estudios_raw),
                    pd.DataFrame(data_popularidad_raw),
                    pd.DataFrame(data_anime_generos_raw),
                    pd.DataFrame(data_anime_estudios_raw)
                    ]

    return lista_df_raw


num_paginas = int(input('Ingresa haste pagina extraer información: '))
tablas = extraccion_data(num_paginas)

print(f'Tabla animes')
print(tablas[0].info())
print(f'\nTabla generos')
print(tablas[1].info())
print(f'\nTabla estudios')
print(tablas[2].info())
print(f'\nTabla popularidad')
print(tablas[3].info())
print(f'\nTabla anime_generos')
print(tablas[4].info())
print(f'\nTabla anime_estudios')
print(tablas[5].info())