print('hello world')
v='hii'
print('heyy'+ v)
import copy

l = [1,2,3,4,5]
l2 = copy.copy(l)
print l2
l.pop()
print l
print l2




l1 = [[1,2,3,4],5,6]
l3 = copy.copy(l1)
print l3
l1[0].append(7)
print l1
print l3

from random import randint


print randint(0,9), randint(0,9), randint(0,9)
