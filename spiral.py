import pygame as pg
import random
FPS = 
clock = pg.time.Clock()
win = pg.display.set_mode((500, 500))
class Circle:
    def __init__(self,x,y,rad,col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.dir = 'right'

    def horizontal_movement(self):
        if self.dir == 'right':
            self.x += 1
            if self.x > 500:
                self.dir = 'left'
        else:
            self.x -= 1
            if self.x < 0:
                self.dir = 'right'

    def draw(self, win):
        pg.draw.circle(win, (self.col), (self.x, self.y), self.rad)


list_circles = []
for i in range(100):
    list_circles.append(Circle(i * 10, i * 5, 30, random.choices(range(256), k=3)))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    win.fill((255, 255, 255))
    for i in range(100):
        list_circles[i].horizontal_movement()
        list_circles[i].draw(win)



    pg.display.update()
    clock.tick(FPS)
