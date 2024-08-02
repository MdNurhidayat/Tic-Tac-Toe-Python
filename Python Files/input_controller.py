from enum_files.game_states import GameStates
from enum_files.player_count import Player_Count

class InputController:

    def game_selection_validation():
        user_input = 0
        while user_input < 1 or user_input > 2:
            user_input = input("How many players are playing? 1 or 2? : ")
            if user_input < 1 or user_input > 2:
                print("Invalid Input, Try Again!")
        return int(user_input)
        
    
    def gameplay_validation():
        return

    def request_user_input(game_state, player_count):
        if game_state == GameStates.GAME_SELECTION:
            # Let player choose amount of players
            player_count = game_selection_validation()
            game_state = GameStates.GAME_PLAY

        elif game_state == GameStates.GAME_PLAY:
            # Gameplay inputs here

            if ()
            
