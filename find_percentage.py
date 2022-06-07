'''
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        # print(f'### name: {name}')
        # print(f'### scores: {scores}')
        student_marks[name] = scores
        # print(f'### student_marks[name]: {student_marks[name]}')
    query_name = input()
    # print(query_name)
    # if query_name == name:
    total = sum(student_marks[name])
    grade_avg = total/3
    print('%.2f'%(grade_avg))

'''
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total_marks = sum(student_marks[query_name])
average_marks = total_marks/3 
print("%.2f"%(average_marks))
'''