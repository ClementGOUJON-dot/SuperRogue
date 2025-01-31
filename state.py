from enum import Enum


class State(Enum) :
    """Define the states of the game."""

    QUIT=0
    PLAY=1
    GAMEOVER=-1
    