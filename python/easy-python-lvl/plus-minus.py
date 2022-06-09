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
    # init value count
    pos = 0
    neg = 0
    zero = 0
    # loop for each element in arr starting at idx 0
    for idx in range(0, len(arr)):
        # check each value in arr if 0, neg, or pos
        # @only-testing
        # print(f'### num in arr at idx- {idx}: {arr[idx]}')
        # check for amount of zeros  && add to count
        if arr[idx] == 0:
            zero += 1
        # check for number of positives (>0) && add to count
        if arr[idx] > 0:
            pos += 1
        # check for num < 0 (negative)
        if arr[idx] < 0:
            neg += 1
        # return pos, neg, zero
      # number of array elements
    #   @only-testing
    # return f'### pos count: {pos}, ### neg count: {neg}, ### zero count: {zero}'
    
    # length of arr to get total
    arr_length = len(arr)
    # @local-testing
    # print(arr_length )
    pos_ratio = pos/arr_length
    neg_ratio = neg/arr_length
    zero_ratio = zero/arr_length
    print(pos_ratio)
    print(neg_ratio)
    print(zero_ratio)


if __name__ == '__main__':
    # @correct
    n = int(input().strip())
    # @correct
    arr = list(map(int, input().rstrip().split()))

    # local test only @testing
    # arr = [1, 1, 0, -1, -2]
    # print(plusMinus(arr)) #@testing
    # @correct
    plusMinus(arr)
