#D4 4871 그래프 경로

def dfs(node):
    visited[node] = False
    for i in graph[node]:
        if visited[i]:
            dfs(i)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [True for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        #단방향 그래프이므로 하나만 추가한다.
        graph[a].append(b)
    start, end = map(int, input().split())
    #시작노드를 출발점으로 dfs를 시작한다.
    dfs(start)
    result = 1
    #끝나는 노드를 못갔다면 0으로 결과를 바꾼다.
    if visited[end]:
        result = 0
    print("#{} {}".format(t, result))