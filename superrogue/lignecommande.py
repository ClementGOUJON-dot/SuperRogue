import argparse

DEFAULT_WIDTH = 40
DEFAULT_HEIGHT = 30
DEFAULT_PIXEL = 10

def lignecommande():
    parser = argparse.ArgumentParser(description='Some description.')
    parser.add_argument('-W','--width', type = int, help="columns number",default=DEFAULT_WIDTH)
    parser.add_argument('-H','--height', type=int, help= "ligns number", default=DEFAULT_HEIGHT)
    parser.add_argument('--tile_size', type=int, help="size of a tile", default=DEFAULT_PIXEL)
    parser.add_argument('--fps', '--framepersecond', type=int, help= "number of frames per second", default=10)
    parser.add_argument('--wall_color', type=str, help="color of the walls", default = '#ffffff')
    parser.add_argument('--door_color', type=str, help="color of the doors", default = '#800080')
    parser.add_argument('--heroe_color',type=str, help="color of the heroe", default = '#ffff00')

    parser.add_argument("--gameover_on_exit", action = "store_true",
                        help="Exiting the board ends the game.")

    args=parser.parse_args()

    # Run parser on command line arguments
    return args


