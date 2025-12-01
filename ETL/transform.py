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


anime_raw = extract.extraccion_anime(3)
genero_raw = extract.extraccion_genero()
estudio_raw = extract.extraccion_studios(3)
popularidad_raw = extract.extraccion_popularidad(3)
anime_generos_raw = extract.extraccion_anime_genero(3)
anime_studios_raw = extract.extraccion_anime_studio(3)

lista_raw = [pd.DataFrame(anime_raw),
             pd.DataFrame(genero_raw),
             pd.DataFrame(estudio_raw),
             pd.DataFrame(popularidad_raw),
             pd.DataFrame(anime_generos_raw),
             pd.DataFrame(anime_studios_raw)
             ]
                    

lista = imputar_df(lista_raw)

print(lista[0])