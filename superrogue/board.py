import pygame
import random as rd

from .gold import Gold
from .subject import Subject
from .observer import Observer
from .gameobject import GameObject

class Board (Subject, Observer) : # subject car le Board reçoit aussi des infos des objets. 
    def __init__(self, screen, tile_size, nb_rows, nb_cols) -> None:
        super().__init__()
        self._screen= screen
        self._tile_size= tile_size
        self._objects=[]
        self._nb_rows= nb_rows
        self._nb_cols= nb_cols
        self._grid = self.generate_grid()  # Grille pour gérer les murs, chemins, etc.

    def generate_grid(self):
        return [[None for _ in range(self._nb_cols)] for _ in range(self._nb_rows)]

    def draw(self) -> None:
        self._screen.fill(pygame.Color('black'))
        for obj in self._objects:
            for tile in obj.tiles:
                tile.draw(self._screen, self._tile_size )

    def add_object(self,gameobject: GameObject):
        if gameobject not in self._objects:
            self._objects.append(gameobject)
            gameobject.attach_obs(self) #permet au board de devenir l'observeur des objects ajoutés.

    def remove_object(self, gameobject: GameObject):
        if gameobject in self._objects:
            gameobject.detach_obs(self) # le board n'est plus l'observateur de l'object.
            self._object.remove(gameobject)

    def detect_collision(self, obj: "GameObject"):
        for o in self._objects:
            if o != obj and not o.background and o in obj : #opérateur in définit par contains dans GameObject
                return o
        return None
    
    def create_gold(self) -> "Gold":
        gold = None
        while gold is None or not self.detect_collision(gold):
            gold = Gold(color=pygame.Color("yellow"), col = rd.randint(0, self._nb_cols - 1), row = rd.randint(0,self._nb_rows - 1))
        self.add_object(gold)   

    def notify_object_moved(self, obj: GameObject) -> None:
        collision = self.detect_collision(obj)
        if collision:
            obj.notify_collision(collision)

    def notify_object_eaten(self, obj: GameObject) -> None:
        self.remove_object(obj)
        self.create_gold()
    
