from dbConnector.Database import DatabaseConnector
from models.cargos import *

class CargoRepository:

    def listarCargos(self):
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

    def buscarIdCargo(self, cargo: str):
            conn = DatabaseConnector().get_connection()
            try: 
                cursor = conn.cursor()
                cursor.execute('''SELECT idCargo FROM Cargo WHERE Cargos = %s''', (cargo,))
                resultado = cursor.fetchone()
                return resultado[0] if resultado else None
                
            except ValueError: 
                print("Erro! Nome vazio")
            finally:
                cursor.close()
                conn.close()
                
repo = CargoRepository()
