from Item import *

class MoveIncrease(Item):
    """ MoveIncrease class
    """
    def __init__(self, moves=5):
        """ Constructor of the MoveIncrease class.

        Parameters:
            moves (int): moves describe how many extra moves the Player will be
                         granted when they collect this Item
        """
        self.id = "M"
        self.collidable = True
        self.moves = moves
  
    def on_hit(self, game):
        """ When the player hits the MoveIncrease(M) item the number of moves
            for the player increases and the M item is removed from the game.
            These actions are implemented via the on_hit method. Specifically,
            extra moves should be granted to the Player and the M item should be
            removed from the game

        Parameters:
            game (GameLogic): the game produced by GameLogic class.
        """
        game.get_player().change_move_count(self.moves)
        del game._game_information[game.get_player().get_position()]
        
    def __str__(self):
        """ Returns the string representation of the MoveIncrease.

        Returns:
            (str): Returns the string representation of the MoveIncrease.
        """
        return "MoveIncrease('"+ self.get_id() + "')"

    def __repr__(self):
        """ Returns the string representation of the MoveIncrease.

        Returns:
            (str): Returns the string representation of the MoveIncrease.
        """
        return "MoveIncrease('"+ self.get_id() + "')"
