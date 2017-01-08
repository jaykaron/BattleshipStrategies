from random import randint, shuffle

class AiMaster ():

    def __init__ (self):
        self.places_to_shoot = []
        self.log = []           #logs the location of the shot and the report int. Newest last.

    def make_decision(self, board):
        print("MASTER")
        if self.places_to_shoot != []:
            shot_destination = self.places_to_shoot.pop()
        else:
            shot_destination = self.add_to_places_to_shoot(self.pick_random(board), board)

        shot_report = board.shoot_spot(shot_destination)
        self.log.append([shot_destination, shot_report])

    def pick_random(self, board):
        if board.unshotTiles <= 0:
            print("No More Tiles")
            return
        while True:
            randX = randint(0,board.get_length()-1)
            randY = randint(0,board.get_height()-1)
            if board.firedMap[randY][randX] == "~":
                break
        return (randY, randX)

    def add_to_places_to_shoot(self, locationTuple, board):
        y,x = locationTuple
        if y >= 0 and y < board.get_height() and x >= 0 and x < board.get_length():
            if board.firedMap[y][x] == "~":
                self.places_to_shoot.append((y,x))
