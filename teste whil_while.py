dia = 1
turno = 1
while dia <= 3:
    if dia == 1:
        print("dia 1")
        dia += 1
    elif dia == 2:
        print("dia 2")
        dia += 1
    elif dia == 3:
        print("dia 3")
        dia = 1

    while turno <= 4:
        if turno == 1:
            print("turno manhã")
            turno += 1
        elif turno == 2:
            print("turno tarde")
            turno += 1
        elif turno == 3:
            print("turno noite")
            turno += 1
        else:
            print ("turno madrugada")
            turno = 1