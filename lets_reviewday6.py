'''
let_review day 6 question
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

def even_odd_idx(s,n):
    n = int(input("Enter string length: "))
    chars = []
    for i in range(0,n):
        s = input("Enter string: ") 
        chars.append(s)
    
    for i in range(0,n):
        for j in range(0, len(chars[i]),2):
            print(chars[i][j], end='')
        print(end=' ')
    for j in range(1,len(chars[i]),2):
        print(chars[i][j],end='')
    # print()
    
even_odd_idx(S,N)
        
        