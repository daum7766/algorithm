# D4 1251 하나로
# 크루스칼 알고리즘
from queue import PriorityQueue

# 가능한 간선의 종류를 만들어주는 함수
def make_edge():
    for i in range(N):
        for j in range(i+1, N):
            # 거리를 계산한다. √( (x1 - x2)^2 + (y1 - y2)^2 )
            d = ((islands_y[i]-islands_y[j])**2 + (islands_x[i]-islands_x[j])**2)**0.5
            # 거리를 기준으로 정렬할꺼기 때문에 거리를 제일앞에두고 어디에서 어디로 가는지 표시
            distance.put((d, i, j))

# 부모를 찾는 함수
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

# 부모를 병합해주는 함수
def unoion_parent(a, b):
    x = find_parent(a)
    y = find_parent(b)
    # 번호가 작은쪽으로 병합된다.
    if x > y: parents[x] = y
    else: parents[y] = x

# 부모가 같은지 확인하는 함수 -> 싸이클 확인
def find(a, b):
    x = find_parent(a)
    y = find_parent(b)
    return x != y


for t in range(int(input())):
    answer = 0
    count = 0
    N = int(input())
    islands_y = list(map(int, input().split()))
    islands_x = list(map(int, input().split()))
    distance = PriorityQueue()
    # 부모의 정보를 저장하는 변수
    parents = [i for i in range(N)]
    E = float(input())
    # 모든 간선정보를 만들어주고
    make_edge()
    # 간선을 하나씩 꺼내며 체크, 간선의 최대개수는 N-1개이므로 끝나기전에 달성하면 종료
    while distance and count != N-1:
        # 정보를 꺼내서
        d, a, b = distance.get()
        # 부모가 다르다면
        if find(a, b):
            # 비용을 저장하고
            answer += (d ** 2) * E
            # 선택한 간선개수 증가하고
            count += 1
            # 부모를 병합
            unoion_parent(a, b)
    # 반올림 처리는 0.5를 더하고 정수로 변환하면 된다.
    answer = int(answer+0.5)


    print('#{} {}'.format(t+1, answer))