#importações necessárias
import csv
import json
import os

#--formatação de texto--------
G = '\033[32m' # green - verde
P = '\033[1;35m' # purple - roxo 
ql = "\n" #quebra de linha
i = '\033[3m' # italico
r = '\033[0m' # reset
#-------------------------------------------
#funções
from dados import inserir_pessoa
from pessoa import Pessoa


# Corrigindo o caminho do arquivo para um caminho relativo baseado no diretório do script
caminho_arquivo = os.path.join(os.path.dirname(__file__), "../rsc/pessoas.txt")

with open(caminho_arquivo, "r", encoding="utf-8") as arquivo: #abre o arquivo para leitura
    linhas = arquivo.readlines() #lê todas as linhas do arquivo
    arquivo = [] #cria lista vazia para armazenar os objetos Pessoa
    for linha in linhas: #itera sobre cada linha do arquivo
        nome, salario, patrimonio= linha.split(",") 
        pessoa = Pessoa(nome, float(salario), float(patrimonio), float(conta_corrente)) #cria objeto Pessoa com os dados lidos
        arquivo.append(pessoa) #adiciona o objeto Pessoa à lista arquivo


#funções do menu------------------------------------------ interface ))))
#opção i
def digitar_dados_pessoa(): 
    nome = input("Digite o nome da pessoa: ")
    salario = float(input(f"{r}Digite o seu salário:{G} R$ "))
    patrimonio = float(input(f"{r}Digite o seu patrimônio:{G} R$ "))
    inserir_pessoa(nome, salario, patrimonio, 0) #coleta os dados e passa para a função inserir_pessoa(adicionando pessoa na lista)
    #cria tupla com os dados da pessoa
   

    print(f"{r}{i}Pessoa inserida com sucesso!{r}{ql}")

#opção 
#usar for para mostrar --------------------------------------------- interface ))))
def mostrar_dados_pessoas():
    for pessoa in arquivo: #itera sobre cada pessoa na lista pessoas
        print(f"Nome: {pessoa.nome:<20} {r}Salário:{i}{G} "
              f"R$ {pessoa.salario:.2f} {r}Patrimônio: R$ {i}{G}"
              f" {pessoa.patrimonio:<10.2f} {r}")    


#opção s OBS: opção s já funciona saindo do while do main