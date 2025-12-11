#classe Data com dia, mes e ano de objeto
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        #objeto para representar a data de nascimento
        self.data_nascimento = f"{self.dia}/{self.mes}/{self.ano}"


