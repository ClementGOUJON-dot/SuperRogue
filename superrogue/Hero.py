import pygame
import numpy as np



class Hero:
   """ Class to define a monster"""
    def __init__(self, position, degats, vies) -> None:
            """Object initialization."""
            # Vérification que 'position' est un tableau numpy avec 2 dimensions
            if not isinstance(position, np.ndarray):
                raise TypeError("Position du monstre doit être un tableau NumPy.")
            if position.shape != (2,):
                raise ValueError("Position du monstre doit être un vecteur à 2 dimensions.")
            self._position = position
            self._degats = degats
            self._vies = vies
            self._or = int(0)

    def move(self._position,hero,mur):

        if norme(self._position,hero._position) <= 1:
        #battle
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
    
