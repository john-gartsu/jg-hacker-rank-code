"""
https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs 
in the given string. String traversal will take place from left to 
right, not from right to left.

"""

def count_substring(string, sub_string):
    sub_str_count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        l = i
        for j in range(0, len(sub_string)):
            if string[l] == sub_string[j]:
                l +=1
                if j == len(sub_string)-1:
                    sub_str_count = sub_str_count + 1
                else:
                    continue
            else:
                break
    return sub_str_count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count