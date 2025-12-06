-- Realizaremos unas consultas para ir familiarizandos con la base de datos

-- # Conocer la tendencias generales

-- 1.-Promedio general por año
SELECT
	ani.annio annio,
	ROUND(AVG(pop.score), 2) Promedio
FROM
	popularidad pop
JOIN 
	animes ani ON pop.mal_id = ani.mal_id
WHERE
	score < 9999
AND
	annio > 0
GROUP BY 
	ani.annio
ORDER BY
	annio DESC;

-- En los últimos años el promedio de score por año es de 6, lo que nos puede dar a entender de que no todos los animes en ese esos años fueron bien recibidos.

-- 2.-Conocer la oferta de anime por año y temporada
SELECT
	annio,
    temporada,
    COUNT(mal_id) as total_animes
FROM
	animes
GROUP BY
	annio,
    temporada
ORDER BY
	annio DESC;
    
-- Se obtuvo la cantidad de animes por año y temporada, las cantidad de algunas temporadas y años no son muy reales ya que
-- algunas muestran solo 1 anime en toal lo cual no es creible que se entre un solo anime por tempora o incluso por año.
-- Esto puede ser una señal de que no hace falta más datos.

-- 3.- Generos top por Decada
WITH rango AS(
	SELECT
		-- Calcula el año de inicio de la década
		FLOOR((CAST(a.annio AS SIGNED) - 2000) / 10) * 10 + 2000 AS Rango_Decenal_Inicio,
		g.nombre_genero,
        COUNT(a.mal_id) AS total_animes_por_genero
	FROM
		animes a
	INNER JOIN anime_generos ag
		ON a.mal_id = ag.mal_id
	INNER JOIN generos g
		ON ag.genero_id = g.genero_id
	WHERE 
		annio >= 1960
	GROUP BY
		Rango_Decenal_Inicio,
        g.nombre_genero
),
RankedGenres AS (
    SELECT
        *,
        -- 2. Clasificar los géneros DENTRO de cada década (PARTITION BY)
        -- RANK() asigna el mismo rango en caso de empate de conteo.
        RANK() OVER (
            PARTITION BY 
                Rango_Decenal_Inicio
            ORDER BY 
                Total_Animes_Por_Genero DESC -- Ordena por el conteo (mayor a menor) para el top
        ) AS rank_por_decada
    FROM
        rango
)
SELECT
    Rango_Decenal_Inicio AS Década,
    nombre_genero AS Género,
    Total_Animes_Por_Genero AS Conteo
FROM
    RankedGenres
WHERE
    -- 3. Filtrar para mostrar solo el Top 10 de cada década
    rank_por_decada <= 10
ORDER BY
    Rango_Decenal_Inicio DESC,
    Conteo DESC;

-- Con los resultados obtenido nos damos una idea de los generos más visto en cada decada.

-- # Calidad y popularidad

-- 1.-Ranking de genero por popularidad
SELECT
	g.nombre_genero,
	ROUND(AVG(p.score), 2) promedio_score
FROM
	animes a
INNER JOIN	popularidad p
	ON a.mal_id = p.mal_id
INNER JOIN anime_generos ag
	ON a.mal_id = ag.mal_id
INNER JOIN generos g
	ON ag.genero_id = g.genero_id
GROUP BY
	g.nombre_genero
ORDER BY
	promedio_score DESC;

-- Se observa que el genero de anime Suspense es el principal con un promedio de 7.1 de score, también se muestra el genero "Award Winning" con 7.1, 
-- como tal este no es un genero de anime sino una descripción o criterio de selección ya que este "genero" son de animes que han gando premedio, se tendria que considerar si se incluirlo
-- en el ranking de generos por popularidad o excluirlo ya que como tal no es un genero.

-- 2.-Generos dominantes por decada
WITH rango AS(
	SELECT
		-- Calcula el año de inicio de la década
		FLOOR((CAST(a.annio AS SIGNED) - 2000) / 10) * 10 + 2000 AS Rango_Decenal_Inicio,
		g.nombre_genero,
        COUNT(a.mal_id) AS total_animes_por_genero
	FROM
		animes a
	INNER JOIN anime_generos ag
		ON a.mal_id = ag.mal_id
	INNER JOIN generos g
		ON ag.genero_id = g.genero_id
	WHERE 
		annio >= 1960
	GROUP BY
		Rango_Decenal_Inicio,
        g.nombre_genero
),
RankedGenres AS (
    SELECT
        *,
        -- 2. Clasificar los géneros DENTRO de cada década (PARTITION BY)
        -- RANK() asigna el mismo rango en caso de empate de conteo.
        RANK() OVER (
            PARTITION BY 
                Rango_Decenal_Inicio
            ORDER BY 
                Total_Animes_Por_Genero DESC -- Ordena por el conteo (mayor a menor) para el top
        ) AS rank_por_decada
    FROM
        rango
)
SELECT
    Rango_Decenal_Inicio AS Década,
    nombre_genero AS Género,
    Total_Animes_Por_Genero AS Conteo
FROM
    RankedGenres
WHERE
    -- 3. Filtrar para mostrar solo el Top 10 de cada década
    rank_por_decada <= 1
ORDER BY
    Rango_Decenal_Inicio DESC,
    Conteo DESC;
    
-- La consulta nos muestra que el genero de comedia es el que más aparace en lo largo de las decadas, esto nos dice que el mayoria de los animes el genero de comedia estya presente.

-- # Desempeño de estudios

-- 1.-ranking de estudios
SELECT
	e.nombre_estudio,
	ROUND(AVG(p.score), 2) AS promedio_score
FROM
	animes a
INNER JOIN anime_estudios ae
	ON a.mal_id = ae.mal_id
INNER JOIN estudios e
	ON ae.estudio_id = e.estudio_id
INNER JOIN popularidad p
	ON p.mal_id = a.mal_id
GROUP BY
	e.nombre_estudio
ORDER BY
	promedio_score DESC;
    
-- La consutla nos muestra el score promedio que han tendio en base a los animes producidos, en dicha consulta tambien aparecen estudios que no tiene 
-- un score posiblemente esto se deba a la falta de datos.

-- 2.-producción por año
SELECT
	a.annio,
    e.nombre_estudio,
    COUNT(a.mal_id) AS cant_producida
FROM
	animes a
INNER JOIN anime_estudios ae
	ON a.mal_id = ae.mal_id
INNER JOIN estudios e
	ON ae.estudio_id = e.estudio_id
GROUP BY
	a.annio,
    e.nombre_estudio
ORDER BY
	a.annio DESC;
    
-- Gracias a la consutla podemos obtener la cantidad de animes producidos por cada estudio en cada año, algunos estudios solo llegan a producir un solo anime por año, esto se puede deber
-- a la tamaño del estudio y no necesariamente a la falta de datos, ya que no se tiene un promedio/cantidad de animes que produce un estudio por año.