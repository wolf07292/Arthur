import pygame as pg
b = (0,) * 3
g = (100,) * 3
w = (255,) * 3
r = (255,0,0)
y = (255,255,0)
l = (0,200,200)
cr = '#046582'
ci = '#e4bad4'

def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pg.draw.circle(sc, ci, (x, y), (size - 3) // 2, 3)

def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    pg.draw.line(sc, cr, (x, y), (x + size - 3, y + size - 3), 3)
    pg.draw.line(sc, cr, (x + size - 3, y - 3), (x, y + size - 3), 3)

def is_end(board):
    for i in range(3):
        if check_i_col(board, i):
            return 'col', i
        if check_i_line(board, i):
            return 'line', i
    if check_main_diag(board):
        return 'diag', 2
    return None

def check_i_line(x, i):
    if x[i][0] == x[i][1] == x[i][2] != 0:
        return True
    else:
        return False

def check_i_col(x, i):
    if x[0][i] == x[1][i] == x[2][i] != 0:
        return True
    else:
        return False

def check_main_diag(x):
    if x[0][0] == x[1][1] == x[2][2] != 0:
        return True
    else:
        return False

def check_secondary_diag(x):
    if x[0][2] == x[1][1] == x[2][0] != 0:
        return True
    else:
        return False



class Board:
    def __init__(self,W,H,size):
        self.W, self.H = W , H
        self.size = size
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.move = 1
    def c(self,mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        if self.board[y][x] == 0:
            self.board[y][x] = self.move
            self.move = -self.move

    def re(self,screen):
        pg.draw.line(screen, g, (0,200),(self.W, 200),2)
        pg.draw.line(screen, g, (0,400),(self.W, 400))
        pg.draw.line(screen, g, (200,0),(200, self.H))
        pg.draw.line(screen, g, (400,0),(400, self.H))
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen, x, y, self.size)
pg.init()
screen = pg.display.set_mode((600,600))
bo = Board(600,600,200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            bo.c(event.pos)

    screen.fill(w)
    bo.re(screen)
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE] or bo.check_end():
        pg.quit()
        exit()
