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
