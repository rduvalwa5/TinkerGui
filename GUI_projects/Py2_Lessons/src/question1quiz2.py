'''
Created on Mar 14, 2013
Question 1:
Write an expression that takes two lists of equal length, k and v, and produces a dict where the keys 
are the elements of k and the corresponding values are the elements of v.
>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> dictionary = dict(zip(keys, values))
>>> print dictionary
'''

v = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
k = [1, 2, 3, 4, 5]

dick = dict(zip(k, v))
tup = zip(k, v)
for i in tup:
    print(i)
print(dick)
print(sorted(dick))


