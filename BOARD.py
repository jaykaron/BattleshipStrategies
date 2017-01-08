# -*- coding: utf-8 -*-
import SHIP

class Board():
    """Class representing one game board, mostly 2 2D arrays.
    one of the ships one recording the fired locations"""

    def __init__(self, h, l, sizes):
        """ h - (int) height of the board. l - (int) length of board
        sizes - (int array) the lengths of the various ships"""

        self.height = h     # number of rows
        self.length = l     # number of columns
        self.sizes = sizes      # int array
        self.shipsLeft = len(sizes)     #Decreases over time, game ends when 0


        # 2D array to contain ship objects
        self.shipsMap = []
        for i in range(0,self.height):
            self.shipsMap.append([None]*self.length)

        self.shipsList = []     # single array of ship objects, needed for resetting
        charCode = 97
        for shipLength in sizes:
            newShip = SHIP.Ship(chr(charCode), shipLength)
            charCode += 1
            newShip.set_randomly(self)
            self.shipsList.append(newShip)

        # 2D char array, ~ - unfired, X - miss, # - hit
        self.firedMap = []
        for i in range(0,self.height):
            self.firedMap.append(['~']*self.length)
        self.unshotTiles = self.height*self.length

        # used when printing firedMap, to change the symbol of the most recent location
        self.last_location_shot = None

    def get_height(self):
        """Inputs: None. Outputs: height of the board"""
        return self.height
    def get_length(self):
        """Inputs: None. Outputs: length of the board"""
        return self.length

    def print_ships(self):
        """Prints the layout of the ships
        Inputs/Outputs: None"""
        for row in self.shipsMap:
            rowTxt = ""
            for tile in row:
                if tile != None:
                    rowTxt += tile.symbol+" "
                else:
                    rowTxt+= "~ "
            print (rowTxt)
        print("--"*self.length)

    def print_shots(self):
        """Prints which locations have been shot
        Inputs/Outputs: None"""

        for y in range(0, self.height):
            rowOutput = ""
            for x in range(0, self.length):
                #Changes the printed symbol of the most recent shot location
                if (y, x) == self.last_location_shot:
                    if self.firedMap[y][x] == "#":      #Hit
                        rowOutput+= "0 "
                    elif self.firedMap[y][x] == "X":    #Miss
                        rowOutput+= "O "
                else:
                    rowOutput+= self.firedMap[y][x] + " "
            print(rowOutput)
        print("--"*self.length)

    def shoot_spot(self, locationTuple):
        """Shoots a spot, returns an int.
        Inputs: (self), a tuple of y, x locations
        Outputs: 0 - Miss
                 1 - Hit
                 2 - Sink"""

        y, x = locationTuple
        if self.firedMap[y][x] == "~":
            self.unshotTiles -= 1
            self.last_location_shot = locationTuple

            if self.shipsMap[y][x] != None:     #Hit
                self.firedMap[y][x] = "#"

                hitShip = self.shipsMap[y][x]
                if hitShip.hit():   #Ship has sunk
                    self.shipsLeft -= 1
                    print("SUNK")
                    return 2    #Ship has sunk

                print("HIT")
                return 1 # Hit but not sunk
            else:
                self.firedMap[y][x] = "X"
                print ("Miss")
                return 0
        else:       #Shouldn't get to here
            print ("Location already shot")
            return False

    def reset(self):
        """Resets firedMap, unshotTiles, shipsLeft and the ships healths
        Inputs/Outputs: None"""
        self.firedMap = []
        for i in range(0,self.height):
            self.firedMap.append(['~']*self.length)
        self.unshotTiles = self.height*self.length
        self.shipsLeft = len(self.sizes)
        for ship in self.shipsList:
            ship.reset_remaining()

    def even_unshot_tiles(self):
        """Returns how many even checkered tiles have not been shot
        Inputs: None, Outputs: int - how many tiles"""
        unshot_even_tiles = 0
        for y in range(0, self.get_height()):
            for x in range(0, self.get_length()):
                if self.firedMap[y][x] == "~":
                    if (x+y)%2 == 0:
                        unshot_even_tiles +=1
        if unshot_even_tiles == 0:
            self.print_ships()
            self.print_shots()
        return unshot_even_tiles
