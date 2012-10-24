#! /usr/bin/python

import sys
import time
from copy import deepcopy


CELL = "*"
EMPTY = "O"

def pprint(board):
  for i in xrange(len(board)):
    for j in xrange(len(board[i])):
      sys.stdout.write(board[i][j])
    print

def areSane(i, j, k, l, board):
  '''limit check'''
  if (i + k) >= 0 and (i + k) < len(board)\
        and (j + l) >= 0 and (j + l) < len(board):
    # ignore current field
    if k == 0 and l == 0:
      return False
    else:
      return True
  return False

def mutate(board, i, j):
  '''checks if board[i][j] will mutate'''
  n = 0
  for k in xrange(-1, 2):
    for l in xrange(-1, 2):
      if areSane(i, j, k, l, board)\
            and board[i + k][j + l] == CELL:
        n += 1

  # cell stays alive of 2 neighbours are alive
  if n == 2 and board[i][j] == CELL:
    return CELL
  elif n == 3:
    return CELL
  return EMPTY
        

def combine(board_even, board_odd):
  board = []
  for i in xrange(0,len(board_even)):
    if i%2 == 0:
      board.append(board_even[i])
    else:
      board.append(board_odd[i])
  return board

if __name__ == "__main__":
  f = open("in", "r")
  board = map(lambda x: 
              map(lambda y: y, x.replace("\n", ""))
              ,f.readlines())

  while (1):
    board_even = deepcopy(board)
    board_odd = deepcopy(board)
    for i in xrange(len(board)):
      for j in xrange(len(board)):
        if i%2 == 0:
          board_even[i][j] = mutate(board, i, j)
        else:
          board_odd[i][j] = mutate(board, i, j)
        
    board = combine(board_even, board_odd)
    pprint(board)
    time.sleep(0.5)
