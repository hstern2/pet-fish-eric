#!/usr/bin/env python3

### reading and writing files

#from sys import stdout
 
### reading from a text file line by line
#with open('in1.txt') as f:
#    n = 1
#    for line in f:
#        stdout.write(f'{n}: {line}')
#        n += 1

### writing to a file
#with open('out.txt','w') as f:
#     f.write('hi there\n')
#     f.write('here is some output\n')
#     f.write(str(23))
#     f.write('\n')

### reading comma separated values
#import csv
# 
#with open('in2.csv') as f:
#    for line in csv.reader(f):
#        print(line)

### changing delimiter
#with open('in3.txt') as f:
#    for line in csv.reader(f, delimiter=' '):
#        print(line)

### read comma separated values with headings into a dictionary
#with open('in4.csv') as f:
#    for line in csv.DictReader(f):
#           print(line)
#           print('Batch id: ' + line['batchID'])
