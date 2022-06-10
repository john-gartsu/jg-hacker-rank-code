#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
# Recurision
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n == 1:
        return 1
    else:
        # recursively calls same fn
        n = n * factorial(n-1)
    return n

if __name__ == '__main__':
    # @hackerankcorrect
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # hackerrank @correct
    # n = int(input().strip())
    # local test
    n = 5

    result = factorial(n)
    # print(f'### result: {1*2*3*4*5} =  {result} ###')

    # @hackerankcorret
    # fptr.write(str(result) + '\n')

    # fptr.close()