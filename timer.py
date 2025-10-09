import time #puxa biblioteca de tempo
#variaveis
min = 0
seg = 0
hora = 0
#loop
while True:
    print(f"\r {hora:02} : {min:02}, : {seg:02}", end = "")
    seg +=1
    if seg >= 60:#condicional segundos
        min += 1
        seg = 0

        if min >= 60:#condicional minutos
            min = 0
            hora +=1
            if hora >= 24:
                hora = 0
    
    time.sleep(0.001)

    
    
    
    
    