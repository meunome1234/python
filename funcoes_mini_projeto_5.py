
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

#opção m
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


#função simular gastos

def simular_gastos(pessoa, gastos): #puxa objeto pessoa e o dicionário gastos
    for setor, (gasto_minimo, gasto_ideal) in gastos.items(): #itera sobre os itens do dicionário gastos
        gasto_ideal = gasto_ideal * pessoa.salario #calcula o gasto ideal em valor monetário
        gato =