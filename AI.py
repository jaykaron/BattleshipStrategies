# -*- coding: utf-8 -*-
"""
Created on Sun May 15 16:26:44 2016

@author: joshuakaron
"""
from random import randint
from random import shuffle
import Board


# this class is meant to be inherited by all AI classes

cpl = open('captains_log.txt', 'r')

locations_to_shoot = []
# record of past guesses in the form of a tuple
past_shots = []
# connects the past guesses (tuples) to the responses
responses = {}

for i in range(Board.height):
    for j in range(Board.length):
        locations_to_shoot.append((i,j))

shuffle(locations_to_shoot)
index = 0

def fire():
    # this outer IF statement is to make shure the second IF dosnt execute on the first turn
    if len(past_shots) != 0:
        if responses[past_shots[len(past_shots)-1]] == 'Hit!':
            print('sink_ship()')
            sink_ship()

    #index = randint(0, len(locations_to_shoot) - 1)
    global index
    output = locations_to_shoot[index]
    index += 1
    past_shots.append(output)

    return output

#this method is called once a ship has been hit once
def sink_ship():
    past_shot = past_shots[len(past_shots) - 1]
    past_row = past_shot[0]
    past_col = past_shot[1]

    # set next shot to right
    if past_col + 1 in range(Board.length):
        if Board.firedMap[past_row][past_col + 1] == 'X':
            locations_to_shoot.insert(index,(past_row,past_col + 1))
