#!/usr/bin/env python3

### pandas (Python Data Analysis Library) - part 1

#import pandas
#from random import random

#d = [random() for i in range(5)]
#print(d)
#labels = ['a','b','c','d','e']

#s1 = pandas.Series(data=d, index=labels)
#print('whole series:')
#print(s1)
#print('\n')

#print('item by label:')
#print(s1['a'])
#print(s1[2])
#print('\n')

#print('slice:')
#print(s1[['c','a','e']])
#print('\n')

#print('(1) selection from array of booleans:')
#print(s1[ [True,False,False,True,True] ])
#print('\n')

#print('(2) boolean array, given a condition:')
#print(s1 > 0.2)
#print('\n')

#print('combining (1) and (2):')
#print(s1[ (0.2 < s1) & (s1 < 0.8) ])
#print('\n')

#print('some statistics... (numpy ndarray functions)')
#print(f'count of non-null values: {s1.count()}')
#print(f'sum: {s1.sum()}')
#print(f'mean: {s1.mean()}')
#print(f'median: {s1.median()}')
#print(f'variance: {s1.var()}')
#print(f'mean absolute deviation: {s1.mad()}')
#print(f'standard deviation: {s1.std()}')
#print(f'standard error of mean: {s1.sem()}')
#print(f'skew: {s1.skew()}')
#print(f'kurtosis: {s1.kurt()}')
#print(f'max: {s1.max()}')
#print(f'min: {s1.min()}')
#print('\n')

#s2 = pandas.Series(data={'a':1.0, 'b':2.0, 'c':3.0, 'd':4.0})
#print('series from dictionary:')
#print(s2)
#print('\n')

#print('vector sum (with NaN for missing value):')
#print(s1+s2)
#print('\n')

#print('test for NaNs...')
#sum = s1+s2
#print(sum.notnull())
#print('\n')

#print('filter out NaNs:')
#print(sum[sum.notnull()])
#print('\n')
