# Ship class

from random import randint
import Board


class Ship(object):
    
    remaining = 3  # the total ships in the game  
    
    game_over = False
    
    def __init__(self, name, length):
        self.length = length
        self.remaining = length
        self.name = name # the caracture representation the ship will take on the board
        self.placed = False
        self.sunk = False
        
    # places ships randomly and makes shure they do not overlap
    def place(ship):
        # 1 represents Horozontal and 2 represents Vertical
        ship_ori = randint(1,2)

        if ship_ori == 1: # Horizontal
            while ship.placed == False:
                ship_row = randint(0, len(Board.hidden) - 1)
                ship_col = randint(0, len(Board.hidden) - ship.length) 
                # check if location is free
                for i in range(0, ship.length):
                    if Board.hidden[ship_row][ship_col + i] != '~':
                        break
                else:
                    ship.placed = True
        
            # place the ship
            for i in range(0,ship.length):
                Board.hidden[ship_row][ship_col + i] = ship.name
    
        elif ship_ori == 2: # Vertical
            while ship.placed == False:
                ship_row = randint(0, len(Board.hidden) - ship.length)
                ship_col = randint(0, len(Board.hidden) - 1)
                # check if the location is free
                for i in range(0, ship.length):
                    if Board.hidden[ship_row + i][ship_col] != '~':
                        break
                else:
                    ship.placed = True
                        # place the ship        
            for i in range(0,ship.length):
                Board.hidden[ship_row + i][ship_col] = ship.name
                
    
    
    # this fucnction is called when a ship is hit, it diecrenents the lives of the ship and the number of ships remaining, and wins the game
    def hit(self):
        self.remaining -= 1
        if self.remaining == 0:
            #print('You sank my ship')
            self.sunk = True
            Ship.remaining -= 1
        if Ship.remaining == 0:
            Ship.game_over = True