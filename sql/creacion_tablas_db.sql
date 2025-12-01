-- Creación de tablas

-- Tabla: anime
CREATE TABLE anime (
    mal_id INT NOT NULL,
    titulo VARCHAR(500) NOT NULL,
    titulo_english VARCHAR(500),
    titulo_japanese VARCHAR(500),
    tipo VARCHAR(50),
    episodios INT,
    annio YEAR,
    temporada VARCHAR(50),
    clasificacion VARCHAR(100), 
    duration VARCHAR(100),
    sinopsis TEXT,
    anime_rank INT, 
    PRIMARY KEY (mal_id)
);

-- Tabla: generos
CREATE TABLE generos (
    genero_id INT NOT NULL,
    nombre_genero VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (genero_id)
);

-- Tabla: estudios
CREATE TABLE estudios (
    estudio_id INT NOT NULL,
    nombre_estudio VARCHAR(255) UNIQUE NOT NULL,
    favoritos INT,
    establecido YEAR,
    PRIMARY KEY (estudio_id)
);

-- Tabla: popularidad
CREATE TABLE popularidad (
    mal_id INT NOT NULL,
    score FLOAT,
    scored_by INT,
    miembros INT, 
    favoritos INT,
    popularidad INT,
    
    PRIMARY KEY (mal_id),
    
    -- Relación: Un anime tiene una única fila de métricas
    FOREIGN KEY (mal_id) REFERENCES anime(mal_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Tablas de asociación (Muchos a Muchos)

-- Tabla de asociación: anime_generos
CREATE TABLE anime_generos (
    mal_id INT NOT NULL,
    genero_id INT NOT NULL,
    
    -- La clave primaria compuesta asegura que una combinación (anime, genero) solo exista una vez
    PRIMARY KEY (mal_id, genero_id),
    
    -- FK al Anime
    FOREIGN KEY (mal_id) REFERENCES anime(mal_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    -- FK al Genero
    FOREIGN KEY (genero_id) REFERENCES generos(genero_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- TABLA DE ASOCIACIÓN: anime_estudios
CREATE TABLE anime_estudios (
    mal_id INT NOT NULL,
    estudio_id INT NOT NULL,
    
    -- La clave primaria compuesta asegura que una combinación (anime, estudio) solo exista una vez
    PRIMARY KEY (mal_id, estudio_id),
    
    -- FK al Anime
    FOREIGN KEY (mal_id) REFERENCES anime(mal_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
        
    -- FK al Estudio
    FOREIGN KEY (estudio_id) REFERENCES estudios(estudio_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);