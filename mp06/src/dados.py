from pessoa import Pessoa
import os
#gambiarra no txt (removi as categorias)
# Define o caminho do arquivo 
caminho_arquivo = os.path.join(os.path.dirname(__file__), "../rsc/pessoas.txt")

def carregar_dados():#lê o txt
    
    lista_pessoas = [] #lista vazia para armazenar os objetos pessoa
    
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo: 
                linha = linha.strip() 
                
                #processamneto dentro do for
                if linha: # Protege contra linhas vazias (evita ValueError)//solução gemini
                    
                    nome, salario_str, patrimonio_str = linha.split(",") 
                        
                    salario = float(salario_str)
                    patrimonio = float(patrimonio_str)
                    
                    # Passa apenas 3 argumentos (conta_corrente = 0.0 é definido na classe Pessoa)
                    pessoa = Pessoa(nome, salario, patrimonio) 
                    
                    lista_pessoas.append(pessoa)# adiciona o objeto pessoa à lista
                        
    return lista_pessoas

def inserir_pessoa(nome, salario, patrimonio, conta_corrente):# insere nova pessoa no arquivo txt
    
    # Escreve APENAS 3 campos (conta corrente inicia em 0 já no pessoas.py)
    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo: 
        arquivo.write(f"{nome},{salario},{patrimonio}\n")


def salvar_dados_pessoas(listas_pessoas):# salva a lista de pessoas no arquivo txt
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:# o caminho já foi definido no início do dados.py
        for pessoa in listas_pessoas:
            # Escreve APENAS 3 campos (conta corrente inicia em 0 já no pessoas.py)
            arquivo.write(f"{pessoa.nome},{pessoa.salario},{pessoa.patrimonio}\n")