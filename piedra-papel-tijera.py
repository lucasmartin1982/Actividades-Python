import random

condicion = True
while condicion:
    print("Elegir piedra, papel o tijera.")

    elecciones = ['piedra', 'papel', 'tijera']
    
    while True:
        jugador = input("Jugador: ")
        if jugador in elecciones:
            break
        else:
            print("opcion no valida")
    
    maquina = elecciones[random.randint(0, 2)]

    if jugador == maquina:
        print("Empate")
    elif (jugador == 'piedra' and maquina == 'papel') or (jugador == 'papel' and maquina == 'tijera') or (jugador == 'tijera' and maquina == 'piedra'):
        print("Gana la máquina")
    else:
        print("Gana el usuario")
    
    while True:
        respuesta = input("¿Desea jugar de nuevo? (s/n) ")
        if respuesta == "n":            
            condicion = False
            break
        elif respuesta == "s":
            condicion = True
            break
        else:
            print("respuesta no valida")         
