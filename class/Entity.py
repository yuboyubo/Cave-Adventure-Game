class Entity:
    """ Entity class
    """
    def __init__(self):
        """ Constructor of the Entity class.
        """
        self.id = "Entity"
        self.collidable = True

    def get_id(self):
        """ Returns a string that represents the Entity’s ID.

        Returns:
            (str): Returns a string that represents the Entity’s ID.
        """
        return self.id

    def set_collide(self, collidable):
        """ Set the collision state for the Entity

        Parameters:
            collidable (bool): the collision state of an entity.
        """
        self.collidable = collidable

    def can_collide(self):
        """ Returns True if the Entity can be collided with (another
            Entity can share the position that this one is in) and False otherwise.

        Returns:
            (bool): Returns the collision state for the Entity
        """
        return self.collidable

    def __str__(self):
        """ Returns the string representation of the Entity.

        Returns:
            (str): Returns the string representation of the Entity.
        """
        return "Entity('"+ self.get_id() + "')"

    def __repr__(self):
        """ Returns the string representation of the Entity.

        Returns:
            (str): Returns the string representation of the Entity.
        """
        return "Entity('"+ self.get_id() + "')"