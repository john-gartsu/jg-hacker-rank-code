'''
https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
string-validators

Python has built-in string validation methods for 
basic data. It can check if a string is composed 
of alphabetical characters, alphanumeric characters
, digits, etc.

Task

You are given a string S .
Your task is to find out if the string S contains:
 alphanumeric characters, alphabetical characters,
  digits, lowercase and uppercase characters.
'''

if __name__ == '__main__':
    # correct
    s = input()

    # test local True
    # s = '2aP'
    # test local False
    # s = '!*&^'

    print(any(a.isalnum() for a in s))
    print(any(a.isalpha() for a in s))
    print(any(a.isdigit() for a in s))
    print(any(a.islower() for a in s))
    print(any(a.isupper() for a in s))

   ''' for chars in s:
        if chars.isalnum():
            print(True)
        elif chars.isalpha():
            print(True)
        elif chars.isdigit():
            print(True)
        elif chars.islower():
            print(True)
        elif chars.isupper():
            print(True)
        else:
            print(False)'''