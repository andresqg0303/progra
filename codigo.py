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


def mainloop():
    Winner = False
    while not Winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Winner = True
        root.fill(Blue)
        pygame.display.update()
        fps.tick(60)


mainloop()
pygame.quit()
quit()
