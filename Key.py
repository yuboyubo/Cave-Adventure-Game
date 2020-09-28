from Item import *

class Key(Item):
    """ Key class
    """
    def __init__(self):
        """ Constructor of the Key class.
        """
        self.id = "K"
        self.collidable = True

    def on_hit(self, game):
        """ When the player takes the Key the Key should be added to
            the Player’s inventory. The Key should then be removed from
            the dungeon once it’s in the Player’s inventory.

        Parameters:
            game (GameLogic): the game produced by GameLogic class.
        """
        game.get_player().add_item(self)
        del game._game_information[game.get_player().get_position()]
        
    def __str__(self):
        """ Returns the string representation of the Key.

        Returns:
            (str): Returns the string representation of the Key.
        """
        return "Key('"+ self.get_id() + "')"

    def __repr__(self):
        """ Returns the string representation of the Key.

        Returns:
            (str): Returns the string representation of the Key.
        """
        return "Key('"+ self.get_id() + "')"
