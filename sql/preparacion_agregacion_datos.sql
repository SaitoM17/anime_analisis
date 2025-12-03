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
