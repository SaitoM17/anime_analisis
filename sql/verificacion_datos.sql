-- Identificación de problemas en los datos
SELECT COUNT(*) cantidad_registros_animes FROM animes; -- 12500
SELECT COUNT(*) cantidad_registros_generos FROM generos; -- 78
SELECT COUNT(*) cantidad_registros_estudios FROM estudios; -- 2699
SELECT COUNT(*) cantidad_registros_popularidad FROM popularidad; -- 12500
SELECT COUNT(*) cantidad_registros_anime_generos FROM anime_generos; -- 22431
SELECT COUNT(*) cantidad_registros_anime_estudios FROM anime_estudios; -- 10656

-- Identificación de valores nulos en tabla animes
SELECT
    SUM(IF(mal_id IS NULL, 1, 0)) AS nulos_mal_id,
    SUM(IF(titulo IS NULL, 1, 0)) AS nulos_titulo,
    SUM(IF(titulo_ingles IS NULL, 1, 0)) AS nulos_titulo_ingles,
    SUM(IF(titulo_japones IS NULL, 1, 0)) AS nulos_titulo_japones,
    SUM(IF(tipo IS NULL, 1, 0)) AS nulos_tipo,
    SUM(IF(episodios IS NULL, 1, 0)) AS nulos_episodios,
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