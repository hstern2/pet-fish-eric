#!/usr/bin/env python3

### pandas (Python Data Analysis Library) - part 2

#import pandas
#from random import random

#s1 = pandas.Series(data=[random() for i in range(5)], index=['a','b','c','d','e'])
#s2 = pandas.Series(data={'a':1.0, 'b':2.0, 'c':3.0, 'd':4.0})

#df = pandas.DataFrame({'col1': s1, 'col2': s2})
#print('data frame:')
#print(df)
#print('\n')

#df = pandas.read_csv('in4.csv', index_col='id')
#print('data frame from csv:')
#print(df)
#print('\n')

#print('a column:')
#print(df['value'])
#print('\n')

#print('an element:')
#print(df['value']['DEF2'])
#print(df.loc['DEF2']['value'])

#print('several columns:')
#print(df[['sampleName','sampleType','value']])
#print('\n')

#print('a row:')
#print(df.loc['DEF2'])
#print('\n')

#print('several rows:')
#print(df.loc[['ABC1','GHI3','JKL4']])
#print('\n')

#print('(1) row selection from array of booleans:')
#print(df[ [False,False,True,True] ])
#print('\n')

#print('(2) boolean array, given a condition:')
#print(df['value'] > 0.5)
#print('\n')

#print('combining (1) and (2):')
#print(df[ df['value'] > 0.5 ])
#print('\n')

#print('a query for particular sampleNames...')
#print(df[ ['Sh2' in n for n in df['sampleName']] ])
#print('\n')

#d1 = [[random() for i in range(4)] for j in range(4)]
#rlabel = ['a','b','c','d']
#clabel = ['A','B','C','D']
#df1 = pandas.DataFrame(data=d1, index=rlabel, columns=clabel)

#d2 = [[random() for i in range(4)] for j in range(4)]
#rlabel = ['a','b','c','d']
#clabel = ['A','B','C','D']
#df2 = pandas.DataFrame(data=d2, index=rlabel, columns=clabel)

#print('numerical data:')
#print(df1)
#print('\n')
#print(df2)
#print('\n')

#print('vector sum:')
#print(df1+df2)
#print('\n')

#print('comparison:')
#print(df1 < df2)
#print('\n')

#print('describe:')
#print(df1.describe())
