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
    SUM(IF(titulo_ingles = 'N/A', 1, 0)) AS Faltantes_titulo_ingles,
    SUM(IF(titulo_japones = 'N/A', 1, 0)) AS Faltantes_titulo_japones,
    SUM(IF(tipo = 'N/A', 1, 0)) AS Faltantes_tipo,
    SUM(IF(episodios = 0, 1, 0)) AS Faltantes_episodios,
    SUM(IF(annio = 0, 1, 0)) AS Faltantes_annio,
    SUM(IF(temporada = 'N/A', 1, 0)) AS Faltantes_temporada,
    SUM(IF(clasificacion = 'N/A', 1, 0)) AS Faltantes_clasificación,
    SUM(IF(duracion = 'N/A', 1, 0)) AS Faltantes_duración,
    SUM(IF(sinopsis = 'N/A', 1, 0)) AS Faltantes_sinopsis,
    SUM(IF(anime_rank = 0, 1, 0)) AS Faltantes_anime_rank
FROM
	animes;
-- Se identificaron varias columnas con valores faltnates 'N/A' y valores '0'.
-- Las columnmas que se sabe que se imputaron con N/A y 0 son:
-- 'titulo_ingles': Nulos rellenados con 'N/A'
-- 'episodios': Nulos rellenados con 0
-- 'annio': Nulos rellenados con 0
-- 'temporada': Nulos rellenados con 'N/A'
-- El resto de columnas se revisara para identificar los posibles errores.

-- Identificación de valores faltantes en tabla genero(valores N/A en string o text y valores 0 en int o float)
SELECT
	SUM(IF(genero_id IS NULL, 1, 0)) AS Faltantes_genero_id,
    SUM(IF(nombre_genero = 'N/A', 1, 0)) AS Faltantes_nombre_genero
FROM
	generos;
    
-- Identificación de valores faltantes en tabla estudios(valores N/A en string o text y valores 0 en int o float)
SELECT
	SUM(IF(estudio_id IS NULL, 1, 0)) AS Faltantes_estudio_id,
    SUM(IF(nombre_estudio LIKE '%N/A%', 1, 0)) AS Faltantes_nombre_estudio,
    SUM(IF(favoritos = 0, 1, 0)) AS Faltantes_favoritos,
    SUM(IF(establecido IS NULL, 1, 0)) AS Faltantes_establecido
FROM
	estudios;
-- Los valores que aparecen como faltantes en la columna favoritos no son faltantes(ya que esta columna registra los usuarios que han marco el anime como favoritos).
-- Los valores faltantes en la columna establecido es por falta de año (de cuanto se fundaron)
    
SELECT
	SUM(IF(mal_id IS NULL, 1, 0)) AS Faltantes_mal_id,
    SUM(IF(score = 0, 1, 0)) AS Faltantes_scored_by,
    SUM(IF(scored_by = 0, 1, 0)) AS Faltantes_score_by,
    SUM(IF(favoritos = 0, 1, 0)) AS Faltantes_favoritos,
    SUM(IF(popularidad = 0,1,0)) AS Faltantes_popularidad
FROM
	popularidad;