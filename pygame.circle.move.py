import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 200
y = 150




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    if x > 500:
        x = -100
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -=3
    if keys[pygame.K_RIGHT]:
        x += 3
    if keys[pygame.K_UP]:
        y -= 3
    if keys[pygame.K_DOWN]:
        y += 3
    if keys[pygame.K_SPACE]:
        if x < 200:
            x+=1
        if y < 150:
            y+=1
        if x > 200:
            x-=1
        if y > 150:
            y-=1





    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))
    pygame.display.update()

    pygame.time.delay(10)
