from support import *
from Player import *
from Entity import *
from Item import *
from Key import *
from Wall import *
from Door import *
from MoveIncrease import *
from GameLogic import *
    
class GameApp:
    """ GameApp class
    """
    def __init__(self):
        """ Constructor of the GameApp class.

        """
        self.game = GameLogic()
        self.game_information = self.game.get_game_information()
        self.dungeon_size = self.game.get_dungeon_size()
        self.display = Display(self.game_information, self.dungeon_size)
        self.player = self.game.get_player()
        
    def play(self):
        """ Handles the player interaction.

        """
        while self.game.check_game_over() == False and self.game.won() == False:
            self.draw()
            action = input("Please input an action: ")
            if action == "H":
                print("Here is a list of valid actions: ['I', 'Q', 'H', 'W', 'S', 'D', 'A']")
            elif action == "Q":
                check = input("Are you sure you want to quit? (y/n): ")
                if check == "y":
                    return
            elif action == "I W":
                print(str(self.game.get_entity_in_direction("W")) + " is on the W side.")
                self.player.change_move_count(-1)
            elif action == "I S":
                print(str(self.game.get_entity_in_direction("S")) + " is on the S side.")
                self.player.change_move_count(-1)
            elif action == "I A":
                print(str(self.game.get_entity_in_direction("A")) + " is on the A side.")
                self.player.change_move_count(-1)
            elif action == "I D":
                print(str(self.game.get_entity_in_direction("D")) + " is on the D side.")
                self.player.change_move_count(-1)
            elif action == "W":
                if self.game.collision_check("W") == True:
                    print("That's invalid.")
                else:
                    if self.game.get_entity_in_direction("W") != None:
                        entity = self.game.get_entity_in_direction("W")
                        self.game.move_player("W")
                        entity.on_hit(self.game)
                    else:
                        self.game.move_player("W")
                self.player.change_move_count(-1)
            elif action == "S":
                if self.game.collision_check("S") == True:
                    print("That's invalid.")
                else:
                    if self.game.get_entity_in_direction("S") != None:
                        entity = self.game.get_entity_in_direction("S")
                        self.game.move_player("S")
                        entity.on_hit(self.game)
                    else:
                        self.game.move_player("S")
                self.player.change_move_count(-1)
            elif action == "A":
                if self.game.collision_check("A") == True:
                    print("That's invalid.")
                else:
                    if self.game.get_entity_in_direction("A") != None:
                        entity = self.game.get_entity_in_direction("A")
                        self.game.move_player("A")
                        entity.on_hit(self.game)
                    else:
                        self.game.move_player("A")
                self.player.change_move_count(-1)
            elif action == "D":
                if self.game.collision_check("D") == True:
                    print("That's invalid.")
                else:
                    if self.game.get_entity_in_direction("D") != None:
                        entity = self.game.get_entity_in_direction("D")
                        self.game.move_player("D")
                        entity.on_hit(self.game)
                    else:
                        self.game.move_player("D")
                self.player.change_move_count(-1)
            else:
                print("That's invalid.")
            
        if self.game.check_game_over():
            print("You have lost all your strength and honour.")
        else:
            print("You have won the game with your strength and honour!")
        
    def draw(self):
        """ Displays the dungeon with all Entities in their positions

        """
        self.display.display_game(self.player.get_position())
        self.display.display_moves(self.player.moves_remaining())
