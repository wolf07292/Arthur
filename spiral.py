import pygame as pg
class Circle:
    def __init__(self,x,y,rad,col):
        self.x = self
        self.y = self
        self.rad = self
        self.col = self
        self.dir = 'right'

    def horizontal_movement(self):
        if self.dir == 'right':
            self.x += 1
            if self.x > W:
                self.dir = 'left'
        else:
            self.x -= 1
            if self.x < 0:
                self.dir = 'right'

    def draw(self, win):
        pg.draw.circle(win, self.col, (self.x, self.y, ), self.rad)
