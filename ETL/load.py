import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saito17Jr",
    database="anime"
)

cursor = connection.cursor()