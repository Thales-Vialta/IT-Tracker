import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

class DatabaseConnector:

    _instance = None
    _connection = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
        return cls._instance
    def get_connection(self):
        return self._connection

db = DatabaseConnector()

conn = db.get_connection()

print(conn)

if conn.is_connected():
    print("Banco conectado!")