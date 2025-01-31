
import typing
from superrogue.tile import Tile
from superrogue.lignecommande import lignecommande
from superrogue.gameobject import GameObject
 

class Walls(GameObject) :

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
                print(f"walls = {i=}{j=}")
                yield Tile(i+100, j+100, args.wall_color)


