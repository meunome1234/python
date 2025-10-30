#__________________________________________________________________________________
#módulo 1: condicionais
#__________________________________________________________________________________
#1. if com condição de variável única e bloco de 1 linha-----------------

#1.Exercício 1: O Mago Elétrico está na área?
usou_mago_eletrico = True
if usou_mago_eletrico == True:
    print("Zap")

#1.Exercício 2: Pedalando sob o sol
esta_fazendo_sol = True
if esta_fazendo_sol == True:
    print("Hoje o pedal tá garantido")

#1.Exercício 3: Riff de Black Sabbath
tocando_black_sabbath = True
if tocando_black_sabbath == True:
    print("Aumenta o som que é iron man!")

#2. if com condição de variável única e bloco de várias linhas--------------------
#Exercício 1: Preparando o deck para a batalha
Modo_ranqueado = True
if Modo_ranqueado == True:
    print("conectando ao servidor de batalhas...")
    print("verificando seu deck...")
    print("Batalha prestes a começar!")

#2.Exercício 2: Cliente VIP da lanchonete
cliente_vip = True
if cliente_vip == True:
    print("Olá, cliente especial!")
    print("Você ganhou uma coxinha extra.")
    print("volte sempre!")
#2.Exercício 3: Checagem de segurança da bicicleta
trilha_longa = True
if trilha_longa == True:
    print("Verifique os freios antes de sair.")
    print("Não se esqueça de levar água.")
    print("Lembre-se de usar capacete.")   
#3. if com expressão de comparação e bloco de várias linhas-----------------
#3.Exercício 1: Elixir suficiente para o Golem
quantidade_elixir = 9
if quantidade_elixir >= 8:
    print("Elixir suficiente!")
    print("Golem posicionado na arena!")
#3.Exercício 2: Tarifa do busão
saldo_cartao = 5.00
if saldo_cartao >= 4.10:
    print("Saldo suficiente")
    print("PBoa viagem!")
#3.Exercício 3: Idade para show de Metal
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Entrada permitida")
#4. if com expressão lógica e bloco de várias linhas-----------------------
#4.Exercício 1: Combo de ataque: Gigante e Bruxa
tem_gigante = True
tem_bruixa = True
if tem_gigante == True and tem_bruixa == True:
    print("Combo Gigante e Bruxa ativado!")
    print("Prepare-se para a destruição!")
#4.Exercício 2: Pedalada para a Praia de Boa Viagem
dia_da_semana = input("Digite o dia da semana: ")
if dia_da_semana == "sábado" or dia_da_semana == "domingo":
    print("Dia de praia!")
    print("Vamos pedalar até a orla!")
#4.Exercício 3: Manutenção da bicicleta
tipo_uso = "trilha"
messes_ultima_manuntenção = 7
if tipo_uso == "trilha" and messes_ultima_manuntenção >= 6:
    print("ALERTA DE MANUNTENÇÃO!")
    print("Revisão completa recomendada")
#5. if com expressão lógica e ifs aninhados--------------------------------
#5.Exercício 1: Defesa Aérea e Terrestre
ataque_aereo = True
ataque_terrestre = False

if ataque_aereo == True and ataque_terrestre == True:
    ataque_combinado = True
    print("ataque combinado!Ativando todas as defesas!")
    torre_de_arqueiras = 599
    if ataque_combinado == True and torre_de_arqueiras <= 600:
        print("Alerta total, torre com pouca vida!")
#5.Exercício 2: Escolhendo o ônibus certo
destino = "faculdade"
onibus_lotado = False

if destino == "faculdade" and onibus_lotado == False:
    print("Embarcando para a ufrpe!")
    cartao_vem = True
    if cartao_vem == True:
        print("pagando meia passagem!")
#5.Exercício 3: Comprando um disco de vinil
album_em_bom_estado = True
preco = 120.0
if album_em_bom_estado == True and preco <= 150.0:
    print("levando essa relíquia para casa!")
    forma_de_pagamento = "dinheiro"
    if forma_de_pagamento == "dinheiro":
        print("Vou tentar pedir um desconnto!")
#6. if-else com variável única e blocos de várias linhas----------------
#6.Exercício 1: Batalha Vencida ou Perdida?
venceu_batalha = bool(input("Você venceu a batalha? (True/False): "))
if venceu_batalha == True:
    print("VITÓRIA!")
    print("Você ganhou 30 trofeus!")
else:
    print("DERROTA!")
    print("Tente novamente na próxima vez!")

#6.Exercício 2: Levar o guarda-chuva?
esta_chovendo = bool(input("Está chovendo? (True/False): "))
if esta_chovendo == True:   
    print("Não esqueça do guarda-chuva!")
    print("cuidado com as ruas alagadas.")
else:
    print("Dia de sol!")
    print("não esqueça o protetor solar")
#6.Exercício 3: Fone de ouvido para o busão
playlist_carregada = bool(input("Sua playlist está carregada? (True/False): "))
if playlist_carregada == True:
    print("Viagem vai ser ao som de muito rock!")
    print("Colocando fones de ouvido no máximo!")
else:
    print("Que tédio!")
    print("vou ter que ouvir a rádio do motorista")
#7. if-elif com variável única e blocos de várias linhas ---------------------------
#7.Exercício 1: Escolha sua carta lendária
escolha_lendaria = input("Escolha uma carta (Dragão infernal,Lenhador, Mineiro): ")
if escolha_lendaria == "Dragão infernal":
    print("cuidado com o calor!")
    print("Dano massivo contra tanques!")
elif escolha_lendaria == "Lenhador":    
    print("Ele chega com fúria!")
    print("Ótimo para ataques rápidos!")
elif escolha_lendaria == "Mineiro":
    print("Ele vai direto na torre!")
    print("Surpresa garantida!")

#7.Exercício 2: Qual lanche você quer?
pedido_lanche = input("Escolha seu lanche (Pastel, Coxinha, Esfiha) ")
if pedido_lanche == "Pastel":
    print("Uòtima escolha!")
    print("Saindo um pastel quentinho!")

elif pedido_lanche == "Coxinha":
    print("A clássica!")
    print("uidado para não queimar a língua!")
elif pedido_lanche == "Esfiha":
    print("Diferente e gostoso!")
    opcao_esfiha =input("temos de carne e queijo, qual você vai querer?")
    if opcao_esfiha == "carne":
        print("Ok!Saindo uma esfiha de carne!")
    elif opcao_esfiha == "queijo":
        print("combinado! A esfiha de queijo sai em 5 min!")

#7.Exercício 3: Selecionando a estação de rádio
genero_musical = input("Qual gênero musical você prefere? (Metal, Breg funk ou Forró): ") 
if genero_musical == "Metal":
    print("Tocando agora:Black Sabbath")
    print("Aumente o volume!")
elif genero_musical == "Breg funk":
    print("Solta o grave!")
    print("Playlist oficial de Recife!")
elif genero_musical == "Forró":
    print("pra dançar xote!")
    print("Tocando os clássicos pé-de-serra")

#8. if-elif-else com variável única e blocos de várias linhas ---------------------------
#8.Exercício 1: Recompensa diária do jogador
nivel_jogador = input("Digite seu nível (Ouro, Prata, Bronze): ")
if nivel_jogador == "Ouro":
    print("Recompensa Ouro!")
    print("Pvocê ganhou 500 gemas")
elif nivel_jogador == "Prata":
    print("Recompensa Prata!")
    print("Você ganhou 5000 gemas")
elif nivel_jogador == "Bronze":
    print("Recompensa Bronze!")
    print("Você ganhou um baú de prata")
else:   
    print("Nível inválido.")
    print("Jogue mais para subir de nível!")

#8Exercício 2: Linha de ônibus para o destino
destino_usuario = input("Digite seu destino (Shopping Recife, Recife Antigo,UFPE): ")  
if destino_usuario == "Shopping Recife":
    print("Sugestão: Pegue o 1Aeroporto(pcional)'")
    print("Desça na parada em frenta ao shopping")

elif destino_usuario == "Recife Antigo":
    print("Sugestão: Pegue o 'Circular(Conde da boa Vista)'")
    print("DCaminhe pelas ruas históricas.")
elif destino_usuario == "UFPE":
    print("Sugestão: Pegue o 'Barro/Macaxeira(Várzea')")
    print("Bem-Vindo à cidade universitária!")
else:
    print("Destino não encontrado")
    print("Por favor, verifique se o nome do local está correto")

#8.Exercício 3: Escolha de pneu para a bicicleta
tipo_terreno = input("Digite o tipo de terreno (Asfalto, Trilha, Misto): ")
if tipo_terreno == "Asfalto":
    print("Recomendamos: pneu slick")
    print("menos atrito e mais velocidade")
elif tipo_terreno == "Trilha":
    print("Recomendamos: pneu com cravos")
    print("mais aderência e segurança na lama")
elif tipo_terreno == "Misto":
    print("Recomendamos: pneu híbrido")
    print("versatilidade parqa cidade e terra")
else:
    print("Tipo de terreno não encontrado")
    print("consulte um de nossos especialistas")

#9. if-elif-else com ifs aninhados ---------------------------------
#9.Exercício 1: Sistema de Matchmaking do Jogo
modo_de_jogo = input("Escolha o modo de jogo (Ranqueado ou Casual): ")
nivel_de_jogo = int(input("Digite seu nível de jog: "))

if modo_de_jogo == "Ranqueado":
    print("Procurando nova partida")
    if nivel_de_jogo > 10:
        print("Colocando você com jogadores experientes")
    else:
        print("Você jogará com iniciantes no modo ranqueado.")
elif modo_de_jogo == "Casual":  
    print("Procurando partida casual")
    if nivel_de_jogo > 5:
        print("Esta partida não contará pontos")
    else:
        print("modo de jogo inválido")
#9.Exercício 2: Planejador de Viagem de Ônibus
destino = input("Digite seu destino (Zona Sul ou Zona Norte): ")
transito_intenso = (input("Há trânsito intenso no caminho? (True/False): "))

if destino == "Zona Sul":
    print("Calculando rota para Zona Sul") 
    if transito_intenso == True:
        print("Aviso: trânsito pesado na Av. Mascarenhas de Morais")
elif destino == "Zona Norte":
    print("Calculando rota para Zona Norte")
    if transito_intenso == True:
        print("Aviso: Transito lento na Av. Norte")
else:
    print("Por favor, selecione uma região válida( Zona Sul ou Zona Norte)")

#9.Exercício 3: Personalizador de Playlist de Metal
subgenero = (input("Escolha um subgênero de Metal (Heavy Metal, Thrash Metal): "))
decada = (input("Escolha uma década (70, 80): "))
if subgenero == "Heavy Metal":
    print("montando playlist de Heavy Metal...")
    if decada == "70":
        print("Sugestão:Black Sabbath, Judas Priest.")
elif subgenero == "Thrash Metal":
    print("Montando playlist de Thrash Metal...")
    if decada == "80":
        print("Sugestão: Metallica, Slayer.")   
else:
    print("Subgênero não disponível")

#10. if: Alterando variáveis de fora para usar depois--------------------------------
#10.Exercício 1: Bônus de Troféus por Vitória
#
total_trofeus = 1200
venceu_partida = True
if venceu_partida == True:
    bonus_trofeus = 30
    total_trofeus += bonus_trofeus
print("Total de troféus agora:", total_trofeus)
#10.Exercício 2: Desconto na Passagem de Ônibus
valor_passagem = 4.10   
hoje_e_domingo = True
if hoje_e_domingo == True:
    valor_passagem = 2.50
print("Valor a pagar:", valor_passagem)
#10.Exercício 3: Custo do Reparo da Bicicleta
custo_total_reparo = 50.0
precisa_trocar_pneu = True
if precisa_trocar_pneu == True:
    custo_total_reparo += 45.0
print("O orçamento final do conserto é R$:", custo_total_reparo )

#11. if-elif: Atribuindo valores a variáveis externas-------------------------------
#Exercício 1: Recompensa por Arena
recompensa_do_dia = ""
arena_atual = (input("Digite o nome da sua arena: "))
if arena_atual == "Arena Lendária":
    recompensa_do_dia = "Baú lendário"
elif arena_atual == "Pico Congelado":
    recompensa_do_dia = "Baú Mágico"
print(f"Parabéns! A recompensa é {recompensa_do_dia}")

#11.Exercício 2: Sugestão de Lanche no Terminal
lanche_escolhido = ""
nível_de_fome = (input("Digite seu nível de fome: (muita ou pouca): "))
if nível_de_fome == "muita":
    lanche_escolhido = "cachorro-quente duplo"
elif nível_de_fome == "pouca":
    lanche_escolhido = "pastel de queijo"
print(f"OK, seu pedido é: {lanche_escolhido}")

#11.Exercício 3: Gênero Musical e Instrumento Destaque
instrumento_destaque = ""
genero_musical = (input("Digite o gênero musical (Metal, Forró): "))
if genero_musical == "Metal":
    instrumento_destaque = "guitarra com distorção"
elif genero_musical == "Forró":
    instrumento_destaque = "sanfona"
print(f"No gênero {genero_musical}, o instrumento destaque é: {instrumento_destaque}")
#__________________________________________________________________________________
#__________________________________________________________________________________     
#módulo 2: laços de repetição
#__________________________________________________________________________________
#___________________________________________________________________________________
#1. Laços while infinitos-----------------------------------------------------------
#1.Exercício 1: O P.E.K.K.A. incansável

while True:
    print("andando")
    #ctrl + c para parar o código
#1.Exercício 2: Esperando o ônibus da madrugada
    break

    
while True:
    print("ainda esperando o ônibus")       
    #ctrl + c para parar o código
#1.Exercício 3: riff eterno
    break
while True:
    print("peuum... peum... peueummm...")
    #ctrl + c para parar o código
    break
#2. Laços while com uma variável como condicional----------------------------------
#Exercício 1: Batalha em andamento
batalha_continua = True
while batalha_continua == True:
    print("tropas Lutando...")
status_batalha = (input("A batalha acabou? (sim/não): "))
if status_batalha == "sim":
    batalha_continua = False

#Exercício 2: Cadastrando itens na bicicletaria
continuar_cadastrando: True
peça =''

while continuar_cadastrando == True:
    peça = (input("Digite o nome da peça: "))
    print(f"Peça {peça} cadastrada")
    continuar = input("deseja cadastrar outras peças?(s/n) ")
    if continuar == "s" or "S":
        continuar_cadastrando = True
    elif continuar == "n" or "N":
        continuar_cadastrando = False
    break
#2.Exercício 3: Montando a Setlist do show
adicionar_musica = True
while adicionar_musica == True:
    nome_da_musica = input (f"Qual o nome da música? ")
    print(f"{nome_da_musica} adicionada à setlist")
    nova_musica = input (" adicionar nova musica? (s/n)")
    if nova_musica == "S" or "s":
        adicionar_musica = True
    elif nova_musica == "n" or "N":
        adicionar_musica = False
    break
#3. Laços while com expressão de comparação----------------------------------------
#Exercício 1: Contagem regressiva para a batalha
contador = 5
while contador > 0:
    print(f"{contador} s")
    contador -= 1
print(" BATALHA!")

#Exercício 2: Enchendo o pneu da bicicleta
pressao_pneu = 10
while pressao_pneu < 30:
    print(f" enchendo.. pressão atual{pressao_pneu}")
    pressao_pneu += 2
print(" pneu calibrado!")

#Exercício 3: Economizando para o ingresso do show
dinheiro_guardado = 20
while dinheiro_guardado < 100:
    print(f"dinheiro atual: R$ {dinheiro_guardado}. Ainda não é suficiente")
    dinheiro_guardado += 10
print("Hora de comprar o ingresso!")

#4. Laços while com expressão lógica------------------------------------------------
#Exercício 1: Destruindo a torre inimiga
vida_torre = 1000
tempo_restante = 60
while vida_torre > 0 and tempo_restante > 0:
    vida_torre -= 150
    tempo_restante -= 1
    print(f"tempo restante: {tempo_restante} vida da torre: {vida_torre}")
if vida_torre <= 0:
    print("vitória!")
else:
    print(" derrota!")

#Exercício 2: Viagem de ônibus com paradas
parada_atual = 0
saldo_vem = 15.0
while parada_atual < 10 and saldo_vem >= 1.5:
    parada_atual += 1 
    saldo_vem -= 1.5
    print(f"passando pela parada: {parada_atual} saldo: {saldo_vem}")
print("chegou")



#Exercício 3: Aprendendo uma música na guitarra
nivel_habilidade = 10
paciencia = 100
while nivel_habilidade < 50 and paciencia > 0:
    print(f"status treino paciencia: {paciencia} habilidade:{nivel_habilidade}")
    nivel_habilidade += 5
    paciencia -= 10


#5. Laços while com if dentro--------------------------------------------------------
#5.Exercício 1: Procurando o Barril de Goblins
carta_encontrada = False
while not carta_encontrada:
    carta = (input ("dige o nome de uma carta"))
    if carta == "Barril de Goblins":
        print("carta encontrada!")
        carta_encontrada = True
    else:
        print("não é essa")

#5.Exercício 2: Espera seletiva do ônibus
onibus_correto_chegou = False
while onibus_correto_chegou == False:
    onibus = (input(" qual onibus passou? "))
    if onibus == "CDU/Várzea":
        onibus_correto_chegou = True
        print("Finalmente! Embarcando...")
    else:
        print("esse não é o meu. Continuo Esperando.")

#5.Exercício 3: Caça ao Tesouro do Vinil
prateleira_atual = 1
while prateleira_atual <= 5:
    print("verificando preteleira")
    disco = (input(" o disco 'sabbath bloody sabbath' está aqui? (sim/não)"))
    if disco == "s" or "S":
        print("Achei! Dia de sorte!")
        break
    else:
        prateleira_atual += 1
#6. Laços while aninhados (um while dentro de outro)--------------------------------------
#Exercício 1: Simulador de dias e horas de jogo

