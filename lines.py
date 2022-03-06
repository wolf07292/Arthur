import pygame
pygame.init()
a=int(input())
b=int(input())
win = pygame.display.set_mode((a,b))
color = (0, 0, 0)
win.fill(color)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #pygame.draw.rect(win, (255, 255, 0), (150, 200, 100, 70))
    #pygame.draw.circle(win, (0, 255, 255), (100, 200), 40)
    #pygame.draw.polygon(win, (0, 0, 0),[(0, 100), (100, 50), (100, 150)], False)
    pygame.draw.line(win, (255, 255, 255), (0, 0), (a, b), 5)
    pygame.draw.line(win, (255, 255, 255), (a, 0), (0, b), 5)
    pygame.display.update()
