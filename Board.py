# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:16:02 2016

@author: joshuakaron
"""

hidden = []
for i in range(0,5):
    hidden.append(['~']*5)
    
player = []
for i in range(0,5):
    player.append(['~']*5)
    
def print_board(board):
    for row in board:
        print(" ".join(row))
        
def print_board_hidden(board):
    for row in board:
        for col in row:
            print(" ".join())