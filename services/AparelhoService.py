from views.limparTela import limpar_tela
from views.cores import CORES
from repositories.aparelhosRepository import repoAp
from models.aparelhos import Aparelhos

class AparelhoService:

    def __init__(self, aparelho_repository):
        self.aparelho_repo = aparelho_repository

    def aparelho_existe(self,idAparelho: int ):
        if not self.aparelho_repo.Buscar_Aparelho(idAparelho):
            return False    
        else:
            return True

    def cadastrar_aparelho(self, serial:str,idStatus:int,idModelo:int):
        if not serial.strip():
            return "Erro: O número de patrimônio/serial não pode ser vazio!"
        if self.aparelho_existe(serial):
            return f"Erro: Aparelho com patrimônio '{serial}' já cadastrado!"
        
        novo_aparelho = Aparelhos(serial, idStatus,idModelo)
        patrimonio = novo_aparelho.serial
        status = novo_aparelho.statusAparelho
        id = novo_aparelho.idModelo

        self.aparelho_repo.inserir_aparelho(patrimonio, status, id)
        return "Aparelho cadastrado com sucesso!"

    def listar_aparelhos(self): 
        limpar_tela()
        aparelhos = self.aparelho_repo.Listar_Todos_Aparelhos()

        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- TODOS DISPOSITIVOS CADASTRADOS ----\n\n{CORES['RESET']}"

        if not aparelhos:
            return resultado + "Nenhum aparelho cadastrado.\n"

        for numero, aparelho in enumerate(aparelhos, start=1):
            id_aparelho = aparelho[0]
            patrimonio = aparelho[1]
            marca = aparelho[2]
            modelo = aparelho[3]

            num_format = f"{numero}.".ljust(4)
            patrimonio_format = patrimonio.ljust(20)
            descricao_format = f"{modelo} ({marca})".ljust(30)

            resultado += (
                    f"{CORES['AMARELO']}{CORES['NEGRITO']}{num_format}{CORES['RESET']} "
                    f"ID: {str(id_aparelho).ljust(4)} | "
                    f"Modelo: {descricao_format} | "
                    f"Patrimônio: {patrimonio_format}\n"                    
                )
            
        return resultado

    def buscar_aparelho_por_id(self, id_aparelho: int):
        aparelho = self.aparelho_repo.Buscar_Aparelho(id_aparelho)
        if not aparelho:
            print("Aparelho não encontrado!")
        return aparelho

    def exibir_aparelho_mais_utilizado(self):
        dados = self.aparelho_repo.aparelho_mais_utilizado()
        if not dados:
            return f"{CORES['VERMELHO']}Nenhum dado de alocação encontrado.{CORES['RESET']}"
            
        patrimonio, marca, modelo = dados
        return (f"{CORES['VERDE']}{CORES['NEGRITO']} APARELHO MAIS UTILIZADO \nPatrimônio: {patrimonio} | Modelo: {marca} {modelo}{CORES['RESET']}\n")
    def serial_ja_cadastrado(self, serial: str) -> bool:
       
        return bool(self.aparelho_repo.Buscar_Por_Serial(serial))
    def atualizar_aparelho(self, id_aparelho: int, novo_serial: str, novo_id_modelo: int):
        aparelho_atual = self.aparelho_repo.Buscar_Aparelho(id_aparelho)
        
        if not aparelho_atual:
            return "Erro: Aparelho não encontrado para atualização!"
        serial_antigo = aparelho_atual[1] 

        if novo_serial != serial_antigo and self.serial_ja_cadastrado(novo_serial):
            return f"Erro: O patrimônio '{novo_serial}' já está em uso por outro aparelho!"
        sucesso = self.aparelho_repo.Editar_Aparelho(novo_serial, novo_id_modelo, id_aparelho)
        if sucesso:
            return "Aparelho updated com sucesso!"
        return "Erro técnico ao tentar atualizar o aparelho."
    
    def remover_aparelho(self, id_aparelho: int):
        aparelho = self.aparelho_repo.Buscar_Aparelho(id_aparelho)
        if not aparelho:
            return "Erro: Aparelho não encontrado!"

        sucesso = self.aparelho_repo.deletar_aparelho(id_aparelho)
        if sucesso:
            return "Aparelho removido com sucesso!"

        return "Erro: Não foi possível remover o aparelho. Certifique-se de que ele não possui alocações vinculadas."

    def mostra_aparelhos_disponiveis(self, marca=None):
        aparelhosDisp = self.aparelho_repo.Listar_Aparelhos_Disponiveis(marca)
        listaDisp = ''
        for id_ap, patrimonio, marca, modelo in aparelhosDisp:
            listaDisp = f"ID: {id_ap} | Pat: {patrimonio} | {marca} - {modelo}"
        return listaDisp
    
    def validaId_Disponivel(self, marca, id):
        aparelhosDisp = self.aparelho_repo.Listar_Aparelhos_Disponiveis()
        lista_IDs = []
        for id_ap in aparelhosDisp:
            lista_IDs.append(id_ap)

        if id not in lista_IDs:  
            return False   
        else:
            return True
        
aparelhoService = AparelhoService(repoAp)