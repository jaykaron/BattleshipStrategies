from random import randint, shuffle

class AiMaster ():

    def __init__ (self):
        self.places_to_shoot = []
        self.log = []           #logs the location of the shot and the report int. Newest last.

    def make_decision(self, board):
        """This should not be called, every AI sublclass should override this method with it's own.
            Simply shoots a random spot if places_to_shoot is empty"""
        print("MASTER")
        if self.places_to_shoot == []:
            shot_destination = self.add_to_places_to_shoot(self.pick_random(board), board)
        shot_destination = self.places_to_shoot.pop()

        shot_report = board.shoot_spot(shot_destination)
        self.log.append([shot_destination, shot_report])

    def pick_random(self, board):
        """Picks a random unshot tile
        Input: board. Output: a location tuple"""
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
        """Add a location tuple to the end of places_to_shoot, checks to see if the spot has been shot already
        Inputs: a location tuple. Outputs: None"""
        y,x = locationTuple
        if y >= 0 and y < board.get_height() and x >= 0 and x < board.get_length():
            if board.firedMap[y][x] == "~":
                self.places_to_shoot.append((y,x))
