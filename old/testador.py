passageiros = 40
paradas_percorridas= 0
while paradas_percorridas < 5:# menor que 5, já que o laço começa em 0
    passageiros -= 3
    paradas_percorridas += 1
print(f"Após 5 paradas, restam {passageiros} passageiros no ônibus")
    