import os

caminho_arquivo = "../rsc/pessoas.txt"

# Resolve o caminho relativo com base no diretório do script //copilot
caminho = os.path.join(os.path.dirname(__file__), caminho_arquivo)
#------------------------------------------------------

print(f"Testando leitura do arquivo: {caminho}\n")

# Verifica se o arquivo existe /
if not os.path.exists(caminho):
    print(" O arquivo não foi encontrado.")
else:
    print("✔ Arquivo encontrado!")
    print("\n--- Conteúdo do arquivo ---\n")
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print(conteudo if conteudo.strip() else "(Arquivo vazio)")
    except Exception as erro:
        print(f" Erro ao ler o arquivo: {erro}")

print("\n--- Fim do teste ---")
