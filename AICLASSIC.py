import AIMASTER as M

class AiClassic(M.AiMaster):
    """Shoots randomly until a hit. Then shoots adjaccents until a hit. Then finds the line and shoots up and down until sink or misss"""

    #When sinking the dingy, it hasn't switched to checking line mode. so it continues to shoot all adjacents
    # Possibly can skip step 2 and go to 3

    def __init__(self):
        M.AiMaster.__init__(self)

        self.mode = "random_search"
        self.search_start = (None, None)    # The origin of the checking_adj

    def make_decision(self, board):
        if self.places_to_shoot == []:
            self.mode = "random_search"
            self.add_to_places_to_shoot(self.pick_random(board), board)

        shot_destination = self.places_to_shoot.pop()
        shot_report = board.shoot_spot(shot_destination)
        self.log.append([shot_destination, shot_report])
        if shot_report == 1:    # hit
            oldY, oldX = shot_destination
            if self.mode == "random_search":
                self.mode = "checking_adj"
                self.search_start = shot_destination
                self.add_adjacents_to_shoot(shot_destination, board)
            elif self.mode == "checking_adj":
                self.mode = "checking_line"
                line_orient =  self.line_orientation(self.search_start, shot_destination)
                self.places_to_shoot = []

                hit_miss_high, hit_miss_low = False, False
                mod = 1
                while not hit_miss_low or not hit_miss_high:
                    if line_orient == "Horizontal":
                        xMod = mod
                        yMod = 0
                    elif line_orient == "Vertical":
                        yMod = mod
                        xMod = 0
                    if oldX+xMod >= board.get_length() or oldY+yMod >= board.get_height() or board.firedMap[oldY+yMod][oldX+xMod] == "X":
                        hit_miss_high = True
                    elif not hit_miss_high:
                        self.add_to_places_to_shoot((oldY+yMod, oldX+xMod), board)
                    if oldX-xMod < 0 or oldY-yMod < 0 or board.firedMap[oldY-yMod][oldX-xMod] == "X":
                        hit_miss_low = True
                    elif not hit_miss_low:
                        self.add_to_places_to_shoot((oldY-yMod, oldX-xMod), board)
                    mod += 1
                self.places_to_shoot.reverse()

        elif shot_report == 0 and self.mode == "checking_line":
            line_direct = self.line_direction(self.search_start, shot_destination)
            targets_to_remove = []
            for target in self.places_to_shoot:
                if self.line_direction(self.search_start, target) == line_direct:
                    targets_to_remove.append(target)
            for target in targets_to_remove:
                self.places_to_shoot.remove(target)
        elif shot_report == 2 and self.mode == "checking_line":
            self.places_to_shoot = []

    def line_orientation(self, point1, point2):
        y1, x1 = point1
        y2, x2 = point2
        if y1 == y2:
            return "Horizontal"
        elif x1 == x2:
            return "Vertical"
        else:
            return "No Line"

    def line_direction(self, point1, point2):
        """Line points from point1 to point2"""
        orient = self.line_orientation(point1, point2)
        y1, x1 = point1
        y2, x2 = point2
        if orient == "Vertical":
            if y2 < y1:
                return "Up"
            elif y2 > y1:
                return "Down"
        elif orient == "Horizontal":
            if x2 < x1:
                return "Left"
            elif x2 > x1:
                return "Right"
        return "Error"

    def add_adjacents_to_shoot(self, locationTuple, board):
        # doesn't choose the order quite randomly
        originY, originX = locationTuple
        rangeY  = range(-1,2)
        M.shuffle(rangeY)
        for dy in rangeY:
            rangeX = range(-1,2)
            M.shuffle(rangeX)
            for dx in rangeX:
                if dy != dx and dx*dy == 0:
                    self.add_to_places_to_shoot((originY+dy, originX+dx), board)
