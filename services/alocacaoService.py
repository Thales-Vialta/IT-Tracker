from repositories.alocacaoRepository import repoAlocacao
from services.userService import userService
from services.salaService import salaService

class AlocacacaoService: 
    def __init__(self, repoAlocacao, salaService, userService):
        self.repoAloc = repoAlocacao
        self.salaServ = salaService
        self.userServ = userService

    def cadastrarAlocacao(self,data_hora_inicio, data_hora_fim, qtd_ap, listIDs_aparelho:list, user, sala):

        usuario = self.userServ.buscaUsuario(user)
        salaFinal = sala.buscabuscarSalas(sala)

        for i in range(qtd_ap-1):
            self.repoAloc.inserir_Alocacao(usuario,listIDs_aparelho[i],salaFinal,data_hora_inicio,data_hora_fim)
        
   

    def listarAlocacao(self):
        alocacoes = self.repoAloc.Listar_Alocacao()

        print("\n======================= RELATÓRIO DE ALOCAÇÕES =======================")

        for registro in alocacoes:
            # Desempacota cada coluna na ordem exata do seu SELECT
            _, usuario, patrimonio, marca, modelo, sala, dt_alocacao, dt_devolucao = registro
            
            # Formata uma linha única e organizada para cada registro
            print(f"Alocação #{usuario} | Sala: {sala}")
            print(f"  └─ Disp: [{patrimonio}] {marca} {modelo}")
            print(f"  └─ Período: {dt_alocacao} até {dt_devolucao}")
            print("-" * 70) 

        print("======================================================================")

        pass

    def buscarAlocacao(self, usuario):
        validacao = self.repoAloc.Buscar_Alocacao(id)
        texto_retorno = f"=================== RESULTADO DA BUSCA (ID: {id}) ===================\n"

        if not validacao:
            texto_retorno = "Nenhuma alocação encontrada com este ID.\n"
        else:
            for alocacao in validacao:
                id_alocacao, id_aparelho, id_usuario, id_sala, data_alocacao, data_devolucao = alocacao
                
                texto_retorno += f"Alocação: {usuario}\n"
                texto_retorno += f"  ├─ ID do Usuário:  {id_usuario}\n"
                texto_retorno += f"  ├─ ID do Aparelho: {id_aparelho}\n"
                texto_retorno += f"  ├─ ID da Sala:     {id_sala}\n"
                texto_retorno += f"  ├─ Data Início:    {data_alocacao}\n"
                texto_retorno += f"  └─ Data Devolução: {data_devolucao}\n"
                texto_retorno += "-" * 60 + "\n"

            texto_retorno += "===================================================================="
            
            return texto_retorno

    def editarAlocacao(self,id,atributo,valor,qtd=None):

        if atributo == "Aparelho":
            for i in range(qtd-1):
                self.repoAloc.Editar_Alocacao(id,atributo,valor[i])
        else:
            self.repoAloc.Editar_Alocacao(id,atributo,valor)
          

    def removerAlocacao(self,slaOQvaiPassar):
        self.repoAloc.Deletar_Alocacao(slaOQvaiPassar)



        


        
    
        
alocacaoServ = AlocacacaoService(repoAlocacao)
        