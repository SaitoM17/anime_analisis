import pandas as pd
import extract 

def imputar_df(lista_df: list[pd.DataFrame]) -> list[pd.DataFrame]:

    lista_df_limpios = []

    for idx, df in enumerate(lista_df):
        print(f'\n--- Limpiando DataFrame {idx + 1}/{len(lista_df)} (Columnas: {list(df.columns)}) ---')

        # Detectar valores nulos e imputarlos con 'N/A y '0
        for columna in df.columns:
            if df[columna].isnull().any():
                
                # Verificar si el tipo de dato es TEXTO (object/string)
                if df[columna].dtype == object:
                    df[columna] = df[columna].fillna('N/A')
                    print(f"Imputado '{columna}': Nulos rellenados con 'N/A'")
                
                # Verificar si el tipo de dato es NUMÉRICO (int, float, etc.)
                elif pd.api.types.is_numeric_dtype(df[columna]):
                    df[columna] = df[columna].fillna(0) #.astype(int) # Usar .astype(int) para asegurar enteros si aplica
                    print(f"Imputado '{columna}': Nulos rellenados con 0")
                
                else:
                    print(f"Columna '{columna}' contiene nulos pero no es numérica ni de texto; se omitió.")
            
        lista_df_limpios.append(df)
    
    return lista_df_limpios

def cambio_tipo_dato(lista_df):

    lista_df_tipo_correcto = []
    # Tabla anime
    tabla_anime = lista_df[0]
    tabla_anime['mal_id'] = tabla_anime['mal_id'].astype(int)
    tabla_anime['titulo'] = tabla_anime['titulo'].astype(object)
    tabla_anime['titulo_ingles'] = tabla_anime['titulo_ingles'].astype(object)
    tabla_anime['titulo_japones'] = tabla_anime['titulo_japones'].astype(object)
    tabla_anime['tipo'] = tabla_anime['tipo'].astype(object)
    tabla_anime['episodios'] = tabla_anime['episodios'].astype(int)
    tabla_anime['annio'] = tabla_anime['annio'].astype(int)
    tabla_anime['temporada'] = tabla_anime['temporada'].astype(object)
    tabla_anime['clasifificacion'] = tabla_anime['clasifificacion'].astype(object)
    tabla_anime['duracion'] = tabla_anime['duracion'].astype(object)
    tabla_anime['sipnosis'] = tabla_anime['sipnosis'].astype(object)
    tabla_anime['anime_rank'] = tabla_anime['anime_rank'].astype(int)

    #Tabla genero
    tabla_genero = lista_df[1]
    tabla_genero['genre_id'] = tabla_genero['genre_id'].astype(int)
    tabla_genero['nombre_genero'] = tabla_genero['nombre_genero'].astype(object)

    #Tabla estudio
    tabla_estudio = lista_df[2]
    tabla_estudio['mal_id'] = tabla_estudio['mal_id'].astype(int)
    tabla_estudio['nombre_studio'] = tabla_estudio['nombre_studio'].astype(object)
    tabla_estudio['favoritos'] = tabla_estudio['favoritos'].astype(int)
    tabla_estudio['establecido'] = (pd.to_datetime(tabla_estudio['establecido'], errors='coerce').dt.date.astype(str))
    tabla_estudio['establecido'] = (
    tabla_estudio['establecido']
    .replace('NaT', 0) # Reemplaza la cadena 'NaT' con el objeto Python None
)

    #Tabla de popularidad
    tabla_popularidad = lista_df[3]
    tabla_popularidad['mal_id'] = tabla_popularidad['mal_id'].astype(int)
    tabla_popularidad['score'] = tabla_popularidad['score'].astype(float)
    tabla_popularidad['scored_by'] = tabla_popularidad['scored_by'].astype(int)
    tabla_popularidad['miembros'] = tabla_popularidad['miembros'].astype(int)
    tabla_popularidad['favoritos'] = tabla_popularidad['favoritos'].astype(int)
    tabla_popularidad['popularidad'] = tabla_popularidad['popularidad'].astype(int)

    #Tabla anime_genero
    tabla_anime_genero = lista_df[4]
    tabla_anime_genero['mal_id'] = tabla_anime_genero['mal_id'].astype(int)
    tabla_anime_genero['genero_id'] = tabla_anime_genero['genero_id'].astype(int)

    #Tabla anime_estudio
    tabla_anime_estudio = lista_df[5]
    tabla_anime_estudio['mal_id'] = tabla_anime_estudio['mal_id'].astype(int)
    tabla_anime_estudio['studio_id'] = tabla_anime_estudio['studio_id'].astype(int)

    lista_df_tipo_correcto.append(tabla_anime)
    lista_df_tipo_correcto.append(tabla_genero)
    lista_df_tipo_correcto.append(tabla_estudio)
    lista_df_tipo_correcto.append(tabla_popularidad)
    lista_df_tipo_correcto.append(tabla_anime_genero)
    lista_df_tipo_correcto.append(tabla_anime_estudio)

    return lista_df_tipo_correcto

anime_raw = extract.extraccion_anime(3)
genero_raw = extract.extraccion_genero()
estudio_raw = extract.extraccion_estudios(3)
popularidad_raw = extract.extraccion_popularidad(3)
anime_generos_raw = extract.extraccion_anime_genero(3)
anime_studios_raw = extract.extraccion_anime_estudio(3)

lista_raw = [pd.DataFrame(anime_raw),
             pd.DataFrame(genero_raw),
             pd.DataFrame(estudio_raw),
             pd.DataFrame(popularidad_raw),
             pd.DataFrame(anime_generos_raw),
             pd.DataFrame(anime_studios_raw)
             ]
                    

lista_df_limpios = imputar_df(lista_raw)
lista_df_tipo_correcto = cambio_tipo_dato(lista_df_limpios)

# print(cambio_tipo_dato(lista))
print("\n--- Verificación de Tipos de Datos (Tabla Popularidad) ---")
print(lista_df_tipo_correcto[2].dtypes)
print(lista_df_tipo_correcto[2])