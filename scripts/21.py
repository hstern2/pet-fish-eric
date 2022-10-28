#!/usr/bin/env python3

### pandas (Python Data Analysis Library) - part 3

#import pandas
#from random import random

#a1 = pandas.read_csv('in.a1.csv', index_col='id')
#a2 = pandas.read_csv('in.a2.csv', index_col='id')
#a3 = pandas.read_csv('in.a3.csv', index_col='id')

#print('a1:')
#print(a1)
#print('\n')
#print('a2:')
#print(a2)
#print('\n')
#print('a3:')
#print(a3)
#print('\n')

#a1_a2 = a1.join(a2, how='outer')
#print('a1 join a2:')
#print(a1_a2)
#print('\n')

#a2_a3 = a2.join(a3, lsuffix='_a', rsuffix='_b', how='outer')
#print('a2 join a3:')
#print(a2_a3)
#print('\n')

#a1_a2_a3 = a1.join(a2, how='outer').join(a3, lsuffix='_a', rsuffix='_b', how='outer')
#print('a1 join a2 join a3 - outer')
#print(a1_a2_a3)
#print('\n')

#print('test for NaN:')
#print(a1_a2_a3.notnull())
#print('\n')

#print('all: True if all rows in a column are True (for axis=0)')
#print('     or all columns in a row are True (for axis=1)')
#print(a1_a2_a3.notnull().all(axis=1))
#print('\n')

#print('get only rows with no NaNs')
#print(a1_a2_a3[a1_a2_a3.notnull().all(axis=1)])
#print('\n')

#print('but this is much easier!')
#a1_a2_a3 = a1.join(a2, how='inner').join(a3, lsuffix='_a', rsuffix='_b', how='inner')
#print('a1 join a2 join a3 - inner')
#print(a1_a2_a3)
#print('\n')
