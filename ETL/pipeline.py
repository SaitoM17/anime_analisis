import pandas as pd
import extract
import transform
import load

num_paginas = 500
print(f'Configurado para extraer {num_paginas} páginas de datos')


def extraccion_data(num_paginas):
    
    print('\n--- INICIO DE EXTRACCIÓN (E) ---')
    
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

def transformacion_data(lista_df_raw):

    print('\n--- INICIO DE TRANSFORMACIÓN (T) ---')

    lista_df_imputados = transform.imputar_df(lista_df_raw)
    lista_df_cambio_tipo = transform.cambio_tipo_dato(lista_df_imputados)

    return lista_df_cambio_tipo

def carga_data(df_final):

    print('\n--- INICIO DE CARGA (L) ---')

    secuencia_carga = [
        (df_final[0], load.load_animes, 'Animes'),
        (df_final[1], load.load_generos, 'Generos'),
        (df_final[2], load.load_estudios, 'Estudios'),
        (df_final[3], load.load_popularidad, 'Popularidad'),
        (df_final[4], load.load_anime_generos, 'Animes_Generos'),
        (df_final[5], load.load_anime_estudios, 'Animes_Estudios'),
    ]

    for df, fun_load, nombre_tabla in secuencia_carga:
        print(f'Cargando datos de tabla {nombre_tabla} ({df.shape[0]} filas)...')
        fun_load(df)

    print(f'\nPIPELINE "ETL" COMPLETO')

if __name__ == '__main__':
    lista_df_raw = extraccion_data(num_paginas)
    lista_df_final = transformacion_data(lista_df_raw)
    carga_data(lista_df_final)