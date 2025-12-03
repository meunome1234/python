from pessoa import Pessoa

#-------------------------------------------- dados )))))
def inserir_pessoa(pessoas, nome, salario, patrimonio, conta_corrente):#insere nova pessoa na lista pessoas (main)
    nova_pessoa = Pessoa(nome, salario, patrimonio, 0)#cria nova pessoa e conta corrente inicia em 0
    pessoas.append(nova_pessoa)#adiciona nova pessoa à lista pessoas