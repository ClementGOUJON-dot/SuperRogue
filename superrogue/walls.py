import pygame
import typing
from .tile import Tile
from .lignecommande import lignecommande

 

class Walls :

    def __init__(self, nb_lines: int, nb_cols: int) -> None:
        """Object initialization."""
        super().__init__()
        self._nb_lines = nb_lines
        self._nb_cols = nb_cols

    @property
    def tiles(self) -> typing.Iterator[Tile]:
        """Tiles generator."""
        args = lignecommande()
        for i in range (30,10):
            for j in range (30,10):
                yield Tile(i+100, j+100, args.wall_color)


