# Silver 1 최소 힙

import heapq
from sys import stdin, stdout

queue = []

N = int(stdin.readline())

for _ in range(N):
    a = int(stdin.readline())
    if a:
        heapq.heappush(queue, a)
    else:
        if len(queue):
            stdout.write('{}\n'.format(heapq.heappop(queue)))
        else:
            stdout.write('0\n')