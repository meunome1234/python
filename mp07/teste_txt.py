import os 
from pessoa import Pessoa
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
    print(lista_pessoas)            
    return lista_pessoas

  