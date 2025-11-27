
with open("desafio.txt", "w") as arquivo:#criar o arquivo
    arquivo.write("cadastro de pessoas\n")


sair = False#controle do menu

while not sair:
    opcao = input("Digite 'i' para inserir, 'l' para ler, 's para sair: ")
    if opcao == 'i':#pegar nome e adicionar no arquivo-----------------
        nome = input("digite seu nome: ")
        with open("desafio.txt", "a") as arquivo:#adiciona (append)
            arquivo.write(f"\n{nome}")
        input("pressione enter para continuar...")#frear o programa

    elif opcao == 'l':#ler o arquivo e mostrar os nomes ---------------
        with open("desafio.txt", "r") as arquivo:#read
            conteudo = arquivo.read()#cria variavel conteudo e lê o arquivo
            print (f"{conteudo} \n")
        input("pressione enter para continuar...")#frear o programa
    elif opcao == 's':#sair do programa--------------------------------
        sair = True
    else: #erro de opção-----------------------------------------------
        print("opção inválida, tente novamente")
        input("pressione enter para continuar...")
    