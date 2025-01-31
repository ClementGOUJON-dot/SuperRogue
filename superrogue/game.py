import pygame
from .walls import Walls
from .state import State
from .board import Board

class Game :

    def __init__(self, width:int, height:int, tile_size:int,fps: int, wall_color: pygame.color, door_color : pygame.color, heroe_color: pygame.color):
        self._width = width
        self._height = height
        self._tile_size = tile_size
        self._fps = fps
        self._wall_color= wall_color
        self._door_color= door_color
        self._heroe_color= heroe_color
        self._heroe= None

    def _Initialize(self) -> None:
        """Initialize the game."""

        # Create a display screen
        screen_size = (self._width * self._tile_size,
                       self._height * self._tile_size)
        
        self._screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN )
        pygame.display.flip()

        # Create the main board
        self._board = Board(screen=self._screen,
                            nb_rows=self._height,
                            nb_cols=self._width,
                            tile_size=self._tile_size)
        # Create the clock
        self._clock = pygame.time.Clock()

        # Create walls
        self._walls = Walls(nb_lines=self._height,
                                          nb_cols=self._width)
        
    def _process_events(self) -> None:
        """Process pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._state = State.QUIT  # Properly handle quit event
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Press 'Q' to quit
                    self._state = State.QUIT
        
    def start(self) -> None:

        """Start the game."""
        # Initialize pygame
        pygame.init()

        # Initialize game
        self._Initialize()

        # Start pygame loop
        self._state = State.PLAY
        while self._state != State.QUIT:

            # Wait 1/FPS second
            self._clock.tick(self._fps)

            # Listen for events
            self._process_events()

            # Clear the screen before drawing the next frame
            self._screen.fill(pygame.Color("black"))

            # Draw
            self._board.draw()

            match self._state:
                case State.GAMEOVER:
                    self._drawgameover()
            # Display
            pygame.display.update()

        # Terminate pygame
        pygame.quit()