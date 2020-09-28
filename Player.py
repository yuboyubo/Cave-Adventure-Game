from Entity import *

class Player(Entity):
    """ Player class
    """
    def __init__(self, move_count):
        """ Constructor of the Player class.

        Parameters:
            move_count (int): how many moves a Player can have for the given dungeon they are in
        """
        self.id = "O"
        self.collidable = True
        self.position = None
        self.move_count = move_count
        self.inventory = []
        
    def set_position(self, position):
        """ Sets the position of the Player.

        Parameters:
            position (tuple<int, int>): the position of the Player
        """
        self.position = position

    def get_position(self):
        """ Returns a tuple of ints representing the position of the Player.

        Returns:
            (tuple<int, int>): Returns a tuple of ints representing the position of the Player.
        """
        return self.position

    def change_move_count(self, number):
        """ Number to be added to the Player’s move count.

        Parameters:
            number (int): Number to be added to the Player’s move count.
        """
        self.move_count += number

    def moves_remaining(self):
        """ Returns an int representing how many moves the Player has left before they reach the maximum move count.

        Returns:
            (int): Returns an int representing how many moves the Player has left before they reach the maximum move count.
        """
        return self.move_count

    def add_item(self, item):
        """ Adds the item to the Player’s Inventory.

        Parameters:
            item (Entity): the item to add into the Player's Inventory
        """
        self.inventory.append(item)

    def get_inventory(self):
        """ Returns the string representation of the Player.

        Returns:
            (str:): Returns the string representation of the Player.
        """
        return self.inventory
        
    def __str__(self):
        """ Returns the string representation of the Player.

        Returns:
            (str): Returns the string representation of the Player.
        """
        return "Player('"+ self.get_id() + "')"

    def __repr__(self):
        """ Returns the string representation of the Player.

        Returns:
            (str): Returns the string representation of the Player.
        """
        return "Player('"+ self.get_id() + "')"
