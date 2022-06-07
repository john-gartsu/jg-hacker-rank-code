for test in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        division_result = a // b
        print(division_result)
    except ZeroDivisionError as err:
        print("Error Code:", err)
    except ValueError as err:
        print("Error Code:", err)