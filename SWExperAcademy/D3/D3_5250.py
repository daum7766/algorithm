#D3 5250 최소 비용
from collections import deque
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for t in range(int(input())):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    #도착까지 드는 비용 표시
    distance = [[INF for _ in range(N)] for _ in range(N)]
    #처음 부분은 0으로 초기화
    distance[0][0] = 0
    #앞쪽부터 꺼낼꺼니까 디큐사용
    queue = deque()
    #시작점은 0,0
    queue.append((0, 0))
    #큐가 빌대까지 반복
    while queue:
        #좌표 꺼내고
        y, x = queue.popleft()
        #이동할 방향 선택해서
        for dy, dx in move:
            #이동해 봤을때
            my, mx = dy+y, dx+x
            #표에 벗어나지 않는다면
            if 0 <= my < N and 0 <= mx < N:
                #기본 이동비용1
                temp = 1
                #높이차만큼 추가해주고
                if map_list[my][mx] > map_list[y][x]:
                    temp += map_list[my][mx] - map_list[y][x]
                #거리 갱신해주고 큐에 추가
                if distance[my][mx] > distance[y][x] + temp:
                    distance[my][mx] = distance[y][x] + temp
                    queue.append((my, mx))
    #도착점까지의 거리 출력
    print('#{} {}'.format(t+1, distance[N-1][N-1]))