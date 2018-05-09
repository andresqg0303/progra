import pygame
import random
import time


pygame.init()
fps= pygame.time.Clock()
Width= 800
Height= 500

root= pygame.display.set_mode((Width,Height))

Black= (0, 0, 0)
White= (255, 255, 255)
Blue= (29, 49, 86)
Orange= (255, 139, 54)
Red= (174, 24, 24)
Green= (2, 184, 5)
Yellow= (250, 195, 15)

Menu= pygame.image.load("Menu.jpg")

def mainMenu():
    Inicio= True
    while Inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        root.blit(Menu,(0,0))
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
pygame.quit()
quit()
