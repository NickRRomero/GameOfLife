#!/usr/bin/python
import numpy as np
import random

def greet_user():
   """
   Provide the user with instructions for the GameOfLife.
   """
   print """Welcome to The Game Of Life.\n""" 

def create_board():
   return np.random.randint(2, size=(10, 10))


if __name__ == "__main__":
   greet_user()
   print create_board()
