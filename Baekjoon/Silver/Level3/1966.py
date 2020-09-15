# silver 3 프린터 큐
from sys import stdin, stdout
from collections import deque

def get_max(queue):
    max_num = 0
    for i in range(len(queue)):
        if queue[i][1] > max_num:
            max_num = queue[i][1]
    return max_num


t = int(stdin.readline())

for _ in range(t):
    N, M = map(int, stdin.readline().split())
    user_input = list(map(int, stdin.readline().split()))
    queue = deque()
    for i in range(N):
        queue.append((i, user_input[i]))

    cnt = 0
    while 1:
        max_num = get_max(queue)
        idx, num = queue.popleft()
        if num == max_num:
            cnt += 1
            if idx == M:
                print(cnt)
                break
        elif num != max_num:
            queue.append((idx, num))