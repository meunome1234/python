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
i = '\033[3m' # italico
r = '\033[0m' # reset
#------------------------------

#variaveis---------------
taxa = None
var_cdb = False
#--------------------------------------------------
    #missão1: tipo de investimento
#--------------------------------------------------

#------- início da conversa com o usuário ---------
print(f"SIMULADOR DE INVESTIMENTOS")
print(f"Olá, vou te ajudar a simular as possibilidadesde investimentos{ql}{ql}")
print(f"Pra começar, quero te dizer que as {B}taxas anuais{W} que estou utilizando são:")
print(f"{B}IPCA{W}(inflação):{P} 5.53%{W}")
print(f"{B}CDI{W}(Jurus){W}.....{P} 14.65%{W}")
print(f"{B}Poupança{W}:......{P} 6.00%{W}{ql}")
#----
valor_investimento = input(f"Agora me informa o valor em reais que você quer investir:{G} R$ ")
print(f"{r}Ok, registrei o valor do seu investimento.{ql}{ql}")

#---------- opções de investimento ------------
print(f"Essas são as opções de investimento que tenho sisponíveis para você:")
print(f" [A]{B}CDB{W} valendo 100% do CDI, taxa final de {P} 14.65%{W}")
print(f" [B]{B}CDB{W} valendo 110% do CDI, taxa final de {P} 16.12%{W}")
print(f" [B]{B}CDB{W} valendo 120% do CDI, taxa final de {P} 17.58%{W}")
print(f" [B]{B}LCA{W} valendo  95% do CDI, taxa final de {P} 13.92%{W}")
print(f"{i}Obs.: Lembre que o CDB retém ir na fonte, enquanto LCA não.{r}")
# -------------seleção da opção--------------------------
opcao = input(f"{ql}Qual o investimento que você quer fazer? (A,B,C ou D){G}")
print(f"{r}{i}ok, registrei sua opção de investimento{r}{ql}{ql}")
#--------------condicionais da seleção ------------------------------
#letra A---CDB 100% do CDI---
if opcao == "A" or opcao == "a":
    var_cdb = True
    taxa = 14.65
    
elif opcao == "B" or opcao == "b":
    var_cdb = True
    taxa = 16.12

elif opcao == "C" or opcao == "c":
    var_cdb = True
    taxa = 17.58
elif opcao == "D" or opcao == "d":
    var_cdb = False
    taxa = 13.92
else:
    print(f"Opção inválida! Tente novamente.")
#-------mensagem cdb -----
if var_cdb == True:
    print(f"{W}Como você escolheu um CDB vou te lembrar as taxas regressivas de iR:")
    print(f"Até 6 messes:.....{P} 22.50%{W}")
    print(f"Até 12 meses:.....{P} 20.00%{W}")
    print(f"Até 24 meses:.....{P} 17.50%{W}")
    print(f"acima de 24 meses:{P} 15.00%{W}")

#------------------------------------------------
#-------fim missão 1 ----------------------------
#------------------------------------------------
    #missão 2: tempo e resultado 
vartempo = input(f"Quanto tempo você gostaria de esparar para resgatar esse investimento?(em meses){B}")
print(f"{r}Ok, registrei o tempo para resgate.{ql}{ql}")

#condicionais vartempo
if vartempo <= "6":
    ir = 22.5
elif vartempo > "6" and vartempo <= "12":
    ir = 20.0
elif vartempo > "12" and vartempo <= "24":
    ir = 17.5
else:
    ir = 15.0

#resposta----
print(f"TAXAS UTILIZADAS")
print(f"Taxa de IR aplicada.......{P} {ir}.:2F%{W}")
print(f"taxa de rendimento anual..{P} {taxa}%.2F{W}")
print(f"Taxa de rendimento mensal..{P} {(taxa/12):.2F}%{W}")
