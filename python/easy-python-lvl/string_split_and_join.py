
def split_and_join(line):
    # write your code here
    new_str = line.split(" ")
    joined_str = "-".join(new_str)
    # return result = joined_str  
    return joined_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)