"""

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

Find the Runner Up Score!

"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    '''
    make arr a set
    turn set arr back into list
    get second to last highest idx
    '''
    sorted_arr = sorted(list(set(arr)))[-2]
    print(sorted_arr)