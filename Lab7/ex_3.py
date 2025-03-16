import pygame
pygame.init()

# Экран
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Ball")
screen.fill((255, 255, 255))

#Доптың бастапқы координатасы
x, y = 400, 300
radius = 25
speed = 20


running = True


while running:
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #Допты жылжыту
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and y-radius>=0:
                y-=speed
            if event.key==pygame.K_DOWN and y+radius<=600:
                y+=speed
            if event.key==pygame.K_LEFT and x-radius>=0:
                x-=speed
            if event.key==pygame.K_RIGHT and x+radius<=800:
                x+=speed