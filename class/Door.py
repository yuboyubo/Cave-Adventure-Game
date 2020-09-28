from Entity import *

class Door(Entity):
    """ Door class
    """
    def __init__(self):
        """ Constructor of the Door class.
        """
        self.id = "D"
        self.collidable = True

    def on_hit(self, game):
        """ If the Player’s inventory contains a Key
            Entity then this method should set the ‘game over’ state to be True.

        Parameters:
            game (GameLogic): the game produced by GameLogic class.
        """
        if len(game.get_player().get_inventory()) > 0:
            game.set_win(True)
        else:
            print("You don't have the key!")
                
    def __str__(self):
        """ Returns the string representation of the Door.

        Returns:
            (str): Returns the string representation of the Door.
        """
        return "Door('"+ self.get_id() + "')"

    def __repr__(self):
        """ Returns the string representation of the Door.

        Returns:
            (str): Returns the string representation of the Door.
        """
        return "Door('"+ self.get_id() + "')"
