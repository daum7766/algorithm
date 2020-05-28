# D4 1251 하나로
# 크루스칼 알고리즘
from queue import PriorityQueue

def make_edge():
    for i in range(N):
        for j in range(i+1, N):
            d = ((islands_y[i]-islands_y[j])**2 + (islands_x[i]-islands_x[j])**2)**0.5
            distance.put((d, i, j))

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def unoion_parent(a, b):
    x = find_parent(a)
    y = find_parent(b)
    if x > y: parents[x] = y
    else: parents[y] = x


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
    parents = [i for i in range(N)]
    E = float(input())
    make_edge()
    while distance and count != N-1:
        d, a, b = distance.get()
        if find(a, b):
            answer += (d ** 2) * E
            count += 1
            unoion_parent(a, b)
    answer = int(answer+0.5)


    print('#{} {}'.format(t+1, answer))