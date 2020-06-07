#D4 5251 최소 이동 거리
import heapq

for t in range(int(input())):
    N, E = map(int, input().split())
    #0번을 기준으로  노드간의 거리를 계산
    distance =[0] + [float('inf') for _ in range(N)]
    #노드간 거리를 저장하는 변수
    node = [[] for _ in range(N+1)]
    #이미 노드를 방문했는지 체크하는 변수
    visited = [0 for _ in range(N+1)]
    #간선만큼 입력을 받아 저장
    for _ in range(E):
        a, b, c = list(map(int, input().split()))
        node[a].append((b, c))
    #약간 변형이긴한데 큐를 이용하여 시작
    #원래는 방문하지 않은것중 가장작은 노드를 찾아야함
    queue = []
    heapq.heappush(queue, (0, 0))
    #큐가 빌대까지 반복
    while queue:
        #큐에서 확인할 노드번호를 꺼냄
        d, idx = heapq.heappop(queue)
        if visited[a]:
            continue
        #방문 체크를 하고
        visited[idx] = 1
        #그 노드와 연결된 노드를 찾는다.
        for a, b in node[idx]:
            #a는 노드번호, b는 노드간 거리
            # 0번부터 노드a까지의 거리가 지금가는 경로보다
            # 비용이 크다면 갱신
            if distance[a] > d + b:
                distance[a] = d + b
                heapq.heappush(queue, (distance[a], a))
            #해당노드를 방문하지 않았다면 큐에 추가
    #노드 N번까지 거리를 보는것이므로 distance(N)을 출력
    print('#{} {}'.format(t+1, distance[N]))
