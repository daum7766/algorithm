# silver3 N과 M(1)

def dfs(idx, current):
    if idx == M:
        print(*answer)
        return
    for i in range(N):
        if visited[i] == True:
            visited[i] = False
            answer[current] = i+1
            dfs(idx+1, current+1)
            visited[i] = True

N, M = map(int, input().split())

visited = [True for _ in range(N+1)]
answer = [0 for _ in range(M)]

dfs(0, 0)