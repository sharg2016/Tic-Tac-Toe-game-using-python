import pygame,sys
import numpy as np

pygame.init()

#game_constant
WIDTH = 400
HEIGHT = 400
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 40
CIRCLE_WIDTH = 10
CROSS_WIDTH = 16
SPACE       = 36

#colors
RED = (255,0,0)
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)
CIRCLE_COLOR = (239, 231 ,200)
CROSS_COLOR = (66,66,66)
font_color=(0,150,250)



#output screen
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption( 'TIC-TAC-TOE')
screen.fill( BG_COLOR)


board = np.zeros((BOARD_ROWS , BOARD_COLS))



def draw_lines():
    #first horizontal line.......
    pygame.draw.line( screen , LINE_COLOR ,(0,134) , (400,134) , LINE_WIDTH)
    #second horizontal line.....
    pygame.draw.line(screen, LINE_COLOR, (0, 268), (400, 268), LINE_WIDTH)
    #first Vertical Lines.........
    pygame.draw.line(screen, LINE_COLOR, (134, 0), (134, 400), LINE_WIDTH)
    # second VErtical line.........
    pygame.draw.line(screen, LINE_COLOR, (268,0), (268,400), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col  in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen , CIRCLE_COLOR , (int(col * 133 + 67) , int(row * 133 +67)) , CIRCLE_RADIUS,CIRCLE_WIDTH)

            elif board[row][col]==2:
                pygame.draw.line(screen , CROSS_COLOR , (col * 133 +SPACE , row * 133 + 133-SPACE)  , ( col * 133 +133 -SPACE , row *133+SPACE) ,CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col * 133 + SPACE , row * 133  + SPACE) , (col * 133 +133 -SPACE , row * 133 +133 - SPACE) , CROSS_WIDTH)


def  mark_squares(row  , col , player):
    board[row][col] = player

def available_squares(row , col):
    return board[row][col]==0

def is_boardfull():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==0:
                return False
    return  True

def check_win(player):
    #vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col , player)
            return True

    #horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    #asc diagonal check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #desc diagonal check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return  True

    return False

def draw_vertical_winning_line(col,player):
    posX = col * 133 + 67

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color , (posX , 10 ) , (posX , HEIGHT -10 ), 10)

def draw_horizontal_winning_line(row , player):
    posY = row * 133 +67

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color , (10 , posY), (WIDTH-10 , posY), 10)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color , ( 10 , HEIGHT - 10 ) , ( WIDTH - 10  , 10 ), 10)

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CIRCLE_COLOR
    pygame.draw.line(screen, color ,(10 , 10 ) , (WIDTH-10 , HEIGHT -10 ), 10)

def restart():
    screen.fill( BG_COLOR)
    draw_lines()
    player =1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()

player =1
game_over =False
#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // 133
            clicked_col = mouseX // 133

            if available_squares( clicked_row , clicked_col):
                mark_squares(clicked_row , clicked_col, 1)
                if player == 1:
                    if check_win(player):
                        game_over = False
                    player = 2

                elif player  == 2:
                    mark_squares(clicked_row , clicked_col , 2)
                    if check_win(player):
                        game_over = False
                    player = 1


                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()