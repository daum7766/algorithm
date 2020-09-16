# silver 3 스택 수열
from sys import stdin, stdout

answer = []
stack = []
N = int(stdin.readline())

number = 1
is_impossible = False

for _ in range(N):
    user_input = int(stdin.readline())

    while user_input >= number:
        stack.append(number)
        answer.append('+')
        number += 1
    
    while 1:
        if not stack:
            is_impossible = True
            break
        num = stack.pop()
        answer.append('-')
        if num == user_input:
            break
    if is_impossible:
        break

if is_impossible:
    stdout.write('NO')
else:
    for i in answer:
        stdout.write('{}\n'.format(i))