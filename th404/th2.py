import pygame

pygame.init()

#display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Grungich")

#Marisa
marisaImg = pygame.image.load("marisa.png")
marisaX = 300
marisaY = 400
change = 4
focus = 2
def marisa(x, y):
    screen.blit(marisaImg, (x, y))

#loop
running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #control marisa
    usInput = pygame.key.get_pressed()
    if usInput[pygame.K_LSHIFT]:
        if usInput[pygame.K_LEFT] and marisaX > -6:
            marisaX -= focus
        if usInput[pygame.K_RIGHT] and marisaX < 606:
            marisaX += focus
        if usInput[pygame.K_UP] and marisaY > 0:
            marisaY -= focus
        if usInput[pygame.K_DOWN] and marisaY < 436:
            marisaY += focus
    else:
        if usInput[pygame.K_LEFT] and marisaX > -6:
            marisaX -= change
        if usInput[pygame.K_RIGHT] and marisaX < 606:
            marisaX += change
        if usInput[pygame.K_UP] and marisaY > 0:
            marisaY -= change
        if usInput[pygame.K_DOWN] and marisaY < 436:
            marisaY += change



    pygame.time.delay(10)
    marisa(marisaX, marisaY)
    pygame.display.update()
