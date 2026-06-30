from repositories.aparelhosRepository import repo

aparelhosDisp = repo.Listar_Aparelhos_Disponiveis()

for id_ap, patrimonio, marca, modelo in aparelhosDisp:
    print(f"ID: {id_ap} | Pat: {patrimonio} | {marca} - {modelo}")
print()