#!/usr/bin/python
import numpy as np
import random

def get_user_input():
   print """Welcome to The Game Of Life.\n""" 
   print """Please enter X for the size of the game board: X * X\n"""
   return input('Size: ')

def create_empty_board(board_size):
   return np.zeros((board_size, board_size), dtype=np.int8, order='C')



if __name__ == "__main__":
   board_size = get_user_input()
   print create_empty_board(board_size)
