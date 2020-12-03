#D2 4871 그래프 경로

def dfs(node_index, visited, nodes):
    visited[node_index] = 1
    for node in nodes[node_index]:
        if visited[node] != 1:
            dfs(node, visited, nodes)


for t in range(int(input())):
    V, E = map(int, input().split())
    nodes = [ [] for _ in range(V+1) ]
    for _ in range(E):
        start, end = map(int, input().split())
        nodes[start].append(end)
    S, G = map(int, input().split())
    visited = [ 0 for _ in range(V+1)]
    dfs(S, visited, nodes)
    answer = 0
    if visited[G] == 1:
        answer = 1
    print('#{} {}'.format(t+1, answer))