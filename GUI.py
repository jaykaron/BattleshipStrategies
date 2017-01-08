from Tkinter import *
import GAME

gridSize = 40

class Gui():
    def __init__(self, board):
        self.master = Tk()
        self.canvas = Canvas(self.master, width=20+board.get_length()*gridSize, height=20+board.get_height()*gridSize)
        self.canvas.pack()
        self.rects = {}
        for y in range(board.get_height()):
            for x in range(board.get_length()):
                self.rects[(x,y)] = self.canvas.create_rectangle(10+x*gridSize,10+y*gridSize, 10+(x+1)*gridSize,10+(y+1)*gridSize, fill="blue")

        self.master.bind('<Return>', self.update_canvas)
        self.master.mainloop()

    def update_canvas(self, event):
        GAME.shoot_random(GAME.board1)
        for y in  range(GAME.board1.get_height()):
            for x in range(GAME.board1.get_length()):
                if GAME.board1.firedMap[y][x] == 'X':
                    self.canvas.itemconfig(self.rects[(x,y)], fill="orange")
                elif GAME.board1.firedMap[y][x] == '#':
                    self.canvas.itemconfig(self.rects[(x,y)], fill="red")


screen1 = Gui(GAME.board1)
