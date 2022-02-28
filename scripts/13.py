#!/usr/bin/env python3

### command-line arguments

# from argparse import ArgumentParser
#  
# desc = '''Here is a description of my program.
# This might be long so I am putting this in a multiline string.
# Three quote marks are used for that....'''

### default value for number of iterations
# DEFAULT_N = 20 # convention - put constants in CAPS
# 
# p = ArgumentParser(description=desc)

### an optional integer command line argument
# p.add_argument('-n', type=int, 
#                help=f'number of iterations (default: {DEFAULT_N})', 
#                default=DEFAULT_N)

### a required string argument (one or more)
# p.add_argument('file', nargs='+', help='input files') 
# 
# args = p.parse_args() # namespace of command line arguments
# 
# print('number of iterations: {:d}'.format(args.n))
# for f in args.file:
#   print('I am going to process input file: ' + f)
