import os

#--formatação de texto--------
G = '\033[32m' # green - verde
P = '\033[1;35m' # purple - roxo 
ql = "\n" #quebra de linha
i = '\033[3m' # italico
r = '\033[0m' # reset

#-- ler o txt -----------------------------------------
# Ajustando o caminho do arquivo com base no diretório do script//copilot
caminho_arquivo = "../rsc/pessoas.txt"

# Resolve o caminho relativo com base no diretório do script //copilot
caminho_resolvido = os.path.join(os.path.dirname(__file__), caminho_arquivo)

# Abre o arquivo usando o caminho resolvido //copilot
with open(caminho_resolvido, encoding="utf-8") as arquivo:  # abrir o arquivo
    dados_pessoastxt = arquivo.read()  # ler o arquivo




#funções
from dados import inserir_pessoa



#funções do menu------------------------------------------ interface ))))
#opção i
#def digitar_dados_pessoa(pessoas): #a variável do tipo list já está definida automaticamente no no main ou devvo definir o tipo?
#    nome = input("Digite o nome da pessoa: ")
#   salario = float(input(f"{r}Digite o seu salário:{G} R$ "))
#    patrimonio = float(input(f"{r}Digite o seu patrimônio:{G} R$ "))
#    inserir_pessoa(pessoas, nome, salario, patrimonio, 0) #coleta os dados e passa para a função inserir_pessoa(adicionando pessoa na lista)
    #cria tupla com os dados da pessoa
def digitar_dados_pessoa():
    with open(caminho_resolvido, "a", encoding="utf-8") as arquivo:  # abrir o arquivo para adição
        nome = input("Digite o nome da pessoa: ")
        salario = float(input(f"{r}Digite o seu salário:{G} R$ "))
        patrimonio = float(input(f"{r}Digite o seu patrimônio:{G} R$ "))
        conta_corrente = 0
        arquivo.write(f"{nome},{salario},{patrimonio},{conta_corrente}\n")  # adiciona a nova pessoa no arquivo   


    print(f"{r}{i}Pessoa inserida com sucesso!{r}{ql}")

#opção 
#usar for para mostrar --------------------------------------------- interface ))))
def mostrar_dados_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome: {pessoa.nome:<20} {r}Salário:{i}{G} "
              f"R$ {pessoa.salario:.2f} {r}Patrimônio: R$ {i}{G}"
              f" {pessoa.patrimonio:<10.2f} {r}")    


#opção s OBS: opção s já funciona saindo do while do main