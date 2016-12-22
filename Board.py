# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:16:02 2016

@author: joshuakaron
"""

height = 5 # number of rows
length = 5 # number of columns

shipLocations = []
for i in range(0,height):
    shipLocations.append(['~']*length)

firedMap = []
for i in range(0,height):
    firedMap.append(['~']*length)

def print_board(board):
    for row in board:
        print(" ".join(row))

def print_board_hidden(board):
    for row in board:
        for col in row:
            print(" ".join())
