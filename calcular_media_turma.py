#criar uma lista com nome dos alunos
#criar lista com nota dos alunos
#calcular média da lista

alunos = ["teresa", "davi", "joaquim"]
notas = [9.5, 7.0,6.5]

#soma das notas
soma = 0 #soma recebe 0
for nota in notas: #para cada nota(variavel criada agora) da lista notas
    soma += nota #soma é ela mesma + o item nota até completar todos os elementos da lista notas

media = soma / len(notas)


print("a média da turma é", media)
