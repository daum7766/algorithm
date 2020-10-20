# N과 M(2)
def dfs(idx, k):
    if idx == M:
        answer.append(checked[:])
        return
    for i in range(k+1, N):
        if visited[i]:
            visited[i] = 0
            checked[idx] = i+1
            dfs(idx+1, i)
            visited[i] = 1

N, M = map(int, input().split())


visited = [1 for _ in range(N)]
checked = [0 for _ in range(M)]
answer = []
dfs(0, -1)
for i in answer:
    print(*i)