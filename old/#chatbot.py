#chatbot

#variaveis
opcao = ""
nome = None
nascimento = None
patrimonio = None

#loop
while opcao != "sair":
    print("1 - Cadastrar nome \n")
    print("2 - Cadastrar nascimento \n")
    print("3 - Cadastrar patrimônio \n")
    print("digite sair para sair")
    opcao = input("Digite uma opção\n ")
    if opcao == "1":
        nome =  input("digite seu nome:")
    elif opcao == "2":
        nascimento = input("digite o dia do seu nascimento")
    elif opcao == "3":
        patrimonio = float(input("digite seu patrimonio"))


