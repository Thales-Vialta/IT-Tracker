class Horario:
    def __init__(self, Descricao: str, HoraInicio: str, HoraFim: str):
        self.idHorario = None
        self.Descricao = Descricao
        self.HoraInicio = HoraInicio
        self.HoraFim = HoraFim

    def __str__(self):
        return f"Horario [ID: {self.idHorario} | Descrição: {self.Descricao} | Início: {self.HoraInicio} | Fim: {self.HoraFim}]"