import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((500, 500))
position = np.array([3,3]) # à modifier
WALL = [[2,4],[3,4],[4,4]]

def next_position(position:np.ndarray,move:np.ndarray, WALL, DOOR):
     #ajouter murs, portes, donjons, chemins, etc à stocker dans un dico
    next = position + move
    if next not in WALL :
        position = next
    else :
        print('ERROR : YOU CANNOT WALK THROUGHT A WALL')
    return None

Flag=True
while Flag :
    tour = True
    while tour :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == 1073741906: #UP
                    next_position(position,np.array([0,1]))
                    print(position)
                    tour = False
                if event.key == 1073741905: #DOWN
                    next_position(position,np.array([0,-1]))
                    print(position)
                    tour = False
                if event.key == 1073741903: #RIGHT
                    next_position(position,np.array([1,0]))
                    print(position)
                    tour = False
                if event.key == 1073741904: #LEFT
                    next_position(position,np.array([-1,0]))
                    print(position)
                    tour = False
            if event.type == pygame.QUIT:
                    Flag,tour = False,False
pygame.quit()


