from pessoa import Pessoa

#-------------------------------------------- dados )))))
def inserir_pessoa(pessoas, nome, salario, patrimonio, conta_corrente):#insere nova pessoa na lista pessoas (main)
    nova_pessoa = Pessoa(nome, salario, patrimonio, 0)#cria nova pessoa e conta corrente inicia em 0
    pessoas.append(nova_pessoa)#adiciona nova pessoa à lista pessoas
    with open("/rsc/pessoas.txt", "a") as arquivo: #abre o arquivo para adição
        arquivo.write(f"{nome},{salario},{patrimonio},{conta_corrente}\n") #adiciona a nova pessoa no arquivo