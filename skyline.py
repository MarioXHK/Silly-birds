import pygame
import random
pygame.init()
pygame.display.set_caption("flowers!")
screen = pygame.display.set_mode((800, 800))
screen.fill((255,255,255))

def floor(floorx,floory,floryin,flooryan):
        pygame.draw.rect(screen, (random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256)), (floorx, floory, flooryan*floryin, flooryan))
        windowcol = (random.randrange(0, 256),random.randrange(0, 256),random.randrange(0, 256))
        for w in range(floryin):
            pygame.draw.rect(screen, (windowcol), ((floorx+(flooryan/4)+(flooryan*w)), floory+(flooryan/4), flooryan/2, flooryan/2))
def building(xxx,size):
    floormod = random.randrange(1, 9)
    floorsize = size/floormod
    floors = floormod
    for i in range(floors):
        floor(xxx,((-i*floorsize)+800),floormod,floorsize)
    pygame.draw.polygon(screen, (0, 200, 200), ((200, 400), (500, 400), (360, 200)))
    
building(0,400)
pygame.display.flip()