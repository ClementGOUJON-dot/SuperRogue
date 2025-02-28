from superrogue.lignecommande import lignecommande
from superrogue.game import Game 

def main() -> None :
                
        args = lignecommande()

        game = Game(width = args.width, 
             height = args.height, 
             tile_size = args.tile_size, 
             fps = args.fps, 
             wall_color = args.wall_color, 
             door_color = args.door_color, 
             heroe_color = args.heroe_color)
        # Start the game
        game.start()
        
main()
