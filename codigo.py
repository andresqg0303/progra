import pygame
import random
import time

pygame.init()
fps= pygame.time.Clock()
Width= 800
Height= 500

root= pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pong")


Black= (0, 0, 0)
White= (255, 255, 255)
Grey= (130, 130, 130)
LightGrey= (200,200,200)
Blue= (29, 49, 86)
LightBlue=  (49, 69, 106)
Orange= (255, 139, 54)
Red= (174, 24, 24)
Green= (2, 184, 5)
Yellow= (250, 195, 15)

Menu= pygame.image.load("Menu.jpg")

def ObjetosTexto(text, font):
    SuperficieTexto = font.render(text, True, Black)
    return SuperficieTexto, SuperficieTexto.get_rect()

def Boton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(root, ac,(x,y,w,h))
    else:
        pygame.draw.rect(root, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = ObjetosTexto(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    root.blit(textSurf, textRect)


def mainMenu():
    Inicio= True
    while Inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu, (0, 0))
        #Boton(msg,x,y,w,h,ic,ac)
        Boton1 = Boton("PVP",355,240,100,50,LightGrey, Grey)
        Boton2= Boton("PVC", 355, 320, 100, 50, LightGrey, Grey)
        pygame.display.update()
        fps.tick()

def mainloop():
    Winner = False
    while not Winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.fill(Blue)
        pygame.display.update()
        fps.tick(60)
mainMenu()
mainloop()

