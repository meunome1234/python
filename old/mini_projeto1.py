# missão 1 parte 1
var_nome = "billy fernando gato soares"
var_dia = 16
var_mes = 11
var_ano = 2016

#missão 1 parte 2
print( var_nome ,", nascido em", var_dia ,"/", var_mes,"/", var_ano )

#missão 1 parte 3 - calculo da idae

    # conversão de mês para dias
    
var_ano_limite = 2025  #ano da data limite(dado fixo)

var_anos_vividos = var_ano_limite - var_ano 
var_idade_anos = var_anos_vividos - 1# armazenar corretamente a idade em anos
var_anos_vividos = var_anos_vividos * 365 #conversão de ano para dias

    # obs: var_anos_vividos está com o valor definitivo (em dias)

var_mes_limite = 5 #como a pessoa ainda não fez aniversário, há uma subtração de meses
var_meses_vividos = var_mes_limite - var_mes #resultado negativo não interfere no resultado real

var_meses_vividos = var_meses_vividos * 30 #conversão de mês para dias
    # obs: var_meses_vividos também está com o valor definitivo (em dias)

    # conversão dias
var_dia_limite = 14
var_dias_vividos = var_dia_limite - var_dia #resultado negativo necessário para resultado preciso

#missão 1 parte 4
#calculo final dos dias vividos
var_dias_totais= var_anos_vividos + var_meses_vividos + var_dias_vividos

print(var_nome, "tem", var_dias_totais ,"dias de vida.")
print(var_nome, "tem", var_idade_anos ,"anos de vida.")


#missa0 1 concluida


#missão 2 parte 1
var_patrimonio = 2500
var_salario= 1518
var_gastos= 1250
var_investimento= 100


#missão 2 parte 2
var_numero_SM_renda = var_salario / 1518 #calculo numero de salarios minimos

var_porcentagem_SM_renda = (var_salario / 1518) *100 #calculo % renda em sm

var_porcentagem_SM_patrimonio = (var_patrimonio / 1518) *100 #calculo % patrimonio em sm

var_porcentagem_sm_gastos = (var_gastos / 1518) *100 #calculo % gastos em sm

print( var_nome,", recebe mensalmente R$", var_salario)
print("os recebimentos equivalem a", var_numero_SM_renda , "salarios mínimos")#informacao extra salario
print( var_nome,"tem um patrimonio de R$", var_patrimonio)#informacao extra patrimonio
print( var_nome,"gasta R$", var_gastos, "por mês")#informacao extra gastos


#percentual patrimonio em salario minimo
print("patrimonio em salario minimo = ", var_porcentagem_SM_patrimonio,"%")#informacao extra patrimonio
#percentual gastos em salario minimo
print("gastos em salario minimo = ", var_porcentagem_sm_gastos,"%")#informacao extra gastos


#missão 2 parte 3

#rendimento patrimonio mes
var__patrimonio_com_rendimento = (var_patrimonio * 0.05) + var_patrimonio #rendimento mensal do patrimonio (5%)
var_patrimonio = var__patrimonio_com_rendimento + var_investimento  #adiciona o investimento mensal ao patrimonio
var_sobra = var_salario - var_gastos #calculo do que sobra do salario

print("os gastos equivalem a", var_porcentagem_sm_gastos ,"% de sua renda")#porcentagem gastos
print( var_nome, "investe mensalmente R$", var_investimento)#investimento mensal
print(var_nome, "após 1 mês está com o patrimônio de R$",var__patrimonio_com_rendimento)#patrimonio com rendimento
print("o saldo de dinheiro livre no mês foi de R$", var_sobra)#sobra após gastos

#missão 2 concluida

#missão 3 parte 1

#rendimento 12 meses sem adição no período

var__patrimonio_12meses = var__patrimonio_com_rendimento * (1 + 0.05)**12 #calculo dinheiro total sem investir
var_rendimento12meses = var__patrimonio_12meses - var__patrimonio_com_rendimento #calculo do rendimento em 12 meses
#missão 3 parte 2


print( "se", var_nome, " não investir nada, após 12 meses o seu patrimônio terá rendio R$", var_rendimento12meses,"e será R$", var__patrimonio_12meses )



