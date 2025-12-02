import mysql.connector

def load_animes(df):
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saito17Jr",
            database="anime"
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f'Conexión exitosa a MySQL version:{db_info}')
            print('Conectado a la base de datos')

            cursor = connection.cursor()

            insert_query = """
            INSERT INTO anime(
                mal_id, titulo, titulo_english, titulo_japanese, tipo, episodios, annio, temporada, clasificacion, duracion, sinopsis, anime_rank
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                titulo = VALUES(titulo),
                titulo_ingles = (titulo_ingles),
                titulo_japones = (titulo_japones),
                tipo = (tipo),
                episodios = (episodios),
                annio = (annio),
                temporada = (temporada),
                clasificacion = (clasificacion),
                duracion = (duracion),
                sinopsis = (sinopsis),
                anime_rank = (anime_rank)
            """

            for _, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print(f'Datos de la tabla anime insertados/actualizados con éxito ({df.shape[0]} filas).')

    except mysql.connector.Error as e:
        print(f'Error al conectar a MySQL {e}')
        if connection and connection.is_connected():
            connection.rollback()
            print('Rollback ejecutado.')
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print('Conexión cerrada')

def load_generos(df):
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saito17Jr",
            database="anime"
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f'Conexión exitosa a MySQL version:{db_info}')
            print('Conectado a la base de datos')

            cursor = connection.cursor()

            insert_query = """
            INSERT INTO genros(
                genero_id, nombre_genero
            )
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE
                nombre_genero = VALUES(nombre_genero),
            """

            for _, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print(f'Datos de la tabla anime insertados/actualizados con éxito ({df.shape[0]} filas).')

    except mysql.connector.Error as e:
        print(f'Error al conectar a MySQL {e}')
        if connection and connection.is_connected():
            connection.rollback()
            print('Rollback ejecutado.')
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print('Conexión cerrada')

def load_estudios(df):
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saito17Jr",
            database="anime"
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f'Conexión exitosa a MySQL version:{db_info}')
            print('Conectado a la base de datos')

            cursor = connection.cursor()

            insert_query = """
            INSERT INTO genros(
                estudio_id, nombre_estudio, favoritos, establecido
            )
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                nombre_estudio = VALUES(nombre_estudio),
                favoritos = VALUES(favoritos),
                establecido = VALUES(establecido)
            """

            for _, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print(f'Datos de la tabla anime insertados/actualizados con éxito ({df.shape[0]} filas).')

    except mysql.connector.Error as e:
        print(f'Error al conectar a MySQL {e}')
        if connection and connection.is_connected():
            connection.rollback()
            print('Rollback ejecutado.')
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print('Conexión cerrada')

def load_popularidad(df):
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saito17Jr",
            database="anime"
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f'Conexión exitosa a MySQL version:{db_info}')
            print('Conectado a la base de datos')

            cursor = connection.cursor()

            insert_query = """
            INSERT INTO genros(
                mal_id, score, score_by, miembros, favoritos, popularidad
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                score = VALUES(score),
                score_by = VALUES(score_by),
                miembros = VALUES(miembros),
                favoritos = VALUES(favoritos),
                popularidad = VALUES(popularidad)
            """

            for _, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print(f'Datos de la tabla anime insertados/actualizados con éxito ({df.shape[0]} filas).')

    except mysql.connector.Error as e:
        print(f'Error al conectar a MySQL {e}')
        if connection and connection.is_connected():
            connection.rollback()
            print('Rollback ejecutado.')
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print('Conexión cerrada')

def load_anime_generos(df):
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saito17Jr",
            database="anime"
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f'Conexión exitosa a MySQL version:{db_info}')
            print('Conectado a la base de datos')

            cursor = connection.cursor()

            insert_query = """
            INSERT INTO anime_generos(
                mal_id, genero_id
            )
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE
                genero_id = VALUES(genero_id)
            """

            for _, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print(f'Datos de la tabla anime insertados/actualizados con éxito ({df.shape[0]} filas).')

    except mysql.connector.Error as e:
        print(f'Error al conectar a MySQL {e}')
        if connection and connection.is_connected():
            connection.rollback()
            print('Rollback ejecutado.')
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print('Conexión cerrada')

def load_anime_estudios(df):
    connection = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saito17Jr",
            database="anime"
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f'Conexión exitosa a MySQL version:{db_info}')
            print('Conectado a la base de datos')

            cursor = connection.cursor()

            insert_query = """
            INSERT INTO anime_estudios(
                mal_id, estudio_id
            )
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE
                estudio_id = VALUES(estudio_id)
            """

            for _, row in df.iterrows():
                cursor.execute(insert_query, tuple(row))

            connection.commit()
            print(f'Datos de la tabla anime insertados/actualizados con éxito ({df.shape[0]} filas).')

    except mysql.connector.Error as e:
        print(f'Error al conectar a MySQL {e}')
        if connection and connection.is_connected():
            connection.rollback()
            print('Rollback ejecutado.')
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print('Conexión cerrada')