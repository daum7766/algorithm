#D3 5209 최소 생산비용

def dfs(idx, _sum):
    global answer
    if _sum >= answer:
        return
    if idx == N:
        answer = _sum
    for i in range(N):
        if visited[i]:
            visited[i] = 0
            dfs(idx+1, _sum + V[idx][i])
            visited[i] = 1


for t in range(int(input())):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [1 for _ in range(N)]
    answer = 999999
    dfs(0, 0)
    print('#{} {}'.format(t+1, answer))