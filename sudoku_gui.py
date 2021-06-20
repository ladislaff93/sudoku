import pygame as pg
import sys
from pygame.constants import KEYDOWN, K_DELETE, K_LEFT, K_SPACE, K_UP
from sudoku_engine import board
from sudoku_engine import sudoku_solver
from sudoku_engine import valid_n
from sudoku_engine import empty_space

pg.init()
pg.display.set_caption('Sudoku') 
SIZE = 500
FPS = 60
BORDER_C = 'black'
BACKGROUND_C = 'white'
BORDER_M = 5
BORDER_M_2 = 2
SQ_SIZE = SIZE/len(board)
FONT = pg.font.SysFont(None, int(SIZE*0.1))
screen = pg.display.set_mode((SIZE,SIZE))


def grid():
    pg.draw.rect(screen, pg.Color(BORDER_C), pg.Rect(BORDER_M_2,BORDER_M_2,SIZE,SIZE),BORDER_M)
    i = 1   
    while ((SIZE/9)*i) < SIZE:
        line_width = 1 if i%3 !=0 else 5
        pg.draw.line(screen, pg.Color(BORDER_C), pg.Vector2(((SIZE/9)*i)+BORDER_M_2,BORDER_M), pg.Vector2(((SIZE/9)*i)+BORDER_M_2,SIZE), line_width)
        pg.draw.line(screen, pg.Color(BORDER_C), pg.Vector2(BORDER_M,((SIZE/9)*i)+BORDER_M_2), pg.Vector2(SIZE,((SIZE/9)*i)+BORDER_M_2), line_width)
        i += 1


def numbers(possible_moves):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] !=0:
                if (r,c) not in possible_moves:
                    n_text = FONT.render(str(board[r][c]), True, pg.Color('black'))
                    screen.blit(n_text, pg.Vector2(((c*SQ_SIZE)+SQ_SIZE*0.4), (r*SQ_SIZE)+SQ_SIZE*0.25))
                else:
                    n_text = FONT.render(str(board[r][c]), True, pg.Color('blue'))
                    screen.blit(n_text, pg.Vector2(((c*SQ_SIZE)+SQ_SIZE*0.4), (r*SQ_SIZE)+SQ_SIZE*0.25))


def main():
    move_log = []
    possible_moves = []
    del_values = []
    sel_sq = tuple()
    temporary_value = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
               possible_moves.append((r,c)) 

    run = True 
    while run:
        clock = pg.time.Clock()
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                m_x, m_y = pg.mouse.get_pos()                       
                sq_r = int(m_y/SQ_SIZE)
                sq_c = int(m_x/SQ_SIZE)

                if (sq_r,sq_c) in possible_moves:

                    if sel_sq == (sq_r,sq_c):
                        sel_sq = () 

                    else:
                        sel_sq = (sq_r,sq_c)

            if event.type == pg.KEYDOWN:
                keys = {0:pg.K_KP0, 1:pg.K_KP1, 2:pg.K_KP2, 3:pg.K_KP3, 4:pg.K_KP4,
                        5:pg.K_KP5, 6:pg.K_KP6, 7:pg.K_KP7, 8:pg.K_KP8, 9:pg.K_KP9
                        }
                for k,v in keys.items():
                    if event.key == v:
                        temporary_value = k

                if event.key == K_DELETE:               
                    del_values.append(sel_sq)

                if event.key == K_SPACE:
                    sudoku_solver(board)                 


        screen.fill(pg.Color(BACKGROUND_C))
        grid()
        numbers(possible_moves)
        if len(sel_sq) != 0:
            if valid_n(board, temporary_value, sel_sq[0], sel_sq[1]):
                move_log.append(sel_sq)
                board[sel_sq[0]][sel_sq[1]] = temporary_value

        if len(del_values) != 0 and len(sel_sq) != 0:
            for d_move in del_values:
                if d_move in possible_moves:
                        board[sel_sq[0]][sel_sq[1]] = 0   
                        del_values.remove(d_move)

        pg.display.update()
        pg.display.flip()
    pg.quit()


main()