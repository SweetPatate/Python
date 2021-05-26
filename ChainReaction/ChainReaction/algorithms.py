
def newBoard(n,m):
    n = 10
    m = 15
    gameBoard = [[[0 for k in range(2)] for j in range(n)] for i in range(m)]
    return gameBoard

def display(gameBoard,n , m):
    affichage = ''
    for j in range(n):
        affichage += '\n'
        for i in range(m):
            affichage += '  '
            for l in range(2):
                affichage += str(gameBoard[i][j][l])
    print(affichage)

def joueur(player, nb):
    player = player + 1
    if player >= nb:
        player = 1
    return player

def possible(gameBoard,n,m,i,j,player):
    if gameBoard[i][j][1] == 0 or gameBoard[i][j][0] == player:
        return True
    else:
        return False


def put(gameBoard,n,m,i,j,player): # va exectuer toute la pose et ce qui en decoule

    if gameBoard[i][j][1] < 4:
        gameBoard[i][j][0] = player
        gameBoard[i][j][1] += 1

    if gameBoard[0][0][1] == 2:  # coin haut gauche
        gameBoard[i][j][0] = 0
        gameBoard[i][j][1] = 0

        put(gameBoard, n, m, 0, 1, player)
        put(gameBoard, n, m, 1, 0, player)

    if gameBoard[m-1][0][1] == 2:  # coin haut droit
        gameBoard[m-1][0][0] = 0
        gameBoard[m-1][0][1] = 0

        put(gameBoard, n, m, m-1, 1, player)
        put(gameBoard, n, m, m-2, 0, player)

    if gameBoard[0][n-1][1] == 2:  # coin bas gauche
        gameBoard[0][n-1][0] = 0
        gameBoard[0][n-1][1] = 0

        put(gameBoard, n, m, 0, n-2, player)
        put(gameBoard, n, m, 1, n-1, player)

    if gameBoard[m-1][n-1][1] == 2:  # coin bas droite
        gameBoard[m-1][n-1][0] = 0
        gameBoard[m-1][n-1][1] = 0

        put(gameBoard, n, m, m-1, n-2, player)
        put(gameBoard, n, m, m-2, n-1, player)
    for x in range(1,m-1): # collonne
        for y in range(1,n-1): # ligne
        # Les Bords (Les cotés)
            if gameBoard[0][y][1] == 3:  # bord gauche
                gameBoard[0][y][0] = 0
                gameBoard[0][y][1] = 0

                put(gameBoard, n, m, 0, y-1, player)
                put(gameBoard, n, m, 0, y+1, player)
                put(gameBoard, n, m, 1, y, player)

            if gameBoard[x][0][1] == 3: # bord haut
                gameBoard[x][0][0] = 0
                gameBoard[x][0][1] = 0

                put(gameBoard, n, m, x - 1, 0, player)
                put(gameBoard, n, m, x + 1, 0, player)
                put(gameBoard, n, m, x, 1, player)

            if gameBoard[m-1][y][1] == 3: # bord droit
                gameBoard[m-1][y][0] = 0
                gameBoard[m-1][y][1] = 0

                put(gameBoard, n, m, m - 1, y - 1, player)
                put(gameBoard, n, m, m - 2, y, player)
                put(gameBoard, n, m, m - 1, y + 1, player)

            if gameBoard[x][n-1][1] == 3: # bord bas
                gameBoard[x][n-1][0] = 0
                gameBoard[x][n-1][1] = 0

                put(gameBoard, n, m, x, n - 2, player)
                put(gameBoard, n, m, x - 1, n - 1, player)
                put(gameBoard, n, m, x + 1, n - 1, player)

            if gameBoard[x][y][1] == 4: # bord bas
                gameBoard[x][y][0] = 0
                gameBoard[x][y][1] = 0

                put(gameBoard, n, m, x, y+1, player)
                put(gameBoard, n, m, x, y-1, player)
                put(gameBoard, n, m, x+1, y, player)
                put(gameBoard, n, m, x-1, y, player)


def loose(gameBoard,n,m,player):
    for ligne in range(n):
        for colonne in range(m):
            if gameBoard [ligne][colonne][0] == player:
                return False
    return True

def win(gameBoard,n,m,player):
    for ligne in range(n):
        for colonne in range(m):
            if gameBoard [ligne][colonne][1] != player and gameBoard [ligne][colonne][1] != 0:
                return False
    return True

def printBoard(gameBoard,n,m):
    for m in range(n):
        print(gameBoard[m])