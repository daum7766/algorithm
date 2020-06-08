# D4 1249 보급로
import heapq

# 상하좌우 이동계산용
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 다익스트라 알고리즘 계산 함수
def dijkstra(queue):
    # 큐가 빌때까지 반복
    while queue:
        # 좌표를 꺼내서
        d, y, x = heapq.heappop(queue)
        # 상하좌우로 이동해보고
        for dy, dx in move:
            my, mx = y+dy, x+dx
            # 이동할 수 있다면
            if 0 <= my < N and 0 <= mx < N:
                # 거리(비용) 비교를 해본다. 갱신이 가능하다면 갱신하고 큐에추가
                temp = d + field[my][mx]
                if distance[my][mx] > temp:
                    distance[my][mx] = temp
                    if my == N-1 and mx == N-1:
                        return
                    heapq.heappush(queue, (temp, my, mx))

for t in range(int(input())):
    # 필드 크기
    N = int(input())
    # 필드 입력
    field = [list(map(int, list(input()))) for _ in range(N)]
    # 초기 거리는 무한대로 놓는다.
    INF = float('inf')
    distance = [[ INF for _ in range(N)] for _ in range(N)]
    # 처음 시작부분은 0으로 설정
    distance[0][0] = 0
    # 디큐만들고 처음좌표를 넣어준다.
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    # 알고리즘 돌려서 거리를 계산한다.
    dijkstra(queue)
    # 결과출력
    print('#{} {}'.format(t+1, distance[N-1][N-1]))