# formatação de texto
from main import G, P, ql, i, r
#funções
from dados import inserir_pessoa



#funções do menu------------------------------------------ interface ))))
#opção i
def digitar_dados_pessoa(pessoas): #a variável do tipo list já está definida automaticamente no no main ou devvo definir o tipo?
    nome = input("Digite o nome da pessoa: ")
    salario = float(input(f"{r}Digite o seu salário:{G} R$ "))
    patrimonio = float(input(f"{r}Digite o seu patrimônio:{G} R$ "))
    inserir_pessoa(pessoas, nome, salario, patrimonio, 0) #coleta os dados e passa para a função inserir_pessoa(adicionando pessoa na lista)
    #cria tupla com os dados da pessoa


    print(f"{r}{i}Pessoa inserida com sucesso!{r}{ql}")

#opção 
#usar for para mostrar --------------------------------------------- interface ))))
def mostrar_dados_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome: {pessoa.nome:<20} {r}Salário:{i}{G} "
              f"R$ {pessoa.salario:.2f} {r}Patrimônio: R$ {i}{G}"
              f" {pessoa.patrimonio:<10.2f} {r}")    


#opção s OBS: opção s já funciona saindo do while do main