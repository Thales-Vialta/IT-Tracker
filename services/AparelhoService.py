from views.limparTela import limpar_tela
from views.cores import CORES
from repositories.aparelhosRepository import repoAp
from models.aparelhos import Aparelhos

class AparelhoService:

    def __init__(self, repoAp):
        self.aparelho_repo = repoAp

    def aparelho_existe(self, idAparelho: int):
        dados = self.aparelho_repo.Buscar_Aparelho(idAparelho)
        
        if not dados or dados == "[]" or len(dados) == 0:
            return False
        return True

    def cadastrar_aparelho(self, serial: str, idStatus: int, idModelo: int):
        if not serial.strip():
            return "Erro: O número de patrimônio/serial não pode ser vazio!"
            
        if self.aparelho_existe(serial):
            return f"Erro: Aparelho com patrimônio '{serial}' já cadastrado!"
        
        self.aparelho_repo.inserir_aparelho(serial, idStatus, idModelo)
        
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
        else:
            return aparelho

    def exibir_aparelho_mais_utilizado(self):
        dados = self.aparelho_repo.aparelho_mais_utilizado()
        if not dados:
            return f"{CORES['VERMELHO']}Nenhum dado de alocação encontrado.{CORES['RESET']}"
            
        patrimonio, marca, modelo = dados
        return (f"{CORES['VERDE']}{CORES['NEGRITO']} APARELHO MAIS UTILIZADO \nPatrimônio: {patrimonio} | Modelo: {marca} {modelo}{CORES['RESET']}\n")
    
    def serial_ja_cadastrado(self, serial: str):
        validacao = self.aparelho_repo.Buscar_Aparelho_Por_Serial(serial)

        if not validacao:
            return False
        else:
            True
    

    def atualizar_aparelho(self, atributo: str, valor, id: int):
        self.aparelho_repo.Editar_Aparelho(atributo,valor,id)
       

    def remover_aparelho(self, id_aparelho: int):
            # Garante que o ID recebido seja convertido para inteiro puro
            id_limpo = int(id_aparelho)
            
            aparelho = self.aparelho_repo.Buscar_Aparelho(id_limpo)
            if not aparelho:
                return "Erro: Aparelho não encontrado!"

            try:
                # Passa o ID numérico perfeitamente limpo
                self.aparelho_repo.Deletar_Aparelho(id_limpo)
                return "Aparelho removido com sucesso!"
                
            except Exception as e:
                print(f"Exceção capturada no service: {e}")
                return "Erro: Não foi possível remover o aparelho. Certifique-se de que ele não possui alocações vinculadas."

    def mostra_aparelhos_disponiveis(self, marca=None):
            aparelhosDisp = self.aparelho_repo.Listar_Aparelhos_Disponiveis(marca)
            
            # Se o banco não trouxer nada, avisa o usuário de forma limpa
            if not aparelhosDisp:
                return "Nenhum aparelho disponível no momento.\n"
                
            listaDisp = ''
            for id_ap, patrimonio, marca_nome, modelo in aparelhosDisp:
                # 🌟 CORRIGIDO: Usando += para acumular e \n para quebrar a linha a cada aparelho
                listaDisp += f"ID: {id_ap} | Pat: {patrimonio} | {marca_nome} - {modelo}\n"
                
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