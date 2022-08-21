import os
import random

playerType = 1
playAgain = "s"
winner = " "
rounds = 0
maxRound = 9
board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def menu():
    global board
    global rounds
    os.system("cls")
    print("   0    1    2")
    print("0" + " | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | ") 
    print('----------------')
    print("1" + " | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | ") 
    print('----------------')
    print("2" + " | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | ") 
    print('----------------')
    print("Jogadas restantes: " + str(rounds) )

def playerGame():
    global playerType
    global rounds
    global maxRound
    
    
    if playerType == 1 and rounds<maxRound:
        try:
            lines = int(input('digite o numero da linha...: '))
            coluns = int(input('digite o numero da coluna...: '))
            while board[lines][coluns] != " ":
                lines = int(input('digite o numero da linha...: '))
                coluns = int(input('digite o numero da coluna...: '))
            board[lines][coluns] = "X"
            playerType = 2
            rounds += 1
        except:
            print("Jogada inválida")
            os.system("pause")


def cpuPlayer():
    global rounds
    global playerType
    global maxRound
    if playerType == 2 and rounds<maxRound:
        lines = random.randrange(0,3)
        coluns = random.randrange(0,3)
        while board[lines][coluns] != " ":
            lines = random.randrange(0,3)
            coluns = random.randrange(0,3)
        board[lines][coluns] = "O"
        rounds+=1
        playerType = 1

def verifyVictory():
    global board
    win = 'n'
    symbols = ["X", "O"]   
    for s in symbols:
        win = 'n'
        il = ic = 0  
        #Verify lines
        while il<3:
            aux=0
            ic=0
            while ic<3:
                if board[il][ic] == s:
                    aux+=1
                ic+=1
            if aux == 3:
                win = s
                break
            il+=1

        if win != 'n':
            break
        #verify coluns
        il = ic = 0  
        while ic<3:
            aux=0
            il=0
            while il<3:
                if board[il][ic] == s:
                    aux+=1
                il+=1
            if aux == 3:
                win = s
                break
            ic+=1

        if win != 'n':
            break
        #verify diagonals 1
        aux = 0
        idiag = 0

        while idiag<3:
            if board[idiag][idiag] == s:
                aux+=1
            idiag+=1
        if aux == 3:
            win = s
            break
        #verify diagonals 2
        aux = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if board[idiagl][idiagc] == s:
                aux+=1
            idiagl+=1
            idiagc-=1
        if aux == 3:
            win = s
            break
    return win
                
def redefined():
    global board
    global rounds
    global playerType
    global maxRound
    global winner
    playerType = 1
    playAgain = "s"
    rounds = 0
    winner = ""
    maxRound = 9
    board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]   


while playAgain == "s":
    while True:
        menu()
        playerGame()
        cpuPlayer()
        winner = verifyVictory()
        if winner != 'n' or rounds>=maxRound:
            break
    print("Fim do jogo")
    if winner == 'X':
        print("Resultado: Você venceu!")
    elif winner == 'O':
        print('Resultado: A CPU venceu')
    else:
        print("Resultado: Empate!")
    playAgain = input("Digite [s] para continuar ou [n] para sair: " )
    redefined()

