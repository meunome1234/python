
i = '\033[3m' # italico
r = '\033[0m' # reset
G = '\033[32m' # green - verde
ql = "\n" #quebra de linha
#definição  das funções
from pessoa_mini_projeto_5 import Pessoa
from indices_mini_projeto_5 import taxa_mensal_rendimento
from indices_mini_projeto_5 import gastos   


def inserir_pessoa(pessoas, nome, salario, patrimonio, conta_corrente):#insere nova pessoa na lista pessoas (main)
    nova_pessoa = Pessoa(nome, salario, patrimonio, 0)#cria nova pessoa e conta corrente inicia em 0
    pessoas.append(nova_pessoa)#adiciona nova pessoa à lista pessoas


#funções do menu------------------------------------------
#opção i
def digitar_dados_pessoa(pessoas): #a variável do tipo list já está definida automaticamente no no main ou devvo definir o tipo?
    nome = input("Digite o nome da pessoa: ")
    salario = float(input(f"{r}Digite o seu salário:{G} R$ "))
    patrimonio = float(input(f"{r}Digite o seu patrimônio:{G} R$ "))
    inserir_pessoa(pessoas, nome, salario, patrimonio, 0) #coleta os dados e passa para a função inserir_pessoa(adicionando pessoa na lista)
    #cria tupla com os dados da pessoa


    print(f"{r}{i}Pessoa inserida com sucesso!{r}{ql}")

#opção 
#usar for para mostrar 
def mostrar_dados_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome: {pessoa.nome:<20} {r}Salário:{i}{G} "
              f"R$ {pessoa.salario:.2f} {r}Patrimônio: R$ {i}{G}"
              f" {pessoa.patrimonio:<10.2f} {r}")    


#opção s OBS: opção s já funciona saindo do while do main

#sumular recebimentos para atualizar os valores do patrimônio
def simular_recebimentos(pessoa, taxa_mensal_rendimento): #puxa objeto pessoa e a taxa mensal de rendimento
    rendimento = pessoa.patrimonio * taxa_mensal_rendimento #calcula o rendimento usando a taxa mensall
    pessoa.conta_corrente += rendimento + pessoa.salario #atualiza o valor da conta corrente somando o rendimento e o salário

#---------------------------------------------------------------------------------------------
#função simular gastos

def simular_gastos(pessoa, gastos): #puxa objeto pessoa e o dicionário gastos
    lista_aviso = [] #cria lista vazia para armazenar avisos
    lista_pagamentos = [] #cria lista vazia para armazenar os gastos realizados

    for setor, (gasto_minimo, gasto_ideal) in gastos.items(): #itera sobre os itens do dicionário gastos
        gasto_ideal = gasto_ideal * pessoa.salario #calcula o gasto ideal em valor monetário
        gasto = max( gasto_minimo, gasto_ideal) #determina o gasto real como o máximo entre o mínimo e o ideal

        if pessoa.conta_corrente >= gasto: #verifica se há saldo suficiente na conta corrente
            pessoa.conta_corrente -= gasto #deduz o gasto da conta corrente
            lista_pagamentos.append( #adiciona o gasto à lista de pagamentos realizados
                f"{r}{i}{pessoa.nome} pagou R$ {gasto:.2f} em {setor}.{r}") 

        else:
            lista_aviso.append( #adiciona o setor à lista de avisos se não houver saldo suficiente
                f"{r}{i}Atenção! {pessoa.nome} não tem saldo suficiente! setor afetado:{setor}.{r}{ql}") #avisa sobre saldo insuficiente    
    pessoa.patrimonio += pessoa.conta_corrente #atualiza o patrimônio somando o saldo da conta corrente
    pessoa.conta_corrente = 0 #zera a conta corrente após transferir o saldo para o patrimônio

    return lista_aviso, lista_pagamentos #retorna a lista de avisos e de pagamentos

#----------------------------------------------------------------------------------------
#função simular_mês_população
def simular_mes_populacao(pessoas, taxa_mensal_rendimento, gastos):
    avisos_simulacao = [] #cria lista vazia para armazenar avisos de todas as pessoas
    pagamentos_simulacao = [] #cria lista vazia para armazenar pagamentos de todas as pessoas   
    
    for pessoa in pessoas: #itera sobre cada pessoa na lista pessoas
        simular_recebimentos(pessoa, taxa_mensal_rendimento) #chama a função para simular recebimentos
        
        avisos, pagamentos = simular_gastos(pessoa, gastos) #chama a função para simular gastos e captura os avisos
        
        avisos_simulacao.extend(avisos)  #adiciona os avisos da pessoa à lista geral de avisos
        pagamentos_simulacao.extend(pagamentos)  #adiciona os pagamentos da pessoa à lista geral de pagamentos  
        
    return avisos_simulacao, pagamentos_simulacao #retorna a lista de avisos de todas as pessoas e a simulação de pagamentos