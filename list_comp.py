'''
list comprehension
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
     list_comp = [[x,y,z] for x in [i,j,k] for y in [i,j,k] if i+j+k != n]
     print(list_comp)