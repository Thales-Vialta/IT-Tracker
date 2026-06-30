from views.cores import CORES
from views.limparTela import limpar_tela

from repositories.marcaRepository import marcaRepo  # Supondo que este será o nome do arquivo futuramente
from datetime import datetime

class MarcaService:

    def __init__(self, marcaRepo):
        self.marcaReposit = marcaRepo

    def validarMarca(self, marca):
        # Se buscar e não encontrar nada (lista vazia), a marca não existe e está validada (Disponível)
        if not self.marcaReposit.buscar_Marca(marca):
            return True
        else:
            # Se encontrar algo, a marca já existe no sistema
            return False
        
    def cadastrarMarca(self, marca):
        validacao = self.validarMarca(marca)

        if not validacao:
            return " já cadastrada!"
        else:
            self.marcaReposit.inserir_Marca(marca)
            return " cadastrada com sucesso!"
        
    def listarMarcas(self):
        limpar_tela()
        listaMarcas = self.marcaReposit.listar_Marcas()

        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- MARCAS CADASTRADAS ----\n\n{CORES['RESET']}"

        if not listaMarcas:
            return resultado + "Nenhuma marca cadastrada.\n"

        for numero, marca_item in enumerate(listaMarcas, start=1):
            id_marca = marca_item[0]
            nome_marca = marca_item[1]

            num_format = f"{numero}.".ljust(4)
            nome_format = nome_marca.ljust(30)

            resultado += (
                f"{CORES['AMARELO']}{CORES['NEGRITO']}{num_format}{CORES['RESET']} "
                f"ID: {str(id_marca).ljust(4)} | "
                f"{nome_format}\n"
            )
            
        return resultado

        
    def buscarMarca(self, marca):
        marcaBuscada = self.marcaReposit.buscar_Marca(marca)
        return marcaBuscada
    
    def removerMarca(self, marca):
        marca_encontrada = self.buscarMarca(marca)

        if not marca_encontrada:
            return " não encontrada ou erro ao remover!"

        id_marcaTratado = marca_encontrada[0][0]

        if not id_marcaTratado:
            return "ID inválido!"

        try:
            sucesso = self.marcaReposit.excluir_Marca(id_marcaTratado)
            
            if sucesso == True:
                return " removida com sucesso!"
            elif sucesso == "vinculado":
                # Tratamento caso a marca possua modelos vinculados a ela na FK do banco
                return " não pode ser removida pois está vinculada a um modelo ou aparelho!"
            else:
                return " não encontrada ou erro ao remover!"
                
        except Exception as e:
            print(f"Erro no serviço ao remover marca: {e}")
            return " Erro interno ao processar a remoção!"
    
    def editarMarca(self, marca_antiga: str, atributo: str, valor: str):
        marca_encontrada = self.buscarMarca(marca_antiga)
        
        if not marca_encontrada:
            return "Marca não encontrada!"
        
        id_marcaTratado = marca_encontrada[0][0]

        try:
            self.marcaReposit.Editar_Marca(id_marcaTratado, atributo, valor)
            return f"Marca editada com sucesso!"
            
        except Exception as e:
            print(f"Erro no serviço ao editar marca: {e}")
            return "Erro interno ao processar a edição!"

# Instanciação automática pronta utilizando o repositório (quando ele for criado)
marcaServ = MarcaService(marcaRepo)