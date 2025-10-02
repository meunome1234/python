#classe Data com dia, mes e ano de objeto
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        #objeto para representar a data de nascimento
        self.data_nascimento = f"{self.dia}/{self.mes}/{self.ano}"
# usuario 2--------------------------------------------------------
class Data2:
    def __init__(self, dia2, mes2, ano2):
        self.dia2 = dia2
        self.mes2 = mes2
        self.ano2 = ano2
        #objeto para representar a data de nascimento
        self.data_nascimento2 = f"{self.dia2}/{self.mes2}/{self.ano2}"

