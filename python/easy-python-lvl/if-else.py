"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 30, print Weird
If  is even and greater than  20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints
1 </= n </= 100

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""



import math
import os
import random
import re
import sys

def odd_or_even_weird(n):
    if n % 2 != 0:
        # if odd
        print("Weird")
    if n % 2 == 0 and n in range(2,6):
        print('Not Weird')
    if n % 2 == 0 and n in range(6,21):
        print("Weird")
    if n % 2 == 0 and n > 20:
        print("Not Weird")



if __name__ == '__main__':
    n = int(input().strip())
    odd_or_even_weird(n)
