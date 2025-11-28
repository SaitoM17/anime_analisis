import pandas as pd
import extract 

anime_raw = extract.extraccion_anime()
genero_raw = extract.extraccion_genero()
estudio_raw = extract.extraccion_studios()
popularidad_raw = extract.extraccion_popularidad()
anime_generos_raw = extract.extraccion_anime_genero()
anime_studios_raw = extract.extraccion_anime_studio()

lista_raw = [pd.DataFrame(anime_raw),
             pd.DataFrame(genero_raw),
             pd.DataFrame(estudio_raw),
             pd.DataFrame(popularidad_raw),
             pd.DataFrame(anime_generos_raw),
             pd.DataFrame(anime_studios_raw)
             ]

def imputar_df(lista_df: list[pd.DataFrame]) -> list[pd.DataFrame]:

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

imputar_df(lista_raw)