from pessoa import Pessoa

#importações necessárias
import csv
import json
import os

# Caminho correto para o arquivo pessoas.txt
caminho_arquivo = os.path.join(os.path.dirname(__file__), "../rsc/pessoas.txt")

#carregar pesssoas
def carregar_dados():
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo: #abre o arquivo para leitura
        linhas = arquivo.readlines() #lê todas as linhas do arquivo




#-------------------------------------------- dados )))))
def inserir_pessoa(nome, salario, patrimonio, conta_corrente):#insere nova pessoa na lista pessoas (main)
    nova_pessoa = Pessoa(nome, salario, patrimonio, 0)#cria nova pessoa e conta corrente inicia em 0
    arquivo.append(nova_pessoa)#adiciona nova pessoa à lista pessoas
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo: #abre o arquivo para adição
        arquivo.write(f"{nome},{salario},{patrimonio},{conta_corrente}\n") #adiciona a nova pessoa no arquivo