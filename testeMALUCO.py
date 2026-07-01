from services.horarioService import horarioService
from services.alocacaoService import AlocacacaoService
from repositories.alocacaoRepository import repoAlocacao
from services.salaService import salaService
from services.userService import userService
# =====================================================================
# 1. INSTANCIANDO AS DEPENDÊNCIAS REAIS (Ou simuladas pro teste rodar)
# =====================================================================
class ObjetoSalaExemplo:
    def buscabuscarSalas(self, sala):
        print(f"-> [Método interno da Sala] Buscando dados da sala: {sala}")
        return f"Objeto_Sala_{sala}_Pronto"

# Instanciando o seu serviço exatamente como você faria no sistema
# (Certifique-se de que repoAlocacao, salaService e userService já foram instanciados antes)
alocacaoServ = AlocacacaoService(repoAlocacao, salaService, userService)# Simulando o comportamento de 'sala' que seu método 'cadastrarAlocacao' exige


print("\n" + "="*50)
print("             INICIANDO TESTES MANUAIS")
print("="*50 + "\n")


print("\n--- [TESTE 1] Cadastrar Alocação ---")
try:
    # Garanta que está passando a lista de aparelhos com os colchetes []
    alocacaoServ.cadastrarAlocacao(
        data_hora_inicio="2026-06-30 14:00:00",
        data_hora_fim="2026-06-30 18:00:00",
        listIDs_aparelho=[114],  # Sempre em formato de lista []
        user=30,                 # ID numérico do usuário do seu banco
        sala=358                 # ID numérico da sala do seu banco
    )
    print("✔ Alocação enviada com sucesso!")
except Exception as e:
    print(f"❌ Erro ao cadastrar: {e}")
# =====================================================================
# TESTE 2: LISTAR ALOCAÇÕES
# =====================================================================
print("\n--- [TESTE 2] Listar Alocações ---")
try:
    # Esse método vai direto no banco/repositório e printa na tela
    alocacaoServ.listarAlocacao()
except Exception as e:
    print(f"❌ Erro ao listar: {e}")


# =====================================================================
# TESTE 3: BUSCAR ALOCAÇÃO
# =====================================================================
# --- [TESTE 3] Buscar Alocação ---
print("\n--- [TESTE 3] Buscar Alocação ---")
try:
    # Garanta que essas duas linhas abaixo tenham 4 espaços extras de indentação!
    resultado = alocacaoServ.buscarAlocacao(id_alocacao=304, usuario="Eduardo Lima Vorcaro")
    print(resultado)
except Exception as e:
    print(f"❌ Erro ao buscar: {e}")


# =====================================================================
# TESTE 4: EDITAR ALOCAÇÃO
# =====================================================================
print("\n--- [TESTE 4] Editar Alocação ---")
try:
    # Testando edição simples (Cai no bloco 'else' do seu método)
    alocacaoServ.editarAlocacao(id=2, atributo="idSala", valor="50")
    print("✔ Edição executada!")
except Exception as e:
    print(f"❌ Erro ao editar: {e}")


# =====================================================================
# TESTE 5: REMOVER ALOCAÇÃO
# =====================================================================
print("\n--- [TESTE 5] Remover Alocação ---")
try:
    alocacaoServ.removerAlocacao(id_alocacao=1)
    print("✔ Remoção executada!")
except Exception as e:
    print(f"❌ Erro ao remover: {e}")

print("\n" + "="*50)
print("                 FIM DOS TESTES")
print("="*50)