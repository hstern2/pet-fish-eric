#!/usr/bin/env python3

### sudoku puzzle solver

from sys import stdout
from random import random
from copy import deepcopy
from argparse import ArgumentParser

class Square():
    def __init__(self):
        self.n = -1
        self.excluded = [False]*9
    def is_known(self):
        return self.n >= 0
    def write(self, f):
        f.write(str(self.n+1) if self.is_known() else ' ')
    def how_many_excluded(self):
        return sum([1 for x in self.excluded if x])
    
class Config():
    def __init__(self):
        self.square = [[Square() for i in range(0,9)] for j in range(0,9)]
    def write(self, f):
        for i in range(0,9):
            for j in range(0,9):
                self.square[i][j].write(f)
                f.write('|' if j in (2,5) else ' ')
            f.write('\n')
            if i in (2,5):
                f.write('-----+-----+-----\n')
        f.write('\n\n')
    def read(self, f):
        for i in range(0,9):
            a = f.readline().split()
            for j in range(0,9):
                n = int(a[j])
                if n > 0:
                    self.set_square(i,j,n-1)
    def set_square(self, i, j, n):
        self.square[i][j].n = n;
        # exclude squares in same row, column
        for k in range(0,9):
            if k != j:
                self.square[i][k].excluded[n] = True
            if k != i:
                self.square[k][j].excluded[n] = True
        # exclude squares in same box
        ni = 3*(i//3);
        nj = 3*(j//3);
        for ik in range(ni, ni+3):
            for jk in range(nj, nj+3):
                if ik != i or jk != j:
                    self.square[ik][jk].excluded[n] = True
    def infer(self):
        set_any_square = True
        while set_any_square:
            set_any_square = False;
            solved = True
            for i in range(0,9):
                for j in range(0,9):
                    s = self.square[i][j]
                    if s.is_known():
                        continue;
                    solved = False
                    if s.how_many_excluded() == 9:
                        return False, True
                    elif s.how_many_excluded() == 8:
                        for k in range(0,9):
                            if not s.excluded[k]:
                                self.set_square(i,j,k)
                                set_any_square = True
                                break
            if solved:
                return True, False
        return False, False

    def unknown_squares(self):
        unk = list()
        for i in range(0,9):
            for j in range(0,9):
                s = self.square[i][j]
                if not s.is_known():
                    unk.append((i,j,s.how_many_excluded()))
        unk.sort(key = lambda i: i[2])
        unk.reverse()
        return [(t[0],t[1]) for t in unk]
                
def search(config):
    # First, make all inferences possible from current
    # configuration.  Determine if the puzzle is solved,
    # or the current configuration leads to a contradiction
    solved, contradiction = config.infer()
    config.write(stdout);
    if solved:
        return config
    if contradiction:
        return None
    # Neither solved, nor a contradiction - 
    # make a list of all unknown squares, with
    # how many numbers are excluded for each
    for i,j in config.unknown_squares():
        for y in range(0,9):
            if not config.square[i][j].excluded[y]:
                # Try a particular guess for this square
                config_save = deepcopy(config)
                print(f'Guessing {i+1},{j+1} = {y+1}')
                config.set_square(i,j,y);
                answer = search(config)
                if answer:
                    # The guess worked
                    print(f'Guess {i+1},{j+1} = {y+1} worked.')
                    return answer
                else:
                    print(f'Guess {i+1},{j+1} = {y+1} didn\'t work.')
                    config = config_save
                    config.square[i][j].excluded[y] = True
    return None

desc='Puzzle format: 9 rows of 9 numbers - a 0 means a blank space.'
ap = ArgumentParser(description=desc)
ap.add_argument('puzzle', help='input file containing puzzle')
args = ap.parse_args()

c = Config()
with open(args.puzzle) as f:
  c.read(f)

print('Puzzle:')
c.write(stdout)
answer = search(c)
if answer:
    print('Answer:')
    answer.write(stdout)
else:
    print('Couldn\'t find answer.')
