#D4 5249 최소 신장 트리

#부모가 누구인자 가져오는 함수
def get_parent(x):
    if parent[x] != x: parent[x] = get_parent(parent[x])
    return parent[x]

#부모를 병합하는 함수
def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b: parent[a] = b
    else: parent[b] = a

#부모가 같은지 비교하는 함수
def find(x, y):
    return get_parent(x) == get_parent(y)


for t in range(int(input())):
    answer = 0
    V, E = map(int, input().split())
    #부모가 누구인지 저장하는 변수
    parent = [i for i in range(V+1)]
    #연결된 노드와 가중치를 저장하는 변수
    edge = [list(map(int, input().split())) for _ in range(E)]
    #가중치를 기준으로 정렬(뒤에서 꺼내야 비용이 적으므로 내림차순 정렬)
    edge.sort(key=lambda x: -x[2])
    #간선이 빌때까지 반복
    while edge:
        #데이터 꺼내서
        a, b, v = edge.pop()
        #부모가 다른경우만(싸이클이 안생기는 경우)
        if not find(a,b):
            #부모를 병합한다.
            union_parent(a, b)
            #정답에 값을 더한다.
            answer += v

    print('#{} {}'.format(t+1, answer))