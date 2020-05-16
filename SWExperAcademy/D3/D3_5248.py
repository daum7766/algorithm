#D3 5248 그룹 나누기

def get_parent(x):
    if parent[x] != x: parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b: parent[a] = b
    else: parent[b] = a

for t in range(int(input())):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    votes = list(map(int, input().split()))
    for i in range(0, M*2, 2): union_parent(votes[i], votes[i+1])
    answer = set()
    for i in parent: answer.add(get_parent(i))
    print('#{} {}'.format(t+1, len(answer)-1))