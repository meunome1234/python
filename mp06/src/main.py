#importações necessárias
import csv
import json
import os

# Ajustando o caminho do arquivo com base no diretório do script//copilot
caminho_arquivo = "../rsc/pessoas.txt"

# Resolve o caminho relativo com base no diretório do script //copilot
caminho_resolvido = os.path.join(os.path.dirname(__file__), caminho_arquivo)

# Abre o arquivo usando o caminho resolvido //copilot
with open(caminho_resolvido, encoding="utf-8") as arquivo:  # abrir o arquivo
    dados_pessoastxt = arquivo.read()  # ler o arquivo
    

#importar funções
from interface import digitar_dados_pessoa
from interface import mostrar_dados_pessoas
from indices import taxa_mensal_rendimento
from indices import gastos
from simulador import simular_mes_populacao
from interface import P, ql, i, r
#-------------------------------------------





#programa principal
def main():

    pessoas = [] #cria lista vazia para armazenar pessoas

    sair = False #variável de controle do while do menu


    #menu de opções------------------------------------------------------------------------
    while sair == False:
        print(f"[SIMULADOR DE RELAÇÕES DE MERCADO]{ql}escolha uma opção:{ql}- "
            f"[{P}d{r}]igitar dados de uma nova pessoa{ql}- "
            f"[{P}m{r}]ostrar dados de nova pessoa{ql}- "
            f"S[{P}i{r}]mular finanças mensais da população{ql}- "
            f"[{P}s{r}]air{ql}")

        opcao = input(f"opção: {P}")
        print(r) #reseta a cor após a entrada da opção

        if opcao == "d":
            print(f"[INSERIR NOVA PESSOA]{ql}")
            digitar_dados_pessoa(pessoas)
            input(f"{ql}pressione enter...")#freiar o while
            

        elif opcao == "m":
            print(f"[DADOS DAS PESSOAS]")
            mostrar_dados_pessoas(pessoas)
            input(f"{ql}pressione enter...")#freiar o while

        elif opcao == "i":
            print(f"[SIMULAR MÊS DA POPULAÇÃO]{ql}")
            
            avisos, pagamentos = simular_mes_populacao(pessoas, taxa_mensal_rendimento, gastos) #chama a função para simular o mês da população e captura os avisos 
        

            print(f"{ql}[RELATÓRIO DE PAGAMENTOS]{ql}")
            for p in pagamentos:
                print(p)

            if avisos:
                print(f"{ql}[RELATÓRIO DE AVISOS]{ql}")
                for a in avisos:
                    print(a)
           

            print(f"{i}Simulação de um mês concluída para todas as pessoas.{r}{ql}")
            input(f"{ql}pressione enter...")#freiar o while
        
        
        
        elif opcao == "s":
            sair = True
            print(f"")

        else:
            print(f"{ql}Entrada inválida{ql}")
            
    #-------------------------------------------------------------------------------------
#chama a função main
if __name__ == "__main__":
    main()

#--------------------------------------------
