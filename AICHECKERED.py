import AIMASTER as M
import AICLASSIC as C

class AiCheckered(C.AiClassic, M.AiMaster):
    """ Pretty much the Classic but only shoots even tiles"""

    #unable to complete T shaped layouts
    #   ~ X a X ~ X
    #   X ~ # # # #
    #   ~ X a X ~ X

    #Solution? Keep track of sunken ship sizes and there extreme points see how they match up to actual sizes.
    # Any ships that don't match up. Add adjacents of the extreme points.

    def __init__(self):
        M.AiMaster.__init__(self)
        C.AiClassic.__init__(self)

        self.even_or_odd = 0


    #Override the pick random to only pick "even" tiles
    def pick_random(self, board):
        """Picks a random unshot tile that"""
        if self.even_unshot_tiles(board) <= 0:
            print("switch")
            self.even_or_odd = 1
        while True:
            randX = M.randint(0,board.get_length()-1)
            randY = M.randint(0,board.get_height()-1)
            if (randY+randX)%2 == self.even_or_odd and board.firedMap[randY][randX] == "~":
                break
        return (randY, randX)

    def even_unshot_tiles(self, board):
        """Returns how many even checkered tiles have not been shot
        Inputs: board, Outputs: int - how many tiles"""
        unshot_even_tiles = 0
        for y in range(0, board.get_height()):
            for x in range(0, board.get_length()):
                if board.firedMap[y][x] == "~":
                    if (x+y)%2 == self.even_or_odd:
                        unshot_even_tiles +=1
        #Temporary prints for testing
        #if unshot_even_tiles == 0:
        #    board.print_ships()
        #    board.print_shots()
        return unshot_even_tiles
