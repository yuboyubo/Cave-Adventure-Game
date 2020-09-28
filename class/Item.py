from Entity import *

class Item(Entity):
    """ Item class
    """
    def __init__(self):
        """ Constructor of the Item class.
        """
        self.id = "Entity"
        self.collidable = True

    def on_hit(self, game):
        """ This function should raise the NotImplementedError.

        Parameters:
            game (GameLogic): the game produced by GameLogic class.
        """
        raise NotImplementedError

    def __str__(self):
        """ Returns the string representation of the Item.

        Returns:
            (str): Returns the string representation of the Item.
        """
        return "Item('"+ self.get_id() + "')"

    def __repr__(self):
        """ Returns the string representation of the Item.

        Returns:
            (str): Returns the string representation of the Item.
        """
        return "Item('"+ self.get_id() + "')"
