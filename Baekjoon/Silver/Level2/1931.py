# Silver 2 회의실 배정

from sys import stdin, stdout

N = int(stdin.readline())

rooms = []

for _ in range(N):
    start, end = map(int, stdin.readline().split())
    rooms.append((start, end))
# 종료시간 기준으로 먼저 정렬해야 뒤에사람이 일찍 쓸 수 있다.
rooms.sort(key=lambda x: (x[1], x[0]))
before = 0
answer = 0
for start, end in rooms:
    if before <= start:
        answer += 1
        before = end

stdout.write('{}\n'.format(answer))