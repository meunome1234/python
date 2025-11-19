
i = '\033[3m' # italico
r = '\033[0m' # reset
G = '\033[32m' # green - verde
ql = "\n" #quebra de linha
#definição  das funções
from pessoa_mini_projeto_5 import Pessoa


def inserir_pessoa(pessoas, nome, salario, patrimonio, conta_corrente):#insere nova pessoa na lista pessoas (main)
    nova_pessoa = Pessoa(nome, salario, patrimonio, 0)#cria nova pessoa e conta corrente inicia em 0
    pessoas.append(nova_pessoa)#adiciona nova pessoa à lista pessoas


#funções do menu------------------------------------------
#opção i
def digitar_dados_pessoa(pessoas): #a variável do tipo list já está definida automaticamente no no main ou devvo definir o tipo?
    nome = input("Digite o nome da pessoa: ")
    salario = float(input(f"{r}Digite o seu salário:{G} "))
    patrimonio = float(input(f"{r}Digite o seu patrimônio:{G} "))
    inserir_pessoa(pessoas, nome, salario, patrimonio, 0) #coleta os dados e passa para a função inserir_pessoa(adicionando pessoa na lista)
    #cria tupla com os dados da pessoa


    print(f"{r}{i}Pessoa inserida com sucesso!{r}{ql}")

#opção m
#usar for para mostrar 
def mostrar_dados_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome: {pessoa.nome}Salário:{G} {pessoa.salario}Patrimônio:{G}"
            f" {pessoa.patrimonio}Conta Corrente: {G}{pessoa.conta_corrente}{ql}{r}")    


#opção s OBS: opção s já funciona saindo do while do main
