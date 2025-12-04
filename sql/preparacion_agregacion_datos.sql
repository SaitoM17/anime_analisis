-- Realizaremos unas consultas para ir familiarizandos con la base de datos

-- Conocer la tendencias generales

-- Promedio general por año
SELECT
	ani.annio annio,
	ROUND(AVG(pop.score), 2) Promedio
FROM
	popularidad pop
JOIN 
	animes ani ON pop.mal_id = ani.mal_id
GROUP BY 
	ani.annio
ORDER BY
	annio DESC;

-- En los últimos años(20 años) el promedio de score por año es de 6, lo que nos puede dar a entender de que no todos los animes en ese año fueron bien resibidos.

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