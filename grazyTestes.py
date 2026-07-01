from repositories.alocacaoRepository import repoAlocacao
from services.alocacaoService import alocacaoService
from services.userService import userService
from services.salaService import salaService

# aloca = repoAlocacao.listar_alocacoes()
# for i in aloca:
#     print(i)
#     print()

# print(alocacaoService.cadastrarAlocacao('2026-07-01 00:00:00','2026-07-01 10:30:00',[13,14,15], 'Malena 0202', 'Sala do Mine'))

"""print(alocacaoService.listarAlocacao())


print(userService.buscaUsuario('Malena 0202'))"""

# Exemplo: Mudando os aparelhos da Alocação ID 14 para os aparelhos 1, 5 e 10
print(alocacaoService.editarAlocacao(14, 'Usuario', 'Lola'))