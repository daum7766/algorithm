# D2 5102 노드의 거리


def bfs(queue):
    count = 1
    while queue:
        s_queue = []
        while queue:
            index = queue.pop()
            for i in node[index]:
                if visited[i]: continue
                if i == end: return count
                s_queue.append(i)
                visited[i] = 1
        count += 1
        queue = s_queue
    return 0

for t in range(1, int(input()) + 1):
    #V개의 노드, E개의 간선
    V, E = map(int, input().split())
    #리스트를 이용한 간선 표시
    node = [[] for _ in range(V+1)]
    #방문여부
    visited = [0 for _ in range(V+1)]
    #데이터 편집
    for i in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    #시작노드와 끝나는 노드 저장
    start, end = map(int, input().split())
    #시작노드 방문처리
    visited[start] = 1
    #bfs 돌리기
    print('#{} {}'.format(t, bfs([start])))