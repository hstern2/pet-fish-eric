#!/usr/bin/env python3

### lists - part 1

### This is a list
#a = ['hello','world','my','lucky','number','is', 37]
#print(a)

### Lists are indexed from zero
#print(a[0], a[4])

### Lists have bounds checking
#print(a[37])

### Negative numbers mean from the end
#print(a[-1], a[-2])

### A slice is a range, from first index (included) to last index (excluded)
#print(a[1:3])
#print(a[2:-2])
#print(a[4:])

### copy vs new reference
#b = a # [:]
#a[0] = 'something else'

### Lists can be created with a range
#print(list(range(23)))     # 0 through 22 
#print(list(range(1,10)))   # 1 through 9 
#print(list(range(0,31,5)))   # 0 through 30 by 5's
