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
from dados import carregar_dados
from pessoa import Pessoa




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
    pessoas = carregar_dados() #carrega os dados das pessoas do arquivo
    if not pessoas:
        print(f"{r}{i}Nenhuma pessoa cadastrada.{r}{ql}")
        return

    for pessoa in pessoas: #itera sobre cada pessoa na lista
        print(f"Nome: {pessoa.nome:<23} {r}Salário:{i}{G} "#adicionei 3 caracteres para seguir o formato do txt
              f"R$ {pessoa.salario:.2f} {r}Patrimônio: R$ {i}{G}"
              f" {pessoa.patrimonio:<10.2f} {r}")

#opção s OBS: opção s já funciona saindo do while do main