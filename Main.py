# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:18:27 2016

@author: joshuakaron
"""
# Battle Ships Main

from Ship import Ship
import Board
import AI
from random import randint

#AircraftCarrier 
#ACC = Ship(5)

#Battle Ship
#BS = Ship(4)

#Submarine
S = Ship('S', 3)

#Destroyer
D = Ship('D', 3)

#Patroll Boat
P = Ship('P', 2)

# list of ship objects
ships = [S, D, P]

# Dictonary of ships with there string representation as keys
ship_names = {'P':P, 'D':D, 'S':S}


# place ships
for ship in ships:
    Ship.place(ship)

Board.print_board(Board.hidden)

turn_count = 0

# File used to comuicate to the AI class
cpl = open('captains_log.txt', 'w+')

while Ship.game_over == False:
    
    # for human player
    #guess_row = int(input("Guess Row: "))
    #guess_col = int(input("Guess Col: "))
    
    # for AI player
    guess = AI.fire()
    guess_row = guess[0]
    guess_col = guess[1]
    

    at_guess = Board.hidden[guess_row][guess_col]
    
    if at_guess in ship_names.keys():
        print('Hit!')
        #cpl.write('Hit!\n')
        AI.past_shots.append(guess)
        AI.responses.update({guess:'Hit!'})
        ship_names[at_guess].hit()
        if ship_names[at_guess].remaining == 0:
            print('You sank my ship')
            #cpl.write('You sank my ship\n')
        Board.player[guess_row][guess_col] = '#'
        Board.hidden[guess_row][guess_col] = 'X'
        Board.print_board(Board.player)
        turn_count += 1
    elif at_guess == '~':
        print('Missed')
        #cpl.write('Missed\n')
        AI.past_shots.append(guess)
        AI.responses.update({guess:'Missed'})
        Board.player[guess_row][guess_col] = 'X'
        Board.hidden[guess_row][guess_col] = 'X'
        Board.print_board(Board.player)
        turn_count += 1
    elif at_guess == 'X':
        print('You already shot there')
        cpl.write('You already shot there\n')

# delete the text in captains_log.txt to prepare for next game      
#cpl.seek(0)
#cpl.truncate()
cpl.close()  
print("You Win!!!")
print('Shots Taken: ', turn_count)