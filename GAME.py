import BOARD
import AIMASTER, AICLASSIC, AICHECKERED
from random import randint
import matplotlib.pyplot as plt

board1 = BOARD.Board(10,10, [5,4,3,3,2])

board1.print_ships()

classicP = AICLASSIC.AiClassic()
checkeredP = AICHECKERED.AiCheckered()
randomP = AIMASTER.AiMaster()


def play_game(board, player, print_turns=True):
    while board.shipsLeft > 0:
        player.make_decision(board)
        if print_turns:
            board.print_shots()
    print("Game Over")
    turns = len(player.log)
    print("Turns: " + str(turns))
    return turns

def take_average(board, player, runs, graph=False, new_board=False, print_turns=False):
    total_turns = 0

    #for graph
    if graph:
        number_of_turns = []
        number_of_occurences = []

    for gameN in range(0, runs):
        turns = play_game(board, player, print_turns)
        total_turns += turns
        if new_board:
            print("Board Layout:")
            board.print_ships()
            board = BOARD.Board(10,10, [5,4,3,3,2])
        else:
            board.reset()
        player = player.__class__() #Creates a new instance of the same class

        if graph:
            if turns not in number_of_turns:
                number_of_turns.append(turns)
                number_of_occurences.append(1)
            else:
                number_of_occurences[number_of_turns.index(turns)] += 1

    average = total_turns/runs
    print("-----------------")
    print("Number of Games: "+str(runs))
    print("Average Number of Turns: "+str(average))

    if new_board == False:
        print("Board Layout:")
        board.print_ships()

    if graph:
        plt.bar(number_of_turns, number_of_occurences)
        plt.show()

#play_game(board1, classicP)
take_average(board1, classicP, 500, graph=True, new_board=True)
