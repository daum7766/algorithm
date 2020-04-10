# D2 5102 노드의 거리

#BFS 함수
def bfs(queue):
    count = 1
    #큐가 빌때까지 반복
    while queue:
        #2개의 큐가 필요하므로 한개더 생성한다.
        s_queue = []
        #큐가 빌때까지 반복한다.
        while queue:
            #원소를 꺼내서
            index = queue.pop()
            #연결되어 있는 부분들을 확인한다.
            for i in node[index]:
                #이미 방문했다면 넘어간다.
                if visited[i]: continue
                #도착지와 일치한다면 이동거리를 반환한다.
                if i == end: return count
                #위의 조건에 걸리지 않는다면 두번재 큐에 추가한다.
                s_queue.append(i)
                #방문처리를 한다.
                visited[i] = 1
        #모든 큐가 비었다면 카운트를 증가시킨다.
        count += 1
        #큐를 교체한다.
        queue = s_queue
    #여기까지 왔다면 목적지까지 도착할 수 없다.
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