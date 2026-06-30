from services.horarioService import horarioService

from repositories.horarioRepository import horarioRepo
from repositories.alocacaoRepository import AlocacaoRepository
from services.StatusService import statusServ
from repositories.statusRepository import repo
# print(horarioService.HorarioFuncExiste())

# print(statusServ.listar_status())


# dados_horario = horarioService.buscarHorario('Horario de Funcionamento')
# print(dados_horario)

# # 2. Trata e formata esses dados
# horario_formatado = horarioService.tratarHorario(dados_horario)

# 3. Exibe o resultado final
# print(horarioService.intervaloValido('09:00','17:31'))

'''horario = horarioService.buscarHorario('Intervalo teste')
print(horarioService.tratarHorario(horario))

print(horarioService.intervaloExiste('08:00:00','17:30:00'))'''


'''status_service = StatusService(repo)

print(repo.Listar_Aparelhos_Status())'''

Alocacation_service = AlocacaoRepository()

resposta = Alocacation_service.Listar_Alocacao_Gap_Data("2026-06-01 08:00:00","2026-06-02 17:30:00")



print(Alocacation_service.inserir_Alocacao(13,50,20,'2026-06-13 09:10:00','2026-06-14 16:50:00'))

print(Alocacation_service.Listar_Alocacao())

print(Alocacation_service.Aparelhos_menos_Alocados())

print(Alocacation_service.Buscar_Alocacao(20))

print(Alocacation_service.Editar_Alocacao(13,50,20,'2026-06-13 09:10:00','2026-06-14 16:50:00',1))

print(Alocacation_service.Deletar_Alocacao(20))