#!/usr/bin/env python3

### lists - part 2

### Modifying lists
#a = []
#print(a)
#a.append('hi')
#print(a)
#a.append('there')
#print(a)

#a.extend(['everyone','how','are','you'])
#print(a)

#a.insert(1,'oh')
#print(a)

#a.insert(2,'and greetings')
#print(a)

### remove (and return) last element from list
#b = a.pop()
#print(b)
#print(a)

### just delete an element 
#del a[2]
#print(a)

### or a slice
#del a[0:4]
#print(a)

### concatenate lists
#b = ['some','more','things']
#c = a+b
#print(c)

### reverse and sort 
#a.reverse()
#print(a)
#b.sort()
#print(b)

### map a function to every element of a list
#a = ['3.141','1.21','-3.45','46']
#print(a)
#b = map(float,a)
#print(list(b))

### list comprehensions - 
### another way to do the same thing, but more general
#b = [2*float(x) + 10 for x in a]
#print(b)
