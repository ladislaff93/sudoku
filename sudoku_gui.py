import pygame as pg

SIZE = 750,750
FPS = 60
pg.init()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption('Sudoku') 

def main():
    run = True 
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

main()