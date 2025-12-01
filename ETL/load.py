import mysql.connector


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
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f'Base de datos seleccionada {db_name}')
except mysql.connector.Error as e:
    print(f'Error al conectar a MySQL {e}')
finally:
    if connection is not None and connection.is_connected():
        connection.close()
        print('Conexión cerrada')