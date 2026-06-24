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
            cls._connection = cls._criar_nova_conexao()
        return cls._instance

    @staticmethod
    def _criar_nova_conexao():
        """Método auxiliar para centralizar a criação da conexão"""
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    def get_connection(self):
        if self._connection is None or not self._connection.is_connected():
            DatabaseConnector._connection = self._criar_nova_conexao()
        
        return self._connection

db = DatabaseConnector()
conn = db.get_connection()
print(conn)
if conn.is_connected():
    print("Banco conectado!")