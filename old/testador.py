import time


dia = 1 
turno = 1
print_t = ""



while dia <= 3:  # Limitado a 3 dias para teste
    
    
    while turno <= 4:
        
       
        if turno == 1:
            print_t = "manhã"
        elif turno == 2:
            print_t = "tarde"
        elif turno == 3:
            print_t = "noite"
        elif turno == 4:
            print_t = "madrugada"
        
        
        print(f"Dia: {dia} | Turno da {print_t}")      
        time.sleep(1)      
        turno += 1
    
    dia += 1
    
    turno = 1
    