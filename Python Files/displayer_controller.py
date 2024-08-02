# This python file handles all kind of display to be shown on the game
class DisplayController:
    def display_start():
        print("Welcome to Tic Tac Toe by Hidayat!\n")
        print("How many players are playing? (Type 1 or 2 then press ENTER)")

    def display_battle_with_CPU():
        print("You chose to play with... CPU Hid!\n")

    def display_battle_with_player():
        print("You chose to play with a friend! How nice :)\n")

    def update_display():
        return