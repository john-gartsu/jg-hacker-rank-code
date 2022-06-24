# 
# 
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# 
# 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):   
        print('YES')  
    else:  
        print('NO')
