from services.horarioService import horarioService

from repositories.horarioRepository import horarioRepo
from repositories.statusRepository import StatusRepository
from services.StatusService import StatusService
from repositories.statusRepository import repo
# print(horarioService.HorarioFuncExiste())

# dados_horario = horarioService.buscarHorario('Horario de Funcionamento')
# print(dados_horario)

# # 2. Trata e formata esses dados
# horario_formatado = horarioService.tratarHorario(dados_horario)

# 3. Exibe o resultado final
# print(horarioService.intervaloValido('09:00','17:31'))

'''horario = horarioService.buscarHorario('Intervalo teste')
print(horarioService.tratarHorario(horario))

print(horarioService.intervaloExiste('08:00:00','17:30:00'))'''


status_service = StatusService(repo)

print(status_service.MudarStatus(2, 15))