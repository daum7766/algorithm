# Silver 3 바이러스
from sys import stdin

def dfs(n):
    global answer
    for i in computers[n]:
        if virus[i] == 0:
            virus[i] = 1
            answer += 1
            dfs(i)

N = int(stdin.readline())
M = int(stdin.readline())

computers = [[] for _ in range(N+1)]
virus = [0 for _ in range(N+1)]
virus[1] = 1
answer = 0

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    computers[a].append(b)
    computers[b].append(a)

dfs(1)

print(answer)