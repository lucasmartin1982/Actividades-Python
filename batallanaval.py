matriz = [
    ["-", "-", "-", "-", "-"],  #0
    ["-", "-", "-", "-", "-"],  #1
    ["-", "-", "-", "-", "-"],  #2
    ["-", "-", "-", "-", "-"],  #3
    ["-", "-", "-", "-", "-"],  #4

]
def pantallajugador1():
    pantalla= f"""

       1  2  3  4  5
    a  {matriz[0][0]}  {matriz[0][1]}  {matriz[0][2]}  {matriz[0][3]}  {matriz[0][4]}
    b  {matriz[1][0]}  {matriz[1][1]}  {matriz[1][2]}  {matriz[1][3]}  {matriz[1][4]}
    c  {matriz[2][0]}  {matriz[2][1]}  {matriz[2][2]}  {matriz[2][3]}  {matriz[2][4]}
    d  {matriz[3][0]}  {matriz[3][1]}  {matriz[3][2]}  {matriz[3][3]}  {matriz[3][4]}
    e  {matriz[4][0]}  {matriz[4][1]}  {matriz[4][2]}  {matriz[4][3]}  {matriz[4][4]}

    """
    return pantalla

matriz2 = [
    ["-", "-", "-", "-", "-"],  #0
    ["-", "-", "-", "-", "-"],  #1
    ["-", "-", "-", "-", "-"],  #2
    ["-", "-", "-", "-", "-"],  #3
    ["-", "-", "-", "-", "-"],  #4
]
def pantallajugador2():
    pantalla= f"""

       1  2  3  4  5
    a  {matriz2[0][0]}  {matriz2[0][1]}  {matriz2[0][2]}  {matriz2[0][3]}  {matriz2[0][4]}
    b  {matriz2[1][0]}  {matriz2[1][1]}  {matriz2[1][2]}  {matriz2[1][3]}  {matriz2[1][4]}
    c  {matriz2[2][0]}  {matriz2[2][1]}  {matriz2[2][2]}  {matriz2[2][3]}  {matriz2[2][4]}
    d  {matriz2[3][0]}  {matriz2[3][1]}  {matriz2[3][2]}  {matriz2[3][3]}  {matriz2[3][4]}
    e  {matriz2[4][0]}  {matriz2[4][1]}  {matriz2[4][2]}  {matriz2[4][3]}  {matriz2[4][4]}

    """
    return pantalla

posicion = {
    'a1': [0, 0], 'a2': [0, 1], 'a3': [0, 2], 'a4': [0, 3], 'a5': [0, 4],
    'b1': [1, 0], 'b2': [1, 1], 'b3': [1, 2], 'b4': [1, 3], 'b5': [1, 4],
    'c1': [2, 0], 'c2': [2, 1], 'c3': [2, 2], 'c4': [2, 3], 'c5': [2, 4],
    'd1': [3, 0], 'd2': [3, 1], 'd3': [3, 2], 'd4': [3, 3], 'd5': [3, 4],
    'e1': [4, 0], 'e2': [4, 1], 'e3': [4, 2], 'e4': [4, 3], 'e5': [4, 4]

}

print(pantallajugador1())
print ("Jugador 1 elegir posicion barco de 3 lugares horizontal o vertical dentro de la matriz de 5x5:")
while True:    
    error1 = True
    while error1 == True:
        posini1 = str(input("Posicion inicial:"))
        posfin1 = str(input("Posicion final:"))
        if (posini1 in posicion) and (posfin1 in posicion):
            break
        else:
            print("Posicion no valido/as")

    if ((abs(posicion[posini1][0] - posicion[posfin1][0])) == 2 or abs((posicion[posini1][1] - posicion[posfin1][1])) == 2) and ((posicion[posini1][0] == posicion[posfin1][0]) or (posicion[posini1][1] == posicion[posfin1][1])):
        if (abs(posicion[posini1][1] - posicion[posfin1][1])) == 2:            
            for x in range(3):
                if (posicion[posini1][1] - posicion[posfin1][1]) < 0:
                    matriz[posicion[posini1][0]][posicion[posini1][1]+x] = "o"
                else:
                    matriz[posicion[posini1][0]][posicion[posini1][1]-x] = "o"
        else:
            for x in range(3):
                if (posicion[posini1][0] - posicion[posfin1][0]) < 0:
                    matriz[posicion[posini1][0]+x][posicion[posini1][1]] = "o"
                else:
                    matriz[posicion[posini1][0]-x][posicion[posini1][1]] = "o"
        break
    else:
        print("Longitud incorrecta, deben ser 3 espacios en vertical u horizontal")

print(pantallajugador2())
print ("Jugador 2 elegir posicion barco de 3 lugares horizontal o vertical dentro de la matriz de 5x5:")
while True:    
    error1 = True
    while error1 == True:        
        posini2 = str(input("Posicion inicial:"))
        posfin2 = str(input("Posicion final:"))
        if (posini2 in posicion) and (posfin2 in posicion):
            break
        else:
            print("Posicion no valido/as")

    
    if ((abs(posicion[posini2][0] - posicion[posfin2][0])) == 2 or abs((posicion[posini2][1] - posicion[posfin2][1])) == 2) and ((posicion[posini2][0] == posicion[posfin2][0]) or (posicion[posini2][1] == posicion[posfin2][1])):
        if (abs(posicion[posini2][1] - posicion[posfin2][1])) == 2:            
            for x in range(3):
                if (posicion[posini2][1] - posicion[posfin2][1]) < 0:
                    matriz2[posicion[posini2][0]][posicion[posini2][1]+x] = "o"
                else:
                    matriz2[posicion[posini2][0]][posicion[posini2][1]-x] = "o"
        else:
            for x in range(3):
                if (posicion[posini2][0] - posicion[posfin2][0]) < 0:
                    matriz2[posicion[posini2][0]+x][posicion[posini2][1]] = "o"
                else:
                    matriz2[posicion[posini2][0]-x][posicion[posini2][1]] = "o"
        break
    else:
        print("Longitud incorrecta, deben ser 3 espacios en vertical u horizontal")
espaciado = """







"""

print(espaciado)

c1 = 0
c2 = 0
while c1 < 3 and c2 < 3:
    while True:    
        error1 = True        
        while error1 == True:
            jugada1 = input("JUGADOR 1 ingresar fila(letra) y columna(numero):")
            if (jugada1 in posicion):
                if matriz2[posicion[jugada1][0]][posicion[jugada1][1]] == "o":
                    print("barco averiado")
                    matriz2[posicion[jugada1][0]][posicion[jugada1][1]] == "x"
                    c1 +=1
                    error1 = False
                else:
                    print("Agua")
                    error1 = False
            else:
                print("Posicion no valido/as")
        error2 = True
        while error2 == True and c1 < 3:
            jugada2 = input("JUGADOR 2 ingresar fila(letra) y columna(numero):")
            if (jugada2 in posicion):
                if matriz[posicion[jugada2][0]][posicion[jugada2][1]] == "o":
                    print("barco averiado")
                    matriz[posicion[jugada2][0]][posicion[jugada2][1]] == "x"
                    c2 +=1
                    error2 = False
                else:
                    print("Agua")
                    error2 = False
            else:
                print("Posicion no valido/as")       
        if c1 == 3:
            print("gana el 1")
            break
        if c2 == 3:
            print("gana el 2")
            break

print("Fin Juego")