# Silver 1 숨바꼭질
from collections import deque

N, K = map(int, input().split())
MAX_SIZE = 100001
visited = [0 for _ in range(MAX_SIZE)]

queue = deque()
queue.append(N)
while queue:
    pos = queue.popleft()
    if pos == K:
        break
    pos_list = [pos-1, pos+1, pos*2]
    for p in pos_list:
        if 0 <= p < MAX_SIZE and (visited[p] == 0 or visited[pos] + 1 < visited[p]):
            queue.append(p)
            visited[p] = visited[pos] + 1


print(visited[K])