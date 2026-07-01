class HorarioFuncionamento:
    def __init__(self, horaAbertura: int, horaFechamento: int, desc: str):
        # Atributos protegidos do modelo
        self._horaAbertura = horaAbertura
        self._horaFechamento = horaFechamento
        self._descricao = desc

    # --- GETTERS PADRÃO ---

    @property
    def horaAbertura(self) -> int:
        return self._horaAbertura

    @property
    def horaFechamento(self) -> int:
        return self._horaFechamento

    @property
    def descricao(self) -> dict:
        return self._descricao

