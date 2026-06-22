from dbConnector.Database import DatabaseConnector
from models.cargos import *

# ELE DEVERIA LISTAR OS CARGOS (CORRIGI NO TRELLO)

# class CargoRepository:

#     def inserir_cargo(self, cargo):
#         conn = DatabaseConnector().get_connection()

#         try:
#             cursor = conn.cursor()

#             cursor.execute("""
#                 INSERT INTO Cargo
#                 (Cargos)
#                 VALUES (%s)
#             """,
#             (
#                 cargo.Desc_cargo
#             ))

#             conn.commit()

#         finally:
#             cursor.close()
#             conn.close()

