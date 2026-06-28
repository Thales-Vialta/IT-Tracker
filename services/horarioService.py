from repositories.horarioRepository import horarioRepo

from views.limparTela import limpar_tela
from views.cores import CORES

class horarioService:

    def __init__(self, horario_repository):
        self.horario_repo = horario_repository

    def listarHorarios(self):
        limpar_tela()

        hora = self.horario_repo.Mostrar_Horario()

        resultado = f"{CORES['AZUL']}{CORES['NEGRITO']}---- LISTA DE HOR├üRIOS ----\n\n{CORES['RESET']}"

        for HoraInicio, HoraFim, Descricao in hora:
            inicio_str = str(HoraInicio)
            fim_str = str(HoraFim)
            periodo = f"{inicio_str} - {fim_str}"

            desc_format = Descricao.ljust(30)

            resultado += f"{CORES['AMARELO']}{CORES['NEGRITO']}{desc_format} | {CORES['RESET']} {CORES['RESET']} {periodo}\n"

        return resultado
    
    def validarHorarioFunc(self):
        horarios_cadastrados = self.horario_repo.Listar_Horario()
        
        for HoraInicio, HoraFim, Descricao in horarios_cadastrados:
            if Descricao.strip() == 'Horario de Funcionamento':
                return 'Deseja cadastrar um intervalo?'
                
        return 'Deseja cadastrar o horario de funcionamento?'
    
    def intervaloHora(self):
        pass
        
    
    def criarIntervaloHora(self,desc,inicio,fim):
        self.horario_repo.Inserir_Horario(desc,inicio,fim)
        pass

horarioService = horarioService(horarioRepo)
