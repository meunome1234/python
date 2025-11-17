
i = '\033[3m' # italico
#definição  das funções
from pessoa_mini_projeto_5 import Pessoa


def Inserir_pessoa(pessoas, nome, salario, patrimonio, conta_corrente):#insere nova pessoa na lista pessoas (main)
    nova_pessoa = Pessoa(nome, salario, patrimonio, 0)#cria nova pessoa e conta corrente inicia em 0
    pessoas.append(nova_pessoa)#adiciona nova pessoa à lista pessoas


#funções do menu------------------------------------------
#opção i
def Digitar_dados_pessoa(pessoas): #a variável do tipo list já está definida automaticamente no no main ou devvo definir o tipo?
    nome = input("Digite o nome da pessoa: ")
    salario = float(input("Digite o seu salário;  "))
    patrimonio = float(input("Digite o seu patrimônio "))
    Inserir_pessoa(pessoas, nome, salario, patrimonio, 0) #coleta os dados e passa para a função inserir_pessoa(adicionando pessoa na lista)
    print(f"{i}Pessoa inserida com sucesso!")

#opção m
#usar for para mostrar 

#opção s OBS: opção s já funciona saindo do while do main
