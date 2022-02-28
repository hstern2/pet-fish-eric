#!/usr/bin/env python3

### regular expressions

# from re import search, sub

### simple search
#pattern = r'hi'  # good to use raw strings for regular expressions
#string = 'osidgoin hi aoidnfoisn'
#print('found' if search(pattern,string) else 'not found')

### \d means digit (0 through 9)
### [a-z]+ means one or more lowercase letters
#pattern = r'\d [a-z]+'
#string = '9 asdoin'
#print('found' if search(pattern,string) else 'not found')

### \w means "word character" (A-Z, a-z, 0-9, _)
### \s means "whitespace"  (space, tab, newline)
#pattern = r'\s\w\w\w\s'
#string = ' a8b\t'
#print('found' if search(pattern,string) else 'not found')

### group 1: one of the four letters A,C,G,T, one or more times
### group 2: a lower case letter, one or more times, 
### followed by (one or more whitespace characters), followed by one digit
#pattern = r'([ACGT]+) ([a-z]+\s+\d)'
#string = 'hello ACAGCATACGCA there 4 hi_'
#s = search(pattern,string)
# 
#if s: # if the pattern matches
#   print('DNA sequence: ' + s.group(1))
#   print('tag: ' + s.group(2))
#
#replacement = 'XXXX'
#print(sub(pattern, replacement, string))
