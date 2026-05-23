import pygame
import time
pygame.init()

rows = 3
columns = 3
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
winner = None
player = 'x'
linecolor = (0, 0, 0)

def checkwin():
    #write the winning conditions
    #row, column, or diagonal with the same token

    for i in range(rows):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            if board[i][0] == 'x':
                winner = 'x'
                markingrow(i)
                draw_winner(winner)
                
                return True
            else:
                winner = 'o'
                markingrow(i)
                draw_winner(winner)
                
                return True
    for i in range(columns):
        if board[0][i] == board[1][i] == board[2][i] and board[i][0] != 0:
            if board[0][i] == 'x':
                winner = 'x'
                markingcolumn(i)
                draw_winner(winner)
                
                return True
            else:
                winner = 'o'
                markingcolumn(i)
                draw_winner(winner)
                
                return True

    if board[0][0] == board[1][1] == board[2][2] and board[i][0] != 0:
        if board[0][0] == 'x':
            winner = 'x'
            markingdiagonal1()
            draw_winner(winner)
            
            return True
        else:
            winner = 'o'
            markingdiagonal1()
            draw_winner(winner)
            
            return True

    if board[0][2] == board[1][1] == board[2][0] and board[i][0] != 0:
        if board[0][2] == 'x':
            winner = 'x'
            markingdiagonal2()
            draw_winner(winner)
            
            return True
        else:
            winner = 'o'
            markingdiagonal2()
            draw_winner(winner)
            
            return True

def markingrow(rows):
    pygame.draw.line(screen, 'red', (0, 250*rows+125), (screen.get_width(), 250*rows+125), 15)

def markingcolumn(columns):
    pygame.draw.line(screen, 'red', (250*columns+125, 0), (250*columns+125, screen.get_width()), 15)

def markingdiagonal1():
    pygame.draw.line(screen, 'red', (0, 0), (screen.get_width(), screen.get_height()), 15)

def markingdiagonal2():
    pygame.draw.line(screen, 'red', (screen.get_width(), 0), (0, screen.get_height()), 15)

def drawsymbols():
    for i in range(rows):
         for j in range(columns):
            if board[i][j] == 'x':
                pygame.draw.line(screen, 'blue', (250 * j + 50, 250 * i + 50), (250 * j + 200, 250 * i + 200), 15)
                pygame.draw.line(screen, 'blue', (250 * j + 200, 250 * i + 50), (250 * j + 50, 250 * i + 200), 15)
            elif board[i][j] == 'o':
                pygame.draw.circle(screen, 'red', (250 * j + 125, 250 * i + 125), 100, 15)

def draw_winner(player):
	text = font1.render(player + " won the game", True, (0, 0, 0))
	screen.blit(text, (100, 375))

def setup():
    pygame.draw.line(screen, linecolor, (0, screen.get_height()/3), (screen.get_width(), screen.get_height()/3), 15)
    pygame.draw.line(screen, linecolor, (0, 2*screen.get_height()/3), (screen.get_width(), 2*screen.get_height()/3), 15)
    pygame.draw.line(screen, linecolor, (screen.get_width()/3, 0), (screen.get_width()/3, screen.get_height()), 15)
    pygame.draw.line(screen, linecolor, (2*screen.get_width()/3, 0), (2*screen.get_width()/3, screen.get_height()), 15)

def marksquare(rows, columns, player):
    board[rows][columns] = player

    # if player == 'x':
    #     screen.blit(x, (rows, columns))
    # elif player == 'o':
    #     screen.blit(o, (rows, columns))

def isavailablesquare(row, columns):
    if board[row][columns] == 0:
        return True
    else:
        return False

def ifboardfull():
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 0:
                return False
    return True

# print(isavailablesquare(1, 1))
# marksquare(1, 1, 'x')
# print(isavailablesquare(1, 1))

#images
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Tic-Tac-Toe")
tictactoe = pygame.image.load("tictactoe\\imgs\\tictactoe.png")
pygame.display.set_icon(tictactoe)
x = pygame.image.load("tictactoe\\imgs\\x.png")
o = pygame.image.load("tictactoe\\imgs\\o.png")
x_rect = x.get_rect()
o_rect = o.get_rect()
font1 = pygame.font.SysFont("elephant", 50)

running = True
#screen.fill((18, 53, 36))
screen.fill((255, 255, 255))

while running:
    #imgs
    #screen.blit(x, (300, 300))
    #screen.blit(o, (300, 350))
    setup()

    for event in pygame.event.get():
        #end
        if event.type == pygame.QUIT:
            running = False

        #mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = event.pos[0]
            mousey = event.pos[1]
            # print(mousex, mousey)
            clicked_row = mousey//250
            clicked_column = mousex//250
            print(mousex, mousey)

            calculated_x = 200*clicked_column+100
            calculated_y = 200*clicked_row+100

            if not ifboardfull():
                if isavailablesquare(clicked_row, clicked_column):
                    if player == 'x':
                        print(f"x marked at {clicked_row} and {clicked_row}")
                        marksquare(clicked_row, clicked_column, 'x')
                        #image_rect = x.get_rect(center=(200*clicked_column+100, 200*clicked_row+100))
                        print(f"x marked at {calculated_x} and {calculated_y}")
                        drawsymbols()
                        if checkwin():
                            running = False
                            time.sleep(2)
                        #screen.blit(x, (calculated_x, calculated_y))
                        #screen.blit(x, image_rect)
                        player = 'o'
                    elif player == 'o':
                        print(f"o is marked at {clicked_row, clicked_column}")
                        marksquare(clicked_row, clicked_column, 'o')
                        #image_rect = o.get_rect(center=(200*clicked_column+100, 200*clicked_row+100))
                        print(f"o marked at {calculated_x} and {calculated_y}")
                        drawsymbols()
                        if checkwin():
                            running = False
                            time.sleep(2)
                        #screen.blit(o, (calculated_x, calculated_y))
                        #screen.blit(o, image_rect)
                        player = 'x'
        print("The current status of board is", board)
    pygame.display.update()