from support import *
from Player import *
from Entity import *
from Item import *
from Key import *
from Wall import *
from Door import *
from MoveIncrease import *

class GameLogic:
    """ GameLogic class
    """
    def __init__(self, dungeon_name="game1.txt"):
        """Constructor of the GameLogic class.

        Parameters:
            dungeon_name (str): The name of the level.
        """
        self._dungeon = load_game(dungeon_name)
        self._dungeon_size = len(self._dungeon)

        self._player = Player(GAME_LEVELS[dungeon_name])

        self._game_information = self.init_game_information()

        self._win = False

    def get_positions(self, entity):
        """ Returns a list of tuples containing all positions of a given Entity
             type.

        Parameters:
            entity (str): the id of an entity.

        Returns:
            (list<tuple<int, int>>): Returns a list of tuples representing the 
            positions of a given entity id.
        """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row,col))

        return positions

    def get_dungeon_size(self):
        """ Returns the width of the dungeon as an integer.

        Returns:
            (int): Returns the width of the dungeon as an integer.
        """
        return self._dungeon_size;

    def init_game_information(self):
        """ This method should return a dictionary containing the
            position and the corresponding Entity as the keys and values
            respectively. This method also sets the Player’s position.

        Returns:
            (dict<tuple<int, int>: Entity>): Return game information
        """
        dict = {}
        for row in range(self._dungeon_size):
            for col in range(self._dungeon_size):
                if self._dungeon[row][col] == 'K':
                    dict[(row,col)] = Key()
                elif self._dungeon[row][col] == 'D':
                    dict[(row,col)] = Door()
                elif self._dungeon[row][col] == '#':
                    dict[(row,col)] = Wall()
                elif self._dungeon[row][col] == 'M':
                    dict[(row,col)] = MoveIncrease()
                elif self._dungeon[row][col] == 'O':
                    self._player.set_position((row,col))
        return dict
        
    def get_game_information(self):
        """ Returns a dictionary containing the position and the
            corresponding Entity, as the keys and values, for the
            current dungeon.

        Returns:
            (dict<tuple<int, int>: Entity>): Return game information.
        """
        return self._game_information

    def get_player(self):
        """ This method returns the Player object within the game.

        Returns:
            (Player): Return Player object within the game.
        """
        return self._player
    
    def get_entity(self, position):
        """ Returns an Entity at a given position in the dungeon.

        Parameters:
            position (tuple<int, int>): the position to search
            
        Returns:
            (Entity): Returns an Entity at a given position in the dungeon.
        """
        return self._game_information.get(position)

    def get_entity_in_direction(self, direction):
        """ Returns an Entity in the given direction of the Player’s position.

        Parameters:
            direction (str): the direction to move
            
        Returns:
            (Entity): Returns an Entity in the given direction of the Player’s position.
        """
        return self._game_information.get(self.new_position(direction))
       
    def collision_check(self, direction):
        """ Returns False if a player can travel in the given direction, they won’t collide.
            True, they will collide, otherwise

        Parameters:
            direction (str): the direction to move
            
        Returns:
            (bool): Returns False if a player can travel in the given direction, they won’t collide.
                    True, they will collide, otherwise
        """
        entity = self.get_entity_in_direction(direction)
        if entity == None:
            return False
        elif entity.can_collide() == False:
            return True
        return False
    
    def new_position(self, direction):
        """ Returns a tuple of integers that represents the new position given the direction.

        Parameters:
            direction (str): the direction to move
            
        Returns:
            (tuple<int,int>): Returns a tuple of integers that represents the new position given the direction.
        """    
        pos = self._player.get_position()
        if direction == "W":
            return (pos[0]-1, pos[1])
        elif direction == "D":
            return (pos[0], pos[1]+1)
        elif direction == "S":
            return (pos[0]+1, pos[1])
        elif direction == "A":
            return (pos[0], pos[1]-1)
    
    def move_player(self, direction):
        """ Update the Player’s position to place them one position in the given direction.

        Parameters:
            direction (str): the direction to move
        """
        self._player.set_position(self.new_position(direction))
    
    def check_game_over(self):
        """ Return True if the game has been lost and False otherwise.

        Returns:
            (bool): Return whether game is over or not
        """
        if self._player.moves_remaining() <= 0:
            return True
        return False
    
    def set_win(self, win):
        """ Set the game’s win state to be True or False.

        Parameters:
            win (bool): Set the game’s win state to be True or False.
        """
        self._win = win
        
    def won(self):
        """ Return game’s win state.

        Returns:
            (bool): Return game’s win state.
        """
        return self._win
