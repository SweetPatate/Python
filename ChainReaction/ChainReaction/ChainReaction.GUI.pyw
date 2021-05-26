import pygame
from pygame.locals import *
from algorithms import *

pygame.init()

def creerSurface():
    longeurMenue = 600
    largeurMenue = 500
    mySurface = pygame.display.set_mode((largeurMenue, longeurMenue))
    pygame.display.set_caption('Chain Reaction')
    return mySurface


def initGame(mySurface):
    nb = 2
    n = 8
    m = 5
    menu = True
    BLACK = (0, 0, 0)
    White = (255, 255, 255)
    while menu:
        rect1 = (350, 95, 50, 20)
        pygame.draw.rect(mySurface, BLACK, rect1)
        rect2 = (350, 195, 50, 20)
        pygame.draw.rect(mySurface, BLACK, rect2)
        rect3 = (350, 295, 50, 20)
        pygame.draw.rect(mySurface, BLACK, rect3)

        fontObj = pygame.font.Font('freesansbold.ttf', 20)

        nbplayer = fontObj.render('Nombre joueurs : ', True, White )
        posplayer= (50, 100)
        mySurface.blit(nbplayer, posplayer )

        nbcolonne = fontObj.render('Nombre de colonnes:', True, White )
        poscolonne = (50, 200)
        mySurface.blit(nbcolonne, poscolonne)

        nbligne = fontObj.render('Nombre lignes : ', True, White )
        posligne= (50,300)
        mySurface.blit(nbligne, posligne)

        # affichage des boutons gauche
        buttonleft = pygame.image.load("bouton gauche.png")
        buttonleft = pygame.transform.scale(buttonleft, (30, 30))

        # bouton droit
        buttonright = pygame.image.load("bouton droite.png")
        buttonright = pygame.transform.scale(buttonright, (30, 30))

        posbuttonleft1 = (300, 95)
        posbuttonright1 = (400, 95)
        posbuttonleft2 = (300, 195)
        posbuttonright2 = (400, 195)
        posbuttonleft3 = (300, 295)
        posbuttonright3 = (400, 295)

        mySurface.blit(buttonleft, posbuttonleft1)
        mySurface.blit(buttonleft, posbuttonleft2)
        mySurface.blit(buttonleft, posbuttonleft3)

        mySurface.blit(buttonright, posbuttonright1)
        mySurface.blit(buttonright, posbuttonright2)
        mySurface.blit(buttonright, posbuttonright3)

        startbutton = pygame.image.load("button_start.png")
        startbutton = pygame.transform.scale(startbutton, (136,52))
        postartbutton = (182,475)
        mySurface.blit(startbutton, postartbutton)


        nbplayer = fontObj.render(str(nb), True, White)
        posnb = (360, 95)
        mySurface.blit(nbplayer, posnb)
        zonenb = pygame.Rect((350,95),(136,52))


        nbcolws = fontObj.render(str(m), True, White)
        poscolws = (360, 195)
        mySurface.blit(nbcolws, poscolws)
        zonecowls = pygame.Rect((350, 195), (30, 30))


        nblines = fontObj.render(str(n), True, White)
        poslines = (360, 295)
        mySurface.blit(nblines, poslines)
        zonelines = pygame.Rect((350, 295), (30, 30))

        zonebuttonleft1 = pygame.Rect((300, 95), (30, 30))
        zonebuttonleft2 = pygame.Rect((300, 195), (30, 30))
        zonebuttonleft3 = pygame.Rect((300, 295), (30, 30))

        zonebuttonright1 = pygame.Rect((400, 95), (30, 30))
        zonebuttonright2 = pygame.Rect((400, 195), (30, 30))
        zonebuttonright3 = pygame.Rect((400, 295), (30, 30))

        zoneStart = pygame.Rect((225, 475), (60, 60))

        for event in pygame.event.get():
            if event.type == QUIT:
                menu = False
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                if zonebuttonleft1.collidepoint(x,y):
                    pygame.draw.rect(mySurface, BLACK, (360, 95, 30, 30),0)
                    if nb != 1:
                        nb -= 1
                    mySurface.blit(nbplayer, posnb)
                    print(nb)

                if zonebuttonright1.collidepoint(x, y):
                    pygame.draw.rect(mySurface, BLACK, (360, 95, 30, 30), 0)
                    if nb < 8:
                        nb +=1
                    mySurface.blit(nbplayer, posnb)
                    print(nb)

                if zonebuttonleft2.collidepoint(x, y):
                    if m != 3:
                        m -=1
                    print(m)

                if  zonebuttonright2.collidepoint(x, y):
                    if m < 15:
                        m += 1
                    print(m)

                if zonebuttonleft3.collidepoint(x, y):
                    if n != 3:
                        n -= 1
                    print(n)

                if zonebuttonright3.collidepoint(x, y):
                    if n < 10:
                        n += 1
                    print(n)

                if zoneStart.collidepoint(x,y):
                    menu = False

        pygame.display.update()
    return nb, n, m


def drawBoard(mySurface,n,m,player):
    White = (255, 255, 255)
    Blue = (0, 0, 255)
    Brown = (165, 42, 42)
    Green = (144, 238, 144)
    Grey = (128, 128, 128)
    Purple = (128, 0, 128)
    Red = (255, 0, 0)
    Yellow = (255, 255, 0)
    nbcolwslines = m + 1
    nblignelines = n + 1
    largeurcase = 80
    hauteurcase = 80
    if player == 1:
        for x in range(nbcolwslines):
            pygame.draw.line(mySurface, Blue, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
        for y in range(nblignelines):
            pygame.draw.line(mySurface, Blue, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))

    if player == 2:
        for x in range(nbcolwslines):
            pygame.draw.line(mySurface, Red, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
        for y in range(nblignelines):
            pygame.draw.line(mySurface, Red, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))

    if player == 3:
        for x in range(nbcolwslines):
            pygame.draw.line(mySurface, Green, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
        for y in range(nblignelines):
            pygame.draw.line(mySurface, Green, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))

    if player == 4:
            for x in range(nbcolwslines):
                pygame.draw.line(mySurface, Yellow, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
            for y in range(nblignelines):
                pygame.draw.line(mySurface, Yellow, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))

    if player == 5:
        for x in range(nbcolwslines):
            pygame.draw.line(mySurface, Purple, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
        for y in range(nblignelines):
            pygame.draw.line(mySurface, Purple, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))

    if player == 6:
        for x in range(nbcolwslines):
            pygame.draw.line(mySurface, Brown, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
        for y in range(nblignelines):
            pygame.draw.line(mySurface, Brown, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))

    if player == 7:
        for x in range(nbcolwslines):
            pygame.draw.line(mySurface, White, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
        for y in range(nblignelines):
            pygame.draw.line(mySurface, White, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))

    if player == 8:
        for x in range(nbcolwslines):
            pygame.draw.line(mySurface, Grey, (x * largeurcase, 0), (x * largeurcase, n * largeurcase))
        for y in range(nblignelines):
            pygame.draw.line(mySurface, Grey, (0, (y * hauteurcase)), (m * hauteurcase, (y * hauteurcase)))


def drawCell(nb, m, n, gameBoard,mySurface):
    # joueur 1 = bleu
    bleu1 = pygame.image.load('image/bleu1.jpg')
    bleu2 = pygame.image.load('image/bleu2.jpg')
    bleu3 = pygame.image.load('image/bleu3.jpg')

    # joueur 2 = rouge
    rouge1 = pygame.image.load('image/rouge1.jpg')
    rouge2 = pygame.image.load('image/rouge2.jpg')
    rouge3 = pygame.image.load('image/rouge3.jpg')

    # joueur 3 = vert
    vert1 = pygame.image.load('image/vert1.jpg')
    vert2 = pygame.image.load('image/vert2.jpg')
    vert3 = pygame.image.load('image/vert3.jpg')

    # joueur 4 = jaune
    jaune1 = pygame.image.load('image/jaune1.jpg')
    jaune2 = pygame.image.load('image/jaune2.jpg')
    jaune3 = pygame.image.load('image/jaune3.jpg')

    # joueur 5 = violet
    violet1 = pygame.image.load('image/violet1.jpg')
    violet2 = pygame.image.load('image/violet2.jpg')
    violet3 = pygame.image.load('image/violet3.jpg')

    # joueur 6 = marron
    marron1 = pygame.image.load('image/marron1.jpg')
    marron2 = pygame.image.load('image/marron2.jpg')
    marron3 = pygame.image.load('image/marron3.jpg')

    # joueur 7 = blanc
    blanc1 = pygame.image.load('image/blanc1.jpg')
    blanc2 = pygame.image.load('image/blanc2.jpg')
    blanc3 = pygame.image.load('image/blanc3.jpg')

    # joueur 8 = gris
    gris1 = pygame.image.load('image/gris1.jpg')
    gris2 = pygame.image.load('image/gris2.jpg')
    gris3 = pygame.image.load('image/gris3.jpg')

    for joueur in range(1, nb+1):
        for x in range(m):
            for y in range(n):
                if gameBoard[x][y][0] == 1:  # pose pion du joueur 1
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(bleu1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(bleu2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(bleu3, (x * 80 + 2, y * 80 + 2))

                if gameBoard[x][y][0] == 2:  # pose pion du joueur 2
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(rouge1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(rouge2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(rouge3, (x * 80 + 2, y * 80 + 2))

                if gameBoard[x][y][0] == 3:  # pose pion du joueur 3
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(vert1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(vert2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(vert3, (x * 80 + 2, y * 80 + 2))

                if gameBoard[x][y][0] == 4:  # pose pion du joueur 4
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(jaune1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(jaune2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(jaune3, (x * 80 + 2, y * 80 + 2))

                if gameBoard[x][y][0] == 5:  # pose pion du joueur 5
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(violet1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(violet2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(violet3, (x * 80 + 2, y * 80 + 2))

                if gameBoard[x][y][0] == 6:  # pose pion du joueur 6
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(marron1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(marron2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(marron3, (x * 80 + 2, y * 80 + 2))

                if gameBoard[x][y][0] == 7:   # pose pion du joueur 7
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(blanc1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(blanc2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(blanc3, (x * 80 + 2, y * 80 + 2))

                if gameBoard[x][y][0] == 8:  # pose pion du joueur 8
                    if gameBoard[x][y][1] == 1:
                        mySurface.blit(gris1, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 2:
                        mySurface.blit(gris2, (x * 80 + 2, y * 80 + 2))

                    if gameBoard[x][y][1] == 3:
                        mySurface.blit(gris3, (x * 80 + 2, y * 80 + 2))
    pygame.display.update()

def chainReactionGUI():
    mySurface = creerSurface()
    nb, n, m = initGame(mySurface)
    gameBoard = newBoard(n, m)
    player = 1
    inProgress = True
    pygame.display.set_mode((m * 80, n * 80))
    while inProgress:
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = event.pos[0]  # detecte ou tu clique
                    y = event.pos[1]
                    i = x // 80  # indique sur quel case tu clique
                    j = y // 80
                    print(i, j)

                    verif = possible(gameBoard, n, m, i, j, player)
                    if verif:
                        print("Oui")
                        put(gameBoard, n, m, i, j, player)
                        display(gameBoard, n, m)
                        player = player + 1

                    else:
                        print('Non')

                    mySurface.fill((0,0,0))
        if player == nb + 1:
            player = 1
        drawBoard(mySurface, n, m, player)
        drawCell(nb, m, n, gameBoard, mySurface)
        pygame.display.update()

chainReactionGUI()
