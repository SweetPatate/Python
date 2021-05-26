import copy

def newBoard(n):
    board= []
    for i in range(0,n,1):
        board.append(0)
    return board

def display() :
    for i in range(0, n, 1): #n peut être remplacer len(board)

        if board[i] == 0:

            print(". ", end='')

        if board[i] == 1:

            print("o ", end='')

        if board[i] == 2:

            print("x ", end='')
    print()

    for i in range(0, n):

        print(i + 1, end=' ')

def Turn_player(player):
    print()
    if player == 1:
        print("player blanc")
        return 2
    elif player == 2:
        print("player noir")
        return 1

def select(player,board,removed):
    if player != 1:
        a = int(input("joueur blanc choisissez votre case :")) # a est la touche enttrée
        a = a - 1
        while (a < 0) or (a > 8) or board[a]!=0 or removed.count(a) or board[a-1] == 2 and board[a+1] == 2:
            if (a < 0) or (a > 8): # en dehors de la liste
                a = int(input("joueur blanc choisissez une case entre 1 et 9:", ))
                a = a - 1
            elif board[a]!=0: # a est située sur la case d'un pion
                a = int(input("case déja occupée, choisissez une autre case :", ))
                a = a - 1
            elif removed.count(a): # a est située sur une case qui a était prise au tour précédent
                a = int(input("case prise au tour précédent:", ))
                a = a - 1

    if player != 2:
        a = int(input("joueur noir choisissez votre case :"))
        a = a - 1
        while (a < 0) or (a > 8) or board[a]!=0 or removed.count(a):
            if (a < 0) or (a > 8):
                a = int(input("joueur noir choisissez une case entre 1 et 9:", ))
                a = a - 1
            elif board[a]!=0:
                a = int(input("case déja occupée, choisissez une autre case :", ))
                a = a - 1
            if removed.count(a) :
                a = int(input("case prise au tour précédent:", ))
                a = a - 1
    return a

def put(board, n, player,a,removed):
    removed = []
    if player != 1:
        board[a] = 1

        for i in range(0, a):
            if board[i] != 2:
                break
            elif board[i] == 2:
                for j in range(n - 1, a + 1, -1):
                    if board[j] == 0:
                        break
                    elif board[j] == 1:
                        removed.append(i)
                        board[i] = 0
                        removed.append(j)
                        board[j] = 0

        for i in range(a+1, n):  # captures a droite du pion
            if board[i] == 0:  # si une case est vide break
                break
            elif board[i] == 1:  # si un pion blanc est trouver
                for j in range(i-1, a, -1):  # capture les pions entre les deux pions blancs
                    removed.append(j)
                    board[j] = 0  # comme les pions entre les deux ne sont pas 0 ils sont forcemment 2 "noir(s)"
                break
            elif i == n-1:  # si on atteint le bord de droite
                for j in range(n-1, a, -1):  # capture des pion entre le bord et le pion
                    removed.append(j)
                    board[j] = 0

        for i in range(a-1, -1, -1):  # captures a la gauche du pion
            if board[i] == 0:  # si une case est vide a gauche de a pas de capture
                break
            elif board[i] == 1:  # si un autre pion du meme joueur est present
                for j in range(i+1, a):  # capture des pions entre les deux
                    removed.append(j)
                    board[j] = 0  # comme les pions entre les deux ne sont pas 0 ils sont forcemment 2 "noir(s)"
                break
            elif i == 0:  # si on atteint le bord gauche
                for j in range(0, a):  # capture des pion entre le bord et le pion
                    removed.append(j)
                    board[j] = 0  # comme les pions entre les deux ne sont pas 0 ils sont forcemment 2 "noir(s)"
    elif player != 2:
        board[a] = 2

        for i in range(0, a):
            if board[i] != 1:
                break
            elif board[i] == 1:
                for j in range(n - 1, a + 1, -1):
                    if board[j] == 0:
                        break
                    elif board[j] == 2:
                        print(i)
                        print(j)
                        removed.append(i)
                        board[i] = 0
                        removed.append(j)
                        board[j] = 0

        for i in range(a + 1, n):  # on répéte l'opération pour le joueur 2
            if board[i] == 0:
                break
            elif board[i] == 2:
                for j in range(i - 1, a, -1):
                    removed.append(j)
                    board[j] = 0
                break
            elif i == n - 1:
                for j in range(n - 1, a, -1):
                    removed.append(j)
                    board[j] = 0

        for i in range(a - 1, -1, -1):
            if board[i] == 0:
                break
            elif board[i] == 2:
                for j in range(i + 1, a):
                    removed.append(j)
                    board[j] = 0
                break
            elif i == 0:
                for j in range(0, a):
                    removed.append(j)
                    board[j] = 0
    return removed

def end(board):  # vérifie que la partie est finie
    print()
    if board.count(0) + len(removed) == 0:

        print("fin de la partie")

        if board.count(1) > board.count(2):

            print("le joueur blancs gagne")

        elif board.count(1) < board.count(2):

            print("le joueur noir gagne")

        else:
            print("égalité")

        return False
    else:
        return True

def alak(player,board,n,a,removed):
    display()
    while end(board):
        player = Turn_player(player)
        a = select(player,board,removed)
        removed = []
        removed = put(board, n, player, a,removed)
        display()

n = 9
a = 0
board = []
board = newBoard(n)
removed = []

player = 1
# explication des régles
print("Cette version du jeu Alak a été conçue en 2001 par Alan Baljeu1.")
print("Deux joueurs s’affrontent sur un plateau unidimensionnel de n cases.")
print("Le premier joueur possède des pions blancs et le second des pions noirs.")
print("Au début de la partie toutes les cases sont vides. Les blancs commencent, puis les joueurs vont à tour de rôle poser un de leurs pions en respectant les différentes contraintes suivantes : ")
print()
print("1. Un joueur ne peut placer un pion que sur une case vide, et cette case ne doit pas avoir été occupée par l’un de ses propres pions au tour précédent (voir règle de capture à suivre).")
print("   Si un joueur ne peut plus placer de pion la partie est terminée")
print("2. Si après qu’un joueur ait placé un pion, un groupe de pions adjacents de son adversaire n’a plus de cases adjacentes vides ceux-ci sont capturés et retirés du plateau.")
print("   D’après la première règle, son adversaire ne pourra donc pas poser un pion sur l’une de ces cases au prochain tour. Par « groupe de pions » on entend « au moins un pion ». ")
print("3. Un joueur peut par contre placer un pion et constituer un groupe de pions adjacents sans cases adjacentes vides sans que ce groupe de pions soit capturé. ")

alak(player, board, n, a, removed)