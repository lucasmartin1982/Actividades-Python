

matriz = [
    ["-", "-", "-"],  #0
    ["-", "-", "-"],  #1
    ["-", "-", "-"],  #2
]

posiciones = {
    'a1': [0, 0], 'a2': [0, 1], 'a3': [0, 2],
    'b1': [1, 0], 'b2': [1, 1], 'b3': [1, 2],
    'c1': [2, 0], 'c2': [2, 1], 'c3': [2, 2]
}

ganador = False

def mostrarpantalla():
    pantalla= f"""

       1  2  3
    a  {matriz[0][0]}  {matriz[0][1]}  {matriz[0][2]}
    b  {matriz[1][0]}  {matriz[1][1]}  {matriz[1][2]}
    c  {matriz[2][0]}  {matriz[2][1]}  {matriz[2][2]}

    """
    return pantalla

def esganador1():
    ganadorv = False
    ganadorh = False
    ganadord = False
    c = 0
    for j in range (0,3):
        for f in range (0,3):
            if matriz[f][c] == "X":
                ganadorv = True
            else:
                ganadorv = False
                c +=1
                break
        if ganadorv == True:
            break
    c = 0
    for j in range (0,3):
            for f in range (0,3):
                if matriz[c][f] == "X":
                    ganadorh = True
                else:
                    ganadorh = False
                    c +=1
                    break
            if ganadorh == True:
                break
    d = 2
    for i in range (3):
        if matriz[i][i] == "X" or matriz[d][i] == "X":
            ganadord = True
        else:
            ganadord = False
            break
        d -= 1
    
    
    return ganadorv or ganadorh or ganadord

def esganador2():
    ganadorv = False
    ganadorh = False
    c = 0
    for j in range (0,3):
        for f in range (0,3):
            if matriz[f][c] == "O":
                ganadorv = True
            else:
                ganadorv = False
                c +=1
                break
        if ganadorv == True:
            break
    c = 0
    for j in range (0,3):
            for f in range (0,3):
                if matriz[c][f] == "O":
                    ganadorh = True
                else:
                    ganadorh = False
                    c +=1
                    break
            if ganadorh == True:
                break
    d = 2
    for i in range (3):
        if matriz[i][i] == "O" or matriz[d][i] == "O":
            ganadord = True
        else:
            ganadord = False
            break
        d -= 1
    return ganadorv or ganadorh or ganadord


while True:

    print(mostrarpantalla())
    
    error1 = True
    while error1 == True:
        jugador1 = str(input("Jugador1 ingresar una letra(fila) y un numero (columna):"))
        if jugador1 in posiciones:    
            if matriz[posiciones[jugador1][0]][posiciones[jugador1][1]] == "X" or matriz[posiciones[jugador1][0]][posiciones[jugador1][1]] == "O":
                error1 = True
                print("Espacio ya elegido, pruebe otra vez")
            else:
                error1 = False               
                matriz[posiciones[jugador1][0]][posiciones[jugador1][1]] = "X"       
        else:
            print("posicion no valida")
            error1 = True
    print(mostrarpantalla())
    
    error2 = True
    while error2 == True and esganador1() == False:
        jugador2 = str(input("Jugador2 ingresar una letra(fila) y un numero (columna):"))
        if jugador2 in posiciones:    
            if matriz[posiciones[jugador2][0]][posiciones[jugador2][1]] == "X" or matriz[posiciones[jugador2][0]][posiciones[jugador2][1]] == "O":
                error2 = True
                print("Espacio ya elegido, pruebe otra vez")
            else:
                error2 = False               
                matriz[posiciones[jugador2][0]][posiciones[jugador2][1]] = "O"       
        else:
            print("posicion no valida")
            error2 = True
            
    if esganador1():
        print(mostrarpantalla())
        print ('gana Jugador 1')
        break
    if esganador2():
        print(mostrarpantalla())
        print ('gana Jugador 2')
        break









