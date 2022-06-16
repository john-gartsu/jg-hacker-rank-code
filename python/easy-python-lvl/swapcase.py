def swap_case(s):
    new_string = ''
    for letter in s:
        if letter.isupper():
            new_string += letter.lower()
        if letter.islower():
            new_string += letter.upper()
    return new_string

if __name__ == '__main__':
    # @correct
    s = input()
    #localtest
    # s='sUpEER'
    result = swap_case(s)
    print(result)