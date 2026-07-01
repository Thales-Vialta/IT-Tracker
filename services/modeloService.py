from views.cores import CORES
from views.limparTela import limpar_tela

from models.modelo import ModeloAparelho
from repositories.modeloRepository import modeloRepo

class ModeloService:

    def __init__(self, modeloRepo):
        self.modeloReposit = modeloRepo

    def validarModelo(self, modelo):
        if not self.modeloReposit.buscar_Modelo(modelo):
            # Se buscar e não encontrar nada (lista vazia), o modelo não existe e está validado (Disponível)
            return True
        else:
            # Se encontrar algo, o modelo já existe no sistema
            return False
        
    def cadastrarModelo(self, idmarca, modelo):
        validacao = self.validarModelo(modelo)

        if not validacao:
            return " já cadastrado!"
        else:
            modeloObj = ModeloAparelho(idmarca,modelo)
            idMarca = modeloObj.idMarca
            modeloNovo = modeloObj.modelo
            
            self.modeloReposit.inserir_Modelo(idMarca, modeloNovo)

            return " cadastrado com sucesso!"
        
    def listarModelos(self):
        limpar_tela()
        listaModelos = self.modeloReposit.listar_Modelos()

        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- MODELOS CADASTRADOS ----\n\n{CORES['RESET']}"

        if not listaModelos:
            return resultado + "Nenhum modelo cadastrado.\n"

        for numero, modelo_item in enumerate(listaModelos, start=1):
            marca_nome = modelo_item[0]       
            modelo_nome = modelo_item[1]      

            num_format = f"{numero}.".ljust(4)
            modelo_format = f"{modelo_nome}".ljust(20)

            resultado += (
                f"{CORES['AMARELO']}{CORES['NEGRITO']}{num_format}{CORES['RESET']} "
                f"{modelo_format} | "
                f"Marca: {marca_nome}\n"
            )
            
        return resultado
    
    def buscarModelo(self, modelo):
        modeloBuscado = self.modeloReposit.buscar_Modelo(modelo)
        return modeloBuscado
    
    def removerModelo(self, id_modelo_recebido):
        if not id_modelo_recebido:
            return "ID inválido!"

        try:
            sucesso = self.modeloReposit.Deletar_Modelo(id_modelo_recebido)
            
            if sucesso == True or sucesso == 1:
                return " removido com sucesso!"
            elif sucesso == "vinculado":
                return " não pode ser removido pois está vinculado a um aparelho!"
            else:
                return " não encontrado ou erro ao remover!"
                
        except Exception as e:
            print(f"Erro no serviço ao remover modelo: {e}")
            return " Erro interno ao processar a remoção!"
    
    def editarModelo(self, modelo_antigo: str, atributo: str, valor: str):

            modelo_encontrado = self.buscarModelo(modelo_antigo)
            
            if not modelo_encontrado:
                return "Modelo não encontrado!"
            
            id_modeloTratado = modelo_encontrado[0][0]

            try:
                self.modeloReposit.Editar_Modelo(id_modeloTratado, atributo, valor)
                return "Modelo editado com sucesso!"
                
            except Exception as e:
                print(f"Erro no serviço ao editar modelo: {e}")
                return "Erro interno ao processar a edição!"
        
modeloServ = ModeloService(modeloRepo)           