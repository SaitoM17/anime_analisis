-- Identificación de problemas en los datos
SELECT COUNT(*) cantidad_registros_animes FROM animes; -- 12500
SELECT COUNT(*) cantidad_registros_generos FROM generos; -- 78
SELECT COUNT(*) cantidad_registros_estudios FROM estudios; -- 2699
SELECT COUNT(*) cantidad_registros_popularidad FROM popularidad; -- 12500
SELECT COUNT(*) cantidad_registros_anime_generos FROM anime_generos; -- 22431
SELECT COUNT(*) cantidad_registros_anime_estudios FROM anime_estudios; -- 10656