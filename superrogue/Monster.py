import pygame
import numpy as np
import

def norme(positon1,position2):
    return (positon1[0]-position2[0])**2 + (positon1[1]-position2[1])**2

   """ Class to define a monster"""
    def __init__(self, position, damages, lives,name) -> None:
            """Object initialization."""
            # Vérification que 'position' est un tableau numpy avec 2 dimensions
            if not isinstance(position, np.ndarray):
                raise TypeError("Position du monstre doit être un tableau NumPy.")
            if position.shape != (2,):
                raise ValueError("Position du monstre doit être un vecteur à 2 dimensions.")
            self._position = position
            self._damages = damages
            self._lives = lives
            self._name = name

    def monster_move(self._position,hero,mur):

        if norme(self._position,hero._position) <= 1:
            hero.lives += -self._damages
            if hero._lives > 0 :
                print(self._name, " hurt you... :( ")
                print("You lost ",self._degats, " lives")

        else :
            move = np.array([0,1],[0,-1],[1,0],[-1,0])
            distance =[]
            for m in move:
                next_monster_position = self._position + move
                if next_monster_position in mur:
                    distance.append(float('inf')
                else : 
                    distance.append(norme(next_monstre_position,hero._position))
                
            self._position += move[liste.index(min(distance))]
        return
    
    

    
