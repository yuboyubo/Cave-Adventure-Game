from Entity import *

class Wall(Entity):
    """ Wall class
    """
    def __init__(self):
        """ Constructor of the Wall class.
        """
        self.id = "#"
        self.collidable = False

    def __str__(self):
        """ Returns the string representation of the Wall.

        Returns:
            (str): Returns the string representation of the Wall.
        """
        return "Wall('"+ self.get_id() + "')"

    def __repr__(self):
        """ Returns the string representation of the Wall.

        Returns:
            (str): Returns the string representation of the Wall.
        """
        return "Wall('"+ self.get_id() + "')"
