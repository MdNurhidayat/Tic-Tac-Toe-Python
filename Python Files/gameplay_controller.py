from enum_files.game_states import GameStates
from enum_files.player_count import PlayerCount

class GameplayController:    
    # Gameplay Controller variables
    game_board = []
    game_state = 0
    game_players = 0

    # Class Methods
    def __init__(self):
        self.game_board = ["-", "-", "-",
                           "-", "-", "-",
                           "-", "-", "-"]
        self.game_state = GameStates.MAIN_MENU
        self.game_players = PlayerCount.UNINITALISED
        
    def update_gamestate():
        return
    
    def update_players_playing():
        return