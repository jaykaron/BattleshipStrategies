# Ship class

from random import randint
import BOARD


class Ship(object):
    """ The Ship object, stored in the shipsMap of the board"""

    def __init__(self, symbol, length):
        """ symbol - a single char. length - int """
        self.length = length    #The original length. Doesn't change
        self.remaining = length #Decreases when ship is hit
        self.symbol = symbol # the character representation the ship will take on the board

    def set_randomly(self, board):
        """ Randomly places the ship on a open part of the map
            Inputs: self and the board to place the ship on
            Outputs: None """
        # 1 represents Horozontal and 2 represents Vertical
        ship_ori = randint(1,2)

        if ship_ori == 1: # Horizontal
            while True:
                ship_row = randint(0, board.get_height() - 1)
                ship_col = randint(0, board.get_length() - self.length)
                # check if location is free
                for i in range(0, self.length):
                    if board.shipsMap[ship_row][ship_col + i] != None:
                        break   #something there, go through while-loop again
                else:
                    break   #once done for-loop exit while-loop

            # place the ship
            for i in range(0, self.length):
                board.shipsMap[ship_row][ship_col + i] = self

        elif ship_ori == 2: # Vertical
            while True:
                ship_row = randint(0, board.get_height() - self.length)
                ship_col = randint(0, board.get_length() - 1)
                # check if the location is free
                for i in range(0, self.length):
                    if board.shipsMap[ship_row + i][ship_col] != None:
                        break
                else:
                    break
                        # place the ship
            for i in range(0,self.length):
                board.shipsMap[ship_row + i][ship_col] = self

    def hit(self):
        """ Ship has been hit.
        Inputs: None
        Outputs: True if sunk otherwise False"""

        self.remaining -= 1
        if self.remaining == 0:
            return True
        return False

    def reset_remaining(self):
        """ Puts the ship back to full health
        Inputs: None. Outputs: None"""
        self.remaining = self.length
