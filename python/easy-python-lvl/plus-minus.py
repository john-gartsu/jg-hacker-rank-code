'''
plus or minus hacker rank
https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    # number of array elements
    arr_length = len(arr)
    # print(arr_length)
    for num in arr:
        # check each value in arr if 0, neg, or pos
        if num == 0:
            zero += 1
            # return zero
        if num > 0:
            pos += 1
            # return pos
        if num < 0:
            neg += 1
            # return neg
    '''   
    only for visual aid     
    print(f'### pos count: {pos}')
    print(f'### neg count: {neg}')
    print(f'### zero count: {zero}')
    '''
    # return f'### pos count: {pos}, ### neg count: {neg}, ### zero count: {zero}'
    # print(pos, neg, zero) 
    return pos, neg, zero
    
    pos_ratio = pos/arr_length


        



        

if __name__ == '__main__':
    # @correct
    # n = int(input().strip())
    # @correct
    # arr = list(map(int, input().rstrip().split()))

    arr = [1, 1, 0, -1, -2]
    plusMinus(arr)
