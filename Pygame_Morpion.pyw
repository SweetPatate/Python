import pygame, sys
from pygame.locals import *

def newBoard():
    board = [[0]*3 for i in range(3)]
    return board


def drawGame(surface):
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    surface.fill(BLACK)
    for i in range(0, 9):
        pygame.draw.rect(surface, BLUE, (int((i%3))*100+105, int((i/3))*100+105, 90, 90))

    fontObj = pygame.font.Font('freesansbold.ttf', 48)
    newGameSurface = fontObj.render('Restart', True, BLUE, BLACK)
    quitGameSurface = fontObj.render('Quit game', True, BLUE, BLACK)

    newGameRect = newGameSurface.get_rect()
    newGameRect.topleft = (450, 100)
    quitGameRect = quitGameSurface.get_rect()
    quitGameRect.topleft = (450, 150)

    surface.blit(newGameSurface, newGameRect)
    surface.blit(quitGameSurface, quitGameRect)

    return surface


def drawCross(surface, x, y):
    pygame.draw.line(surface, (0, 255, 0), (x+15, y+15), (x+85, y+85), 3)
    pygame.draw.line(surface, (0, 255, 0), (x+85, y+15), (x+15, y+85), 3)


def drawCircle(surface, x, y):
    pygame.draw.circle(surface, (255, 0, 0), (x+50, y+50), 35, 3)


def put(surface, board, player, x, y):
    if board[x][y] != 0:
        return False
    if player == 1:
        drawCross(surface, x*100+100, y*100+100)
    else:
        drawCircle(surface, x*100+100, y*100+100)
    board[x][y] = player
    return True


def drawWin(surface, color, pos1, pos2):
    pygame.draw.line(surface, color, (pos1[0]*100+150, pos1[1]*100+150), (pos2[0]*100+150, pos2[1]*100+150), 10)


def win(surface, board, player):
    for i in range(0, 3):
        if board[0][i] == player:
            if board[1][i] == player:
                if board[2][i] == player:
                    drawWin(surface, (255*(player-1), (255*(player-(player-1)*2)), 0), (0, i), (2, i))
                    return True
    for i in range(0, 3):
        if board[i][0] == player:
            if board[i][1] == player:
                if board[i][2] == player:
                    drawWin(surface, (255*(player-1), (255*(player-(player-1)*2)), 0), (i, 0), (i, 2))
                    return True
    if board[0][0] == player:
        if board[1][1] == player:
            if board[2][2] == player:
                drawWin(surface, (255 * (player - 1), (255 * (player - (player - 1) * 2)), 0), (0, 0), (2, 2))
                return True
    if board[2][0] == player:
        if board[1][1] == player:
            if board[0][2] == player:
                drawWin(surface, (255 * (player - 1), (255 * (player - (player - 1) * 2)), 0), (2, 0), (0, 2))
                return True
    return False


def updateLabel(surface, player):
    fontObj = pygame.font.Font('freesansbold.ttf', 48)
    if player > 0:
        texteSurface = fontObj.render('Le joueur '+str(player)+' est le vainqueur', True, (0, 0, 0), (0, 0, 255))
    else:
        texteSurface = fontObj.render('Match nul', True, (0, 0, 0), (0, 0, 255))
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (100, 450)
    surface.blit(texteSurface, texteRect)


def boardFull(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 0:
                return False
    return True


pygame.init()
surface = pygame.display.set_mode((800, 550))

clickableArea = list()
clickableArea.append(pygame.Rect((100, 100), (100, 100)))
clickableArea.append(pygame.Rect((200, 100), (100, 100)))
clickableArea.append(pygame.Rect((300, 100), (100, 100)))
clickableArea.append(pygame.Rect((100, 200), (100, 100)))
clickableArea.append(pygame.Rect((200, 200), (100, 100)))
clickableArea.append(pygame.Rect((300, 200), (100, 100)))
clickableArea.append(pygame.Rect((100, 300), (100, 100)))
clickableArea.append(pygame.Rect((200, 300), (100, 100)))
clickableArea.append(pygame.Rect((300, 300), (100, 100)))
newGameArea = pygame.Rect((450, 100), (300, 50))
quitGameArea = pygame.Rect((450, 150), (300, 50))

pygame.display.set_caption('Tic Tac Toe')
FPS = 60
fpsClock = pygame.time.Clock()
inProgress = True
surface = drawGame(surface)
board = newBoard()
player = 1
playable = True

while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            play = False
            if playable:
                if clickableArea[0].collidepoint((x, y)):
                    play = put(surface, board, player, 0, 0)
                elif clickableArea[1].collidepoint((x, y)):
                    play = put(surface, board, player, 1, 0)
                elif clickableArea[2].collidepoint((x, y)):
                    play = put(surface, board, player, 2, 0)
                elif clickableArea[3].collidepoint((x, y)):
                    play = put(surface, board, player, 0, 1)
                elif clickableArea[4].collidepoint((x, y)):
                    play = put(surface, board, player, 1, 1)
                elif clickableArea[5].collidepoint((x, y)):
                    play = put(surface, board, player, 2, 1)
                elif clickableArea[6].collidepoint((x, y)):
                    play = put(surface, board, player, 0, 2)
                elif clickableArea[7].collidepoint((x, y)):
                    play = put(surface, board, player, 1, 2)
                elif clickableArea[8].collidepoint((x, y)):
                    play = put(surface, board, player, 2, 2)
            if newGameArea.collidepoint((x, y)):
                surface = drawGame(surface)
                board = newBoard()
                playable = True
            elif quitGameArea.collidepoint((x, y)):
                inProgress = False
            if play:
                if win(surface, board, player):
                    updateLabel(surface, player)
                    playable = False
                elif boardFull(board):
                    updateLabel(surface, 0)
                player = 3 - player
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
