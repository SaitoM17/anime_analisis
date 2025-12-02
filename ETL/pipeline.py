import pandas as pd
import extract
import transform

def extraccion_data(num_paginas):

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

def transformacion_data(df):
    lista_df_imputados = transform.imputar_df(df)
    lista_df_cambio_tipo = transform.cambio_tipo_dato(lista_df_imputados)

    return lista_df_cambio_tipo


num_paginas = int(input('Ingresa haste pagina extraer información: '))
tablas = extraccion_data(num_paginas)
print(transformacion_data(tablas))