from enum import Enum

# Enum classes for Game States
class GameStates(Enum):
    MAIN_MENU = 1
    GAME_SELECTION = 2
    GAME_PLAY = 3
    PLAYER_1 = 4
    PLAYER_2 = 5
    CPU_HID = 6
    END = 7