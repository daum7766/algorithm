#D4 5249 최소 신장 트리

def get_parent(x):
    if parent[x] != x: parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b: parent[a] = b
    else: parent[b] = a

def find(x, y):
    return get_parent(x) == get_parent(y)

for t in range(int(input())):
    answer = 0
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x: -x[2])
    while edge:
        a, b, v = edge.pop()
        if not find(a,b):
            union_parent(a, b)
            answer += v

    print('#{} {}'.format(t+1, answer))