from dbConnector.Database import DatabaseConnector
from models.cargos import *

class CargoRepository:

    def listarCargos(self):
        conn = DatabaseConnector().get_connection()
        try: 
            with conn.cursor() as cursor:
                cursor.execute('''Select * from Cargo Order by Cargos''')
                resultado = cursor.fetchall()
                return resultado
        except Exception as e: 
                print("Erro! ",e)
        finally:
                conn.close()

    def buscarIdCargo(self, cargo: str):
            conn = DatabaseConnector().get_connection()
            try: 
                with conn.cursor() as cursor:
                    cursor.execute('''SELECT ID_Cargo FROM Cargo WHERE Cargos = %s''', (cargo,))
                    resultado = cursor.fetchall()
                    return resultado if resultado else None
            except ValueError: 
                print("Erro! Nome vazio")
            except Exception as e: 
                print("Erro! ",e)
            finally:
                conn.close()

repo = CargoRepository()
