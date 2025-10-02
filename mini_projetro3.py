#chama os arquivos de data e financas
from data import Data
from financas import Financas
from pessoa import Pessoa

#parte do miniprojeto2.py
#entrada de dados para formatação
G = '\033[32m' # green - verde
B = '\033[34m' # blue - azul
Y = '\033[33m' # yellow - amarelo
C = '\033[36m' # cyan - ciano
W = '\033[37m' # white - branco
ql = "\n" #quebra de linha
#chatbot assistente financeiro

bot_nome = "din" #nome do chatbot


#fala inicial o chatbot din
 #paragrafo1
print(f"oi, pode me chamar de {B}{bot_nome}{W}!{ql}sou seu assistente financeiro{ql}e vou tentar ajudar com as {C}contas{W} e os {C}objetivos{W}.{ql}")
#paragrafo2 - dados pessoais

print(f"[DADOS PESSOAIS] {ql}") #título dados pessoais
nome = input(f"Primeiro, me diz teu {Y}nome{W}: ")
dia = input(f"Me diz o {Y}dia{W} em que tu nasceu: ")
mes = input(f"Agora o {Y}mês{W}: ")
ano = input(f"E o {Y}ano{W}: ")

print(f"{ql} --- {ql}")# separação ----

print(f"Muito bem, então conferindo seus dados, estou registrando aqui.{ql}{G}{nome}{W}, nascimento em{G} {dia}/{mes}/{ano}{W}{ql}")


print(f"[DADOS FINANCEIROS] {ql}") #título dados financeiros

#paragrafo3 - dados financeiros
patrimonio = input(f"Agora me  informa por favor alguns dados financeiros.{ql}Se você somar o dinheiro que tem guardado, me diz o total desse{Y} patrimônio{W}: R$ ")
salario = input(f"Me diz teu {Y}salário{W}: R$")

#paragrafo4 - gastos mensais
aluguel = input(f"Sobre os seus gastos, me informa por partes po favor.{ql}Quanto custa teu {Y}aluguel{W} (incluindo condomínio e outras taxas): R$ ")
feira = input(f"Mais ou menos o quanto você gasta fazendo {Y}feira{W} todo mês: R$ ")
comida = input(f"E com {Y}comida{W} fora de casa, em média dá quanto: R$ ")
transporte = input(f"Na mobilidade, quanto que gasta com {Y}transporte{W} (ônibus, Uber, gasolina etc): R$ ")
outros = input(f"Pra terminar, quanto você gasta com {Y}outros{W} (lazer, roupas, etc): R$ ")

print(f"--- {ql}")# separação ----

#paragrafo5 - cresumo dos dados
print(f"Obrigado,{G}{nome}{W}, resumindoas informações financeiras até agora.{ql}Os seus gastos discriminados são:")
print(f"{G}Aluguel:{W} R$ {float(aluguel):.2f}")
print(f"{G}Feira{W}: R$ {float(feira):.2f}")
print(f"{G}Comida fora{W}: R$ {float(comida):.2f}")
print(f"{G}Transporte{W}: R$ {float(transporte):.2f}")
print(f"{G}Outros{W}: R$ {float(outros):.2f}") 
#calculo dos gastos totais
gasto_total = float(aluguel)+float(feira)+float(comida)+float(transporte)+float(outros)
print(f"{G}GASTOS TOTAIS{W}: R$ {float(gasto_total):.2f}{ql}")

print(f"--- {ql}")# separação ---- 

#paragrafo6 
#restante do salario
sobra = int(salario) - gasto_total
print(f"Pra terminar, calculando o seu saldo mensal, com base em tos os gastos{ql}e no teu salário, o valor resultante é de {G}{float(sobra):.2f}{W}")
#investimento
investimento = input(f"Desse valor, considerando que qualquer investimento é válido,{ql}o quanto você conseguiria{Y} investir{W} todo mês: R$ ")
#sugestão de investimento
print(f"Ok, anotado, o valor do investimento é de R$ {G}{float(investimento):.2f}{W}.{ql}Acredito que coletei todas as informações necessárias{ql}")

#missão 2 (miniprojeto2)----------------------------

print(f"Agora sim, vamos pensar no futuro! Você tem  um próximo objetivo financeiro?{ql}Um desejo de adquirir ou realizar algo que você quer e que precisa de investimento?")
print(f"Exemplos de objetivos assim são:{ql}Comprar uma moto ou carro, fazer uma viagem, comprar uma casa, fazer um curso, etc,")
objetivo = input(f"Qual seria esse seu próximo {Y}objetivo{W} financeiro: ")
valor_objetivo = input(f"Qual o valor do {Y}objetivo{W} financeiro: R$ ")
print(f"Em uma conta simples que fiz aqui, sem considerar rendimentos ou inflação,{ql}com base na sua capacidade de investimento mensal de{G} R$ {float(investimento):.2f}{W}{ql} e seu patrimônio atual de {G}R$ {float(patrimonio):.2f}{W}")
print(f"Você conseguiria atingir o valor de {G}R$ {float(valor_objetivo):.2f}{W} em:")

#calculo do tempo para atingir o objetivo meses
tempo_objetivo_meses = (float(valor_objetivo) - float(patrimonio)) / float(investimento)
#calculo do tempo para atingir o objetivo anos
tempo_objetivo_anos = tempo_objetivo_meses/12

print(f"{float(tempo_objetivo_meses):.2f} meses")
print(f"Ou {tempo_objetivo_anos} anos")

#mensagem final
print(f"Por hora, é isso que tenho para te ajudar{ql}Espero que tenha sido útil")


#missaão 2 - mini projeto 3 -----------------------------------
#criação dos objetos do usuario (antonieta) do chatbot a partrir dos input
data_nascimento = Data(dia, mes, ano)
financas_usuario = Financas(patrimonio, salario, gasto_total, investimento)
pessoa_usuario = Pessoa(nome, data_nascimento, financas_usuario)

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# usuário2
#repetir o processo para outro usuário

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#fala inicial o chatbot din
 #paragrafo1 - 2º usuário
print(f"{ql} --- {ql}")# separação ----
print(f"oi, pode me chamar de {B}{bot_nome}{W}!{ql}sou seu assistente financeiro{ql}e vou tentar ajudar com as {C}contas{W} e os {C}objetivos{W}.{ql}")
#paragrafo2 - dados pessoais

print(f"[DADOS PESSOAIS] {ql}") #título dados pessoais
nome2 = input(f"Primeiro, me diz teu {Y}nome{W}: ")
dia2 = input(f"Me diz o {Y}dia{W} em que tu nasceu: ")
mes2 = input(f"Agora o {Y}mês{W}: ")
ano2 = input(f"E o {Y}ano{W}: ")

print(f"{ql} --- {ql}")# separação ----

print(f"Muito bem, então conferindo seus dados, estou registrando aqui.{ql}{G}{nome2}{W}, nascimento em{G} {dia2}/{mes2}/{ano2}{W}{ql}")


print(f"[DADOS FINANCEIROS] {ql}") #título dados financeiros

#paragrafo3 - dados financeiros
patrimonio2 = input(f"Agora me  informa por favor alguns dados financeiros.{ql}Se você somar o dinheiro que tem guardado, me diz o total desse{Y} patrimônio{W}: R$ ")
salario2 = input(f"Me diz teu {Y}salário{W}: R$")

#paragrafo4 - gastos mensais
aluguel2 = input(f"Sobre os seus gastos, me informa por partes po favor.{ql}Quanto custa teu {Y}aluguel{W} (incluindo condomínio e outras taxas): R$ ")
feira2 = input(f"Mais ou menos o quanto você gasta fazendo {Y}feira{W} todo mês: R$ ")
comida2 = input(f"E com {Y}comida{W} fora de casa, em média dá quanto: R$ ")
transporte2 = input(f"Na mobilidade, quanto que gasta com {Y}transporte{W} (ônibus, Uber, gasolina etc): R$ ")
outros2 = input(f"Pra terminar, quanto você gasta com {Y}outros{W} (lazer, roupas, etc): R$ ")

print(f"--- {ql}")# separação ----

#paragrafo5 - cresumo dos dados
print(f"Obrigado,{G}{nome2}{W}, resumindoas informações financeiras até agora.{ql}Os seus gastos discriminados são:")
print(f"{G}Aluguel:{W} R$ {float(aluguel2):.2f}")
print(f"{G}Feira{W}: R$ {float(feira2):.2f}")
print(f"{G}Comida fora{W}: R$ {float(comida2):.2f}")
print(f"{G}Transporte{W}: R$ {float(transporte2):.2f}")
print(f"{G}Outros{W}: R$ {float(outros2):.2f}") 
#calculo dos gastos totais
gasto_total2 = float(aluguel2)+float(feira2)+float(comida2)+float(transporte2)+float(outros2)
print(f"{G}GASTOS TOTAIS{W}: R$ {float(gasto_total2):.2f}{ql}")

print(f"--- {ql}")# separação ---- 

#paragrafo6 
#restante do salario
sobra2 = int(salario2) - gasto_total2
print(f"Pra terminar, calculando o seu saldo mensal, com base em tos os gastos{ql}e no teu salário, o valor resultante é de {G}{float(sobra2):.2f}{W}")
#investimento
investimento2 = input(f"Desse valor, considerando que qualquer investimento é válido,{ql}o quanto você conseguiria{Y} investir{W} todo mês: R$ ")
#sugestão de investimento
print(f"Ok, anotado, o valor do investimento é de R$ {G}{float(investimento2):.2f}{W}.{ql}Acredito que coletei todas as informações necessárias{ql}")

#missão 2 (miniprojeto2)----------------------------

print(f"Agora sim, vamos pensar no futuro! Você tem  um próximo objetivo financeiro?{ql}Um desejo de adquirir ou realizar algo que você quer e que precisa de investimento?")
print(f"Exemplos de objetivos assim são:{ql}Comprar uma moto ou carro, fazer uma viagem, comprar uma casa, fazer um curso, etc,")
objetivo2 = input(f"Qual seria esse seu próximo {Y}objetivo{W} financeiro: ")
valor_objetivo2 = input(f"Qual o valor do {Y}objetivo{W} financeiro: R$ ")
print(f"Em uma conta simples que fiz aqui, sem considerar rendimentos ou inflação,{ql}com base na sua capacidade de investimento mensal de{G} R$ {float(investimento2):.2f}{W}{ql} e seu patrimônio atual de {G}R$ {float(patrimonio2):.2f}{W}")
print(f"Você conseguiria atingir o valor de {G}R$ {float(valor_objetivo2):.2f}{W} em:")

#calculo do tempo para atingir o objetivo meses
tempo_objetivo_meses2 = (float(valor_objetivo2) - float(patrimonio2)) / float(investimento2)
#calculo do tempo para atingir o objetivo anos
tempo_objetivo_anos2 = tempo_objetivo_meses2/12

print(f"{float(tempo_objetivo_meses2):.2f} meses")
print(f"Ou {tempo_objetivo_anos2} anos")

#mensagem final
print(f"Por hora, é isso que tenho para te ajudar{ql}Espero que tenha sido útil")


#missaão 2 - mini projeto 3 -----------------------------------
#criação dos objetos do usuario (2) do chatbot a partrir dos input
#inportar pra pessoa 2-----
from data import Data2
from financas import Financas2
from pessoa import Pessoa2  
#pessoa 2
data_nascimento2 = Data2(dia2, mes2, ano2)
financas_usuario2 = Financas2(patrimonio2, salario2, gasto_total2, investimento2)
pessoa_usuario2 = Pessoa2(nome2, data_nascimento2, financas_usuario2)

#dados usuario 1
print(f"dados do usuario 1: {pessoa_usuario.nome}, {pessoa_usuario.nascimento.data_nascimento}, {pessoa_usuario.financas.patrimonio}, {pessoa_usuario.financas.salario}, {pessoa_usuario.financas.gastos}, {pessoa_usuario.financas.investimentos}")
#dados usuario 2
print(f"dados do usuario 2: {pessoa_usuario2.nome2}, {pessoa_usuario2.nascimento2.data_nascimento2}, {pessoa_usuario2.financas2.patrimonio2}, {pessoa_usuario2.financas2.salario2}, {pessoa_usuario2.financas2.gastos2}, {pessoa_usuario2.financas2.investimentos2}")  