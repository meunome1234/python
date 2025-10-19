#mini projeto5
#-----------------------------
#--formatação de texto--------
G = '\033[32m' # green - verde
B = '\033[34m' # blue - azul
Y = '\033[33m' # yellow - amarelo
C = '\033[36m' # cyan - ciano
W = '\033[37m' # white - branco
P =  '\033[1;35m' # purple - roxo 
ql = "\n" #quebra de linha
#------------------------------

#------- início da conversa com o usuário ---------
print(f"SIMULADOR DE INVESTIMENTOS")
print(f"Olá, vou te ajudar a simular as possibilidadesde investimentos{ql}{ql}")
print(f"Pra começar, quero te dizer que as {B}taxas anuais{W} que estou utilizando são:")
print(f"{B}IPCA{W}(inflação):{P} 5.53%{W}")
print(f"{B}CDI{W}(Jurus){W}.....{P} 14.65%{W}")
print(f"{B}Poupança{W}:......{P} 6.00%{W}{ql}")
#----
valor_investimento = input(f"Agora me informa o valor em reais que você quer investir:{G} R$ ")
print(f"{W}Ok, registrei o valor do seu investimento.")



