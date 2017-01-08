import AIMASTER as M
import AICLASSIC as C

class AiCheckered(C.AiClassic, M.AiMaster):

    def __init__(self):
        M.AiMaster.__init__(self)
        C.AiClassic.__init__(self)


    #Override the pick random to only pick "even" tiles
    def pick_random(self, board):
        if board.even_unshot_tiles() <= 0:
            print("No More Even Tiles")
            return
        while True:
            randX = M.randint(0,board.get_length()-1)
            randY = M.randint(0,board.get_height()-1)
            if (randY+randX)%2 == 0 and board.firedMap[randY][randX] == "~":
                break
        return (randY, randX)
