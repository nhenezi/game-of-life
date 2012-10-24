#! /usr/bin/python

import sys

CELL = "*"
EMPTY = "O"

if __name__ == "__main__":
  f = open("in", "r")
  board = map(lambda x: 
              map(lambda y: y, x.replace("\n", ""))
              ,f.readlines())

    
