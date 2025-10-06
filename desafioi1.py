
#desafio-------------------------------------------------------------
#classe pessoa
class Pessoa:
    def __init__(self, nome, investimento, patrimonio):
        self.nome = nome
        self.investimento = investimento
        self.patrimonio = patrimonio
#---------------------------------------------------------------------

#conversa inicial =============================================================
nome = input ("olá, irei calcular o rendimento do seu patrimônio. Qual o seu nome?  ")

patrimonio = input(f"perfeito, {nome}, qual seu patrimônio atual? ")
investimento = input(f"ok, {nome}, quanto você investe mensalmente? ")

#criação do objeto pessoa1 -------------------------------------------
pessoa1 = Pessoa(nome, investimento, patrimonio)
#-----calculo rendimento 6 meses----------------------------------------------------------------

var_p_6m_investindo = float(patrimonio)*(1+0.05)**6 + float(investimento)*((1 + 0.05)**6 - 1) / 0.05 #calculo patrimonio em 6M investindo (5%)          

#----- resultados

print(f"se {nome}, investir R${investimento} por mês, após 6 meses o seu patrimônio será R${var_p_6m_investindo:.2f}") #patrimonio investindo
#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------
print("\n")


#conversa 2=========================================================================
nome = input ("olá, irei calcular o rendimento do seu patrimônio. Qual o seu nome?  ")

patrimonio = input(f"perfeito, {nome}, qual seu patrimônio atual? ")
investimento = input(f"ok, {nome}, quanto você investe mensalmente? ")

#criação do objeto pessoa 2-----------------------------------------------------
pessoa2 = Pessoa(nome, investimento, patrimonio)
#- calculo rendimento 6 meses------------------------------------------------------------------------------
var_p_6m_investindo2 = float(pessoa2.patrimonio)*(1+0.05)**6 + float(pessoa2.investimento)*((1 + 0.05)**6 - 1) / 0.05 #calculo patrimonio em 6M investindo (5%)          

#----- resultados
print(f"se {pessoa2.nome}, investir R${pessoa2.investimento} por mês, após 6 meses o seu patrimônio será R${var_p_6m_investindo2:.2f}") #patrimonio investindo

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------
#   resultados  -------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

print("\n")
print(f"{pessoa1.nome}, seu patrimônio atual é R${pessoa1.patrimonio} investe R${pessoa1.investimento} por mês")
print(f"Após 6 meses, o patrimonio de {pessoa1.nome} será de R${var_p_6m_investindo:.2f}")
#----------------------------------------------------------------------

print("\n")
#----------------------------------------------------------------------
print(f"{pessoa2.nome}, seu patrimônio atual é R${pessoa2.patrimonio} investe R${pessoa2.investimento} por mês")
print(f"Após 6 meses, o patrimonio de {pessoa2.nome}   será de R${var_p_6m_investindo2:.2f}")
