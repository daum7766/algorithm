#D4 5251 최소 이동 거리
from collections import deque

for t in range(int(input())):
    N, E = map(int, input().split())
    #0번을 기준으로  노드간의 거리를 계산
    distance =[0] + [float('inf') for _ in range(N)]
    #노드간 거리를 저장하는 변수
    node = [[] for _ in range(N+1)]
    #이미 노드를 방문했는지 체크하는 변수
    visited = [1 for _ in range(N+1)]
    #간선만큼 입력을 받아 저장
    for _ in range(E):
        a, b, c = list(map(int, input().split()))
        node[a].append((b, c))
    #약간 변형이긴한데 큐를 이용하여 시작
    #원래는 방문하지 않은것중 가장작은 노드를 찾아야함
    queue = deque()
    queue.append(0)
    #큐가 빌대까지 반복
    while queue:
        #큐에서 확인할 노드번호를 꺼냄
        idx = queue.popleft()
        #방문 체크를 하고
        visited[idx] = 0
        #그 노드와 연결된 노드를 찾는다.
        for n in node[idx]:
            #a는 노드번호, b는 노드간 거리
            a, b = n
            # 0번부터 노드a까지의 거리가 지금가는 경로보다
            # 비용이 크다면 갱신
            if distance[a] > distance[idx] + b:
                distance[a] = distance[idx] + b
            #해당노드를 방문하지 않았다면 큐에 추가
            if visited[a]:
                queue.append(a)
    #노드 N번까지 거리를 보는것이므로 distance(N)을 출력
    print('#{} {}'.format(t+1, distance[N]))


'''
#5251 다익스트라 알고리즘
for t in range(int(input())):
    N, E = map(int, input().split())
    #계속 함수호출하기 그러니까 캐스팅
    INF = float('inf')
    #0번을 기준으로  노드간의 거리를 계산
    distance =[0] + [INF for _ in range(N)]
    #노드간 거리를 저장하는 변수
    node = [[] for _ in range(N+1)]
    #이미 노드를 방문했는지 체크하는 변수
    visited = [1 for _ in range(N+1)]
    #간선만큼 입력을 받아 저장
    for _ in range(E):
        a, b, c = list(map(int, input().split()))
        node[a].append((b, c))
    #노드 개수만큼 반복(모든노드를 반복해야 하니까)
    for _ in range(N+1):
        #최소거리는 무한대로 두고
        min_distance = INF
        #인덱스도 초기화 해주고
        min_idx = 0
        #반복문 돌리면서 제일 거리가 짧은노드 찾기
        for i in range(N+1):
            if visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_idx = i
        #찾은 노드로 시작하는데 일단 방문체크부터
        visited[min_idx] = 0
        #그 노드와 연결된 노드를 찾는다.
        for n in node[min_idx]:
            #a는 노드번호, b는 노드간 거리
            a, b = n
            # 0번부터 노드a까지의 거리가 지금가는 경로보다
            # 비용이 크다면 갱신
            if distance[a] > min_distance + b:
                distance[a] = min_distance + b
    #노드 N번까지 거리를 보는것이므로 distance(N)을 출력
    print('#{} {}'.format(t+1, distance[N]))
'''