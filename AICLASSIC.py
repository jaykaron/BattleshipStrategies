import AIMASTER as M

class AiClassic(M.AiMaster):
    """Shoots randomly until a hit. Then shoots adjaccents until a hit. Then finds the line and shoots up and down until sink or misss"""

    def __init__(self):
        M.AiMaster.__init__(self)

        self.mode = "random_search"
        self.search_start = (None, None)    # The origin of the checking_adj

        self.saved_lines = []
        self.current_line = []

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
                self.mode = "checking_line"

                self.search_start = shot_destination

                self.saved_lines = self.get_all_directions(shot_destination, board)
                self.current_line = self.saved_lines.pop()
                for loc in self.current_line[2]:
                    self.add_to_places_to_shoot(loc, board)

            if self.mode == "checking_line":
                if self.places_to_shoot == []:
                    #switch directions
                    if self.switch_direction(board) == False:
                        self.current_line = self.saved_lines.pop()
                        for loc in self.current_line[2]:
                            self.add_to_places_to_shoot(loc, board)

        elif shot_report == 0 and self.mode == "checking_line":
            self.places_to_shoot = []
            if self.saved_lines != []:
                if self.switch_direction(board) == False:
                    self.current_line = self.saved_lines.pop()
                    for loc in self.current_line[2]:
                        self.add_to_places_to_shoot(loc, board)

        elif shot_report == 2:
            self.places_to_shoot = []
            self.saved_lines = []

    # Not bieng used currently
    def line_orientation_temp(self, point1, point2):
        y1, x1 = point1
        y2, x2 = point2
        if y1 == y2:
            return "Horizontal"
        elif x1 == x2:
            return "Vertical"
        else:
            return "No Line"

    # Not being used currently
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

    def get_full_line(self, originTuple, orientation, board):

        orgY, orgX = originTuple

        line_locations = []

        hit_miss_high, hit_miss_low = False, False
        mod = 1
        while not hit_miss_low or not hit_miss_high:
            if orientation == "Horizontal":
                xMod = mod
                yMod = 0
            elif orientation == "Vertical":
                yMod = mod
                xMod = 0
            if orgX+xMod >= board.get_length() or orgY+yMod >= board.get_height() or board.firedMap[orgY+yMod][orgX+xMod] == "X":
                hit_miss_high = True
            elif not hit_miss_high:
                line_locations.append((orgY+yMod, orgX+xMod))
            if orgX-xMod < 0 or orgY-yMod < 0 or board.firedMap[orgY-yMod][orgX-xMod] == "X":
                hit_miss_low = True
            elif not hit_miss_low:
                line_locations.append((orgY-yMod, orgX-xMod))
            mod += 1
        line_locations.reverse()

        return line_locations

    def get_half_line(self, originTuple, direction, board):

        orgY, orgX = originTuple
        line_locations = []

        mod = 1
        xMod, yMod = 0, 0
        while True:
            if direction == "Right":
                xMod = mod
            elif direction == "Left":
                xMod = -mod
            elif direction == "Down":
                yMod = mod
            elif direction == "Up":
                yMod = -mod
            if orgX+xMod < 0 or orgX+xMod >= board.get_length() or orgY+yMod < 0 or orgY+yMod >= board.get_height() or board.firedMap[orgY+yMod][orgX+xMod] == "X":
                break
            else:
                line_locations.append((orgY+yMod, orgX+xMod))
            mod += 1
        line_locations.reverse()

        return line_locations

    def get_all_directions(self, originTuple, board):
        lines = []

        up = self.get_half_line(originTuple, "Up", board)
        right = self.get_half_line(originTuple, "Right", board)
        down = self.get_half_line(originTuple, "Down", board)
        left = self.get_half_line(originTuple, "Left", board)

        if up != []:
            lines.append(["Up", len(up), up])
        if right != []:
            lines.append(["Right", len(right), right])
        if down != []:
            lines.append(["Down", len(down), down])
        if left != []:
            lines.append(["Left", len(left), left])

        return lines

    def get_reverse_direction(self, direction):
        if direction == "Up":
            return "Down"
        elif direction == "Down":
            return "Up"
        elif direction == "Right":
            return "Left"
        elif direction == "Left":
            return "Right"

    def switch_direction(self, board):
        new_direction = self.get_reverse_direction(self.current_line[0])

        for line in self.saved_lines:
            if line[0] == new_direction:
                self.current_line = line
                self.saved_lines.remove(line)
                for loc in self.current_line[2]:
                    self.add_to_places_to_shoot(loc, board)
                return True
        return False
