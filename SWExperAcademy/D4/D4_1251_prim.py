# D4 1251 하나로
# 프림 알고리즘
import heapq
INF = float('inf')

# 가능한 간선의 종류를 만들어주는 함수
def make_edge():
    for i in range(N):
        for j in range(i+1, N):
            # 거리를 계산한다. √( (x1 - x2)^2 + (y1 - y2)^2 )
            d = ((islands_y[i]-islands_y[j])**2 + (islands_x[i]-islands_x[j])**2)*E
            # 거리를 기준으로 정렬할꺼기 때문에 거리를 제일앞에두고 어디에서 어디로 가는지 표시
            distance[i][j] = distance[j][i] = d

def prim():
    answer = 0
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        d, idx = heapq.heappop(pq)
        if visited[idx]: continue
        visited[idx] = 1
        answer += d
        for i in range(N):
            if not visited[i] and key[i] > distance[idx][i]:
                key[i] = distance[idx][i]
                parents[i] = idx
                heapq.heappush(pq, (key[i], i))
    return answer


for t in range(int(input())):
    answer = 0
    # 입력받기
    N = int(input())
    islands_y = list(map(int, input().split()))
    islands_x = list(map(int, input().split()))
    distance = [[0]*N for _ in range(N)]
    E = float(input())
    # 부모의 정보를 저장하는 변수
    parents = list(range(N))
    pq = []
    key = [INF] * N
    visited = [0] * N
    # 모든 간선 정보를 만들어주고
    make_edge()
    
    answer = int(prim()+0.5)
    print('#{} {}'.format(t+1, answer))