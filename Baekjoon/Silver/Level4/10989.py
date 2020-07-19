# silver 4 수 정렬하기3
from sys import stdin, stdout

count = [0]*10001
N = int(stdin.readline())

for _ in range(N):
    count[int(stdin.readline())] += 1

for i in range(1, 10001):
    if count[i]:
        stdout.write('{}\n'.format(i)*count[i])