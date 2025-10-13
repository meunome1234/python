#peça ao usuário inserir uma senha
# a senha deve ter no mínimo 8 caracteres
# a senha deve ter pelo manos 1 número
#a senha deve ter caracteres maiúsculos e minúsculos
#para qualquer um dos erros acima, imprima uma mensagem e peça para o usuário digitar novamente


import re

senha_valida = True
#-----------------------------------
senha = input("crie uma senha")

#mensagem de erro
if senha_valida == False
    print("a senha deve ter no mínimo 8 caracteres, número, letras maísculas e minúsculas. tente novamente")



#checagem numero de caracteres
num_caracteres = len(senha)
    if num_caracteres < 8:
    senha_valida = False

#checagem  maiúscula e minúscula

caractere_M = False
    if any(char.isupper() for char in texto):
    caractere_M = True