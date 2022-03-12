import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 200
y = 150

a = 250
b = 0

c = +1
v = +1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    x = x + c
    if x > 500:
        c = - 1
    if x < 0:
        c = +1

    b = b + v
    if b > 500:
        v = - 1
    if b < 0:
        v = +1

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))
    pygame.draw.circle(win,(0, 255, 255), (a, b), 50)
    pygame.display.update()

    pygame.time.delay(10)
