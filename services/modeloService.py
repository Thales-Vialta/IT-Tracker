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
        
    def cadastrarModelo(self, marca, modelo):
        validacao = self.validarModelo(modelo)

        if not validacao:
            return " já cadastrado!"
        else:
            self.modeloReposit.inserir_Modelo(marca, modelo)

            return " cadastrado com sucesso!"
        
    def listarModelos(self):
        listaModelos = self.modeloReposit.listar_Modelos()

        return listaModelos
    
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
    

    


        
modeloServ = ModeloService(modeloRepo)
    

           