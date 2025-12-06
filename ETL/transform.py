import pandas as pd
import extract 

def imputar_df(lista_df: list[pd.DataFrame]) -> list[pd.DataFrame]:

    lista_df_limpios = []

    for nombre_df, df in lista_df:
        print(f'\n--- Limpiando DataFrame "{nombre_df}" (Columnas: {list(df.columns)}) ---')

        if 'establecido' in df.columns:
            df['establecido'] = pd.to_datetime(df['establecido'], errors='coerce')
            df['establecido'] = df['establecido'].dt.strftime('%Y-%m-%d')
            imputacion_fecha = '2261-12-31'
            df['establecido'] = df['establecido'].fillna(imputacion_fecha).replace('NaT', imputacion_fecha)
            print(f"Imputado 'establecido': Nulos (NaT) rellenados con '{imputacion_fecha}'")

        if 'annio' in df.columns:
            df['annio'] = df['annio'].fillna(0)
            print(f"Imputación 'annio': Nulos rellenados con '0' ")

        # Detectar valores nulos e imputarlos con 'N/A y '0
        for columna in df.columns:
            if df[columna].isnull().any():
                
                # Verificar si el tipo de dato es TEXTO (object/string)
                if df[columna].dtype == object:
                    df[columna] = df[columna].fillna('N/A')
                    print(f"Imputado '{columna}': Nulos rellenados con 'N/A'")
                
                # Verificar si el tipo de dato es NUMÉRICO (int, float, etc.)
                elif pd.api.types.is_numeric_dtype(df[columna]):
                    df[columna] = df[columna].fillna(9999) #.astype(int) # Usar .astype(int) para asegurar enteros si aplica
                    print(f"Imputado '{columna}': Nulos rellenados con '9999'")
                
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
    tabla_anime['tipo'] = tabla_anime['tipo'].astype(object)
    tabla_anime['episodios'] = tabla_anime['episodios'].astype(int)
    tabla_anime['annio'] = tabla_anime['annio'].astype(int)
    tabla_anime['temporada'] = tabla_anime['temporada'].astype(object)
    tabla_anime['clasificacion'] = tabla_anime['clasificacion'].astype(object)
    tabla_anime['duracion'] = tabla_anime['duracion'].astype(object)
    tabla_anime['sinopsis'] = tabla_anime['sinopsis'].astype(object)
    tabla_anime['anime_rank'] = tabla_anime['anime_rank'].astype(int)

    #Tabla genero
    tabla_genero = lista_df[1]
    tabla_genero['genero_id'] = tabla_genero['genero_id'].astype(int)
    tabla_genero['nombre_genero'] = tabla_genero['nombre_genero'].astype(object)


    #Tabla estudio
    tabla_estudio = lista_df[2]
    tabla_estudio['mal_id'] = tabla_estudio['mal_id'].astype(int)
    tabla_estudio['nombre_studio'] = tabla_estudio['nombre_studio'].astype(object)
    tabla_estudio['favoritos'] = tabla_estudio['favoritos'].astype(int)
    tabla_estudio['establecido'] = pd.to_datetime(tabla_estudio['establecido'], format='%Y-%m-%d')

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