-- Identificación de problemas en los datos
SELECT COUNT(*) cantidad_registros_animes FROM animes; -- 12500
SELECT COUNT(*) cantidad_registros_generos FROM generos; -- 78
SELECT COUNT(*) cantidad_registros_estudios FROM estudios; -- 2700
SELECT COUNT(*) cantidad_registros_popularidad FROM popularidad; -- 12500
SELECT COUNT(*) cantidad_registros_anime_generos FROM anime_generos; -- 22397
SELECT COUNT(*) cantidad_registros_anime_estudios FROM anime_estudios; -- 10669

-- Identificación de valores nulos en tabla animes
SELECT
    SUM(IF(mal_id IS NULL, 1, 0)) AS nulos_mal_id,
    SUM(IF(titulo IS NULL, 1, 0)) AS nulos_titulo,
    SUM(IF(tipo IS NULL, 1, 0)) AS nulos_tipo,
    SUM(IF(episodios IS NULL, 1, 0)) AS nulos_episodios,
    SUM(IF(annio IS NULL, 1, 0)) AS Faltantes_annio,
    SUM(IF(temporada IS NULL, 1, 0)) AS nulos_temporada,
    SUM(IF(clasificacion IS NULL, 1, 0)) AS nulos_clasificación,
    SUM(IF(duracion IS NULL, 1, 0)) AS nulos_duración,
    SUM(IF(sinopsis IS NULL, 1, 0)) AS nulos_sinopsis,
    SUM(IF(anime_rank IS NULL, 1, 0)) AS nulos_anime_rank
FROM
    animes;

-- Identificación de valores nulos en tabla generos
SELECT
    SUM(IF(genero_id IS NULL, 1, 0)) AS nulos_genero_id,
    SUM(IF(nombre_genero IS NULL, 1, 0)) AS nulos_nombre_genero
FROM
    generos;
    
-- Identificación de valores nulos en tabla estudios
SELECT
    SUM(IF(estudio_id IS NULL, 1, 0)) AS nulos_estudio_id,
    SUM(IF(nombre_estudio IS NULL, 1, 0)) AS nulos_nombre_estudio,
    SUM(IF(favoritos IS NULL, 1, 0)) AS nulos_titulo_favoritos,
    SUM(IF(establecido IS NULL, 1, 0)) AS nulos_establecido
FROM
    estudios;
-- Se identifico 1355 valores nulos en la columna establecido y 78 valores faltantes.

-- Identificación de valores nulos en tabla popularidad
SELECT
    SUM(IF(mal_id IS NULL, 1, 0)) AS nulos_mal_id,
    SUM(IF(score IS NULL, 1, 0)) AS nulos_score,
    SUM(IF(scored_by IS NULL, 1, 0)) AS nulos_scored_by,
    SUM(IF(favoritos IS NULL, 1, 0)) AS nulos_favoritos,
    SUM(IF(popularidad IS NULL,1,0)) AS nulos_popularidad
FROM
    popularidad;
    
-- Identificación de valores nulos en tabla animes_generos
SELECT
    SUM(IF(mal_id IS NULL, 1, 0)) AS nulos_mal_id,
    SUM(IF(genero_id IS NULL, 1, 0)) AS nulos_genero_id
FROM
    anime_generos;
    
-- Identificación de valores nulos en tabla animes_estudios
SELECT
    SUM(IF(mal_id IS NULL, 1, 0)) AS nulos_mal_id,
    SUM(IF(estudio_id IS NULL, 1, 0)) AS nulos_estudio_id
FROM
    anime_estudios;

-- Nose encontraron valores nulos en las tablas cargadas

-- --------------------------------------------------------------------------------------------------------------------------------------------------
-- Identificación de valores faltantes en tabla anime(valores N/A en string o text y valores 0 en int o float)
SELECT
	SUM(IF(mal_id IS NULL, 1, 0)) AS Faltantes_mal_id,
    SUM(IF(titulo = 'N/A', 1, 0)) AS Faltantes_titulo,
    SUM(IF(tipo = 'N/A', 1, 0)) AS Faltantes_tipo,
    SUM(IF(episodios = 9999, 1, 0)) AS Faltantes_episodios,
    SUM(IF(annio = 0, 1, 0)) AS Faltantes_annio,
    SUM(IF(temporada = 'N/A', 1, 0)) AS Faltantes_temporada,
    SUM(IF(clasificacion = 'N/A', 1, 0)) AS Faltantes_clasificación,
    SUM(IF(duracion = 'N/A', 1, 0)) AS Faltantes_duración,
    SUM(IF(sinopsis = 'N/A', 1, 0)) AS Faltantes_sinopsis,
    SUM(IF(anime_rank = 9999, 1, 0)) AS Faltantes_anime_rank
FROM
	animes;
-- Se identificaron varias columnas con valores faltnates 'N/A' y valores '0'.
-- Las columnmas que se sabe que se imputaron con N/A y 0 y que coinciden con las obtendidas en la consulta:
-- Imputación 'annio': Nulos rellenados con '0' - cantidad encontrada: 8769
-- Imputado 'tipo': Nulos rellenados con 'N/A' - cantidad encontrada: 1
-- Imputado 'episodios': Nulos rellenados con '9999' - cantidad encontrada: 29
-- Imputado 'temporada': Nulos rellenados con 'N/A' - cantidad encontrada: 8769
-- Imputado 'clasificacion': Nulos rellenados con 'N/A' - cantidad encontrada: 155
-- Imputado 'sinopsis': Nulos rellenados con 'N/A' - cantidad encontrada: 293
-- Imputado 'anime_rank': Nulos rellenados con '9999' - cantidad encontrada: 1865
-- Las columnas con valores faltantes coinciden con las columnas imputadas

-- Identificación de valores faltantes en tabla genero(valores N/A en string o text y valores 0 en int o float)
SELECT
	SUM(IF(genero_id IS NULL, 1, 0)) AS Faltantes_genero_id,
    SUM(IF(nombre_genero = 'N/A', 1, 0)) AS Faltantes_nombre_genero
FROM
	generos;
    
-- Identificación de valores faltantes en tabla estudios(valores N/A en string o text y valores 0 en int o float)
SELECT
	SUM(IF(estudio_id IS NULL, 1, 0)) AS Faltantes_estudio_id,
    SUM(IF(nombre_estudio = 'N/A', 1, 0)) AS Faltantes_nombre_estudio,
    SUM(IF(favoritos = 9999, 1, 0)) AS Faltantes_favoritos,
    SUM(IF(establecido = '2261-12-31', 1, 0)) AS Faltantes_establecido
FROM
	estudios;

-- La columna establecido coincide con la columna imputa en el ETL con la cantidad de 1333 valores faltes/imputados 
    
SELECT
	SUM(IF(mal_id IS NULL, 1, 0)) AS Faltantes_mal_id,
    SUM(IF(score = 9999, 1, 0)) AS Faltantes_scored_by,
    SUM(IF(scored_by = 9999, 1, 0)) AS Faltantes_score_by,
    SUM(IF(miembros = 9999, 2, 0)) AS Faltantes_miembros,
    SUM(IF(favoritos = 9999, 1, 0)) AS Faltantes_favoritos,
    SUM(IF(popularidad = 9999,1,0)) AS Faltantes_popularidad
FROM
	popularidad;
-- La columna socre, scored_by coinciden con la columnas imputadas en el ETL con 1266 y 1266 correspondiente.
-- La columna popularidad cuenta con 1 registro imputado lo que es raro ya que en el ETL no muestra que la columna popularidad fue imputado.