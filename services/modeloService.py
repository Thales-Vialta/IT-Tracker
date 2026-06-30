from views.cores import CORES
from views.limparTela import limpar_tela

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
            self.modeloReposit.inserir_Modelo(idmarca, modelo)

            return " cadastrado com sucesso!"
        
    def listarModelos(self):
        listaModelos = self.modeloReposit.listar_Modelos()

        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- MODELOS CADASTRADOS ----\n\n{CORES['RESET']}"

        if not listaModelos:
            return resultado + "Nenhum modelo cadastrado.\n"

        for numero, modelo_item in enumerate(listaModelos, start=1):
            id_modelo = modelo_item[0]
            marca = modelo_item[1]
            nome_modelo = modelo_item[2]

            num_format = f"{numero}.".ljust(4)
            descricao_format = f"{marca} {nome_modelo}".ljust(18)

            resultado += (
                f"{CORES['AMARELO']}{CORES['NEGRITO']}{num_format}{CORES['RESET']} "
                f"{descricao_format} | "
                f"Marca: {str(id_modelo).ljust(4)}\n"
            )
            
        return resultado
    
    def buscarModelo(self, modelo):
        modeloBuscado = self.modeloReposit.buscar_Modelo(modelo)
        return modeloBuscado
    
    def removerModelo(self, modelo):

        id_modelo = self.buscarModelo(modelo)

        id_modeloTratado = id_modelo[0][0]

        print(id_modeloTratado)

        
        if not id_modeloTratado:
            return "ID inválido!"

        try:

            sucesso = self.modeloReposit.Deletar_Modelo(id_modeloTratado)
            
            if sucesso == True:
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
            print(modelo_encontrado)
            
            if not modelo_encontrado:
                return "Modelo não encontrado!"
            
            id_modeloTratado = modelo_encontrado[0][0]

            try:
                # CORREÇÃO: Colocado na ordem correta que o repositório espera (id, atributo, valor)
                self.modeloReposit.Editar_Modelo(id_modeloTratado, atributo, valor)
                return "Modelo updated!"
                
            except Exception as e:
                print(f"Erro no serviço ao editar modelo: {e}")
                return "Erro interno ao processar a edição!"

    


        
modeloServ = ModeloService(modeloRepo)
    

           