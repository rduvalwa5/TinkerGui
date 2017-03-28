'''
Created on Mar 20, 2013

@author: rduvalwa2
'''
# Build and return a list
def firstn(n):
    print(n)
    num, nums = 0, []
    while num < n:
        print(num)
        nums.append(num)
        num += 1
        print(num)
        print(nums)
    return nums
    
    
sum_of_first_n = sum(firstn(12))
print(type(sum_of_first_n))
print(sum_of_first_n)
