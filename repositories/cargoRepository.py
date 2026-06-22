from dbConnector.Database import DatabaseConnector
from models.cargos import *

class CargoRepository:

    def listarUsuarios():
        conn = DatabaseConnector().get_connection()
        try: 
            cursor = conn.cursor()
            cursor.execute('''Select * from Cargo Order by Cargos''')
            resultado = cursor.fetchall()
            return resultado
        except ValueError: 
                print("Erro! Nome vazio")
        finally:
                cursor.close()
                conn.close()

    def buscarCargoPorId(cargo:str):
          pass

repo = CargoRepository()