class Horario:
    def __init__(self, Descricao: str, HoraInicio: str, HoraFim: str):
        self.__idHorario = None
        self.__Descricao = Descricao
        self.__HoraInicio = HoraInicio
        self.__HoraFim = HoraFim

    def __str__(self):
        return f"Horario [ID: {self.__idHorario} | Descrição: {self.__Descricao} | Início: {self.__HoraInicio} | Fim: {self.__HoraFim}]"


    @property
    def idHorario(self):
        return self.__idHorario

    @property
    def Descricao(self):
        return self.__Descricao

    @property
    def HoraInicio(self):
        return self.__HoraInicio

    @property
    def HoraFim(self):
        return self.__HoraFim