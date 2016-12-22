# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:10:51 2016

@author: joshuakaron
"""
from random import randint

board = []
is_over = False

for i in range(0,5):
    board.append(['0']*5)
    
def print_board(board):
    for row in board:
        print(" ".join(row))
        
def random_row(board):
    return randint(0, len(board) - 1)
    
def random_col(board):
    return randint(0, len(board) - 1)
        
ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)


while is_over == False:
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        is_over = True    
        print('You Win!!!')
    elif guess_row not in range(0,5) or guess_col not in range(0,5): 
        print('Invalid guess')
    elif board[guess_row][guess_col] == 'X':
        print('You guessed that already')
    else:
        print('missed')
        board[guess_row][guess_col] = 'X'
        print_board(board)