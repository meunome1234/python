from indices import taxa_mensal_rendimento
from indices import gastos

#sumular recebimentos para atualizar os valores do patrimônio ------- simulador )))))
def simular_recebimentos(pessoa, taxa_mensal_rendimento): #puxa objeto pessoa e a taxa mensal de rendimento
    rendimento = pessoa.patrimonio * taxa_mensal_rendimento #calcula o rendimento usando a taxa mensall
    pessoa.conta_corrente += rendimento + pessoa.salario #atualiza o valor da conta corrente somando o rendimento e o salário

#---------------------------------------------------------------------------------------------
#função simular gastos --------------------------------------------- simulador )))))

def simular_gastos(pessoa, gastos): #puxa objeto pessoa e o dicionário gastos
    lista_aviso = [] #cria lista vazia para armazenar avisos
    lista_pagamentos = [] #cria lista vazia para armazenar os gastos realizados

    for setor, (gasto_minimo, gasto_ideal) in gastos.items(): #itera sobre os itens do dicionário gastos
        gasto_ideal = gasto_ideal * pessoa.salario #calcula o gasto ideal em valor monetário
        gasto = max( gasto_minimo, gasto_ideal) #determina o gasto real como o máximo entre o mínimo e o ideal

        if pessoa.conta_corrente >= gasto: #verifica se há saldo suficiente na conta corrente
            pessoa.conta_corrente -= gasto #subtrai o gasto da conta corrente
            lista_pagamentos.append( #adiciona o gasto à lista de pagamentos realizados
                f"{r}{i}{pessoa.nome} pagou R$ {gasto:.2f} em {setor}.{r}") 

        else:
            lista_aviso.append( #adiciona o setor à lista de avisos se não houver saldo suficiente
                f"{r}{i}Atenção! {pessoa.nome} não tem saldo suficiente! setor afetado:{setor}.{r}{ql}") #avisa sobre saldo insuficiente    
    pessoa.patrimonio += pessoa.conta_corrente #atualiza o patrimônio somando o saldo da conta corrente
    pessoa.conta_corrente = 0 #zera a conta corrente após transferir o saldo para o patrimônio

    return lista_aviso, lista_pagamentos #retorna a lista de avisos e de pagamentos

#----------------------------------------------------------------------------------------
#função simular_mês_população ---------------------------------------------- simulador )))))
def simular_mes_populacao(pessoas, taxa_mensal_rendimento, gastos):
    avisos_simulacao = [] #cria lista vazia para armazenar avisos 
    pagamentos_simulacao = [] #cria lista vazia para armazenar pagamentos   
    
    for pessoa in pessoas: #itera sobre cada pessoa na lista pessoas
        simular_recebimentos(pessoa, taxa_mensal_rendimento) #chama a função para simular recebimentos
        
        avisos, pagamentos = simular_gastos(pessoa, gastos) #chama a função para simular gastos e captura os avisos
        
        avisos_simulacao.extend(avisos)  #adiciona os avisos da pessoa à lista geral de avisos
        pagamentos_simulacao.extend(pagamentos)  #adiciona os pagamentos da pessoa à lista geral de pagamentos  

    return avisos_simulacao, pagamentos_simulacao #retorna a lista de avisos de todas as pessoas e a simulação de pagamentos
#--------------------------------------------