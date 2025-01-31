from .lignecommande import lignecommande
from .game import Game 

def main() -> None :
                
        args = lignecommande()

        Game(width = args.width, 
             height = args.height, 
             tile_size = args.tile_size, 
             fps = args.fps, 
             wall_color = args.wall_color, 
             door_color = args.door_color, 
             heroe_color = args.heroe_color)
        
        

