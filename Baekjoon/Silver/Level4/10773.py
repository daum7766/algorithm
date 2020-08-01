# silver 4 제로
from sys import stdin, stdout
N = int(stdin.readline())

answer = []
for _ in range(N):
    k = int(stdin.readline())
    if k:
        answer.append(k)
    else:
        answer.pop()
stdout.write(str(sum(answer)))