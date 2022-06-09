#!/bin/python3
'''
Objective
Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.

Example
Print 4 3 2 1. Each integer is separated by one space.

Input Format
The first line contains an integer,  (the size of our array).
The second line contains  space-separated integers that describe array 's elements.

Constraints

, where  is the  integer in the array.
Output Format

Print the elements of array  in reverse order as a single line of space-separated numbers.

'''



import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # @correct for hrank
    # n = int(input().strip())
    # @local-test
    n = 4

    # @correct 
    # arr = list(map(int, input().rstrip().split()))
    # @local-test
    arr = [4, 3, 2, 1]

    # use array/list slice to reverse array list
    rev_arr = arr[::-1]
    # @local-testing
    # print(f'### Reverse array for arr: {arr}  == {rev_arr} ###')
    
    # 
    # Loop each number in the reverse arr/list
    # Seperate with a space
    # 
    for num in rev_arr:
        print(num, end=' ')
   
#    
# If goal was to return reverse array without ","
# 
"""
    rev_arr_comma_split = ''.join(str(rev_arr).split(','))
    print(rev_arr_comma_split)
"""