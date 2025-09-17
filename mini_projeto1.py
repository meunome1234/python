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

var_renda_e_patrimonio = var_patrimonio + var_salario

#missão 2 parte 2
print("patrimonio de", var_patrimonio,"salario de", var_salario,"gastos mensais:", var_gastos, "investimento mensal:", var_investimento)#dados

#percentual salario + patrimonio em salario minimo
var_renda_e_patrimonio


print("salario + renda = ", var_renda_e_patrimonio)#informacao extra



