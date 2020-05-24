# D5 1248 공통조상

# 자기 위의 노드가 누구누구 있는지 확인하는 함수
def find_parent(n, idx, count=0):
    # 트리를 돌면서 체크하자
    for i in tree[idx]:
        # i[1]이면 부모라는 뜻이다.
        if i[1]:
            # 부모노드를 찾았으니까 set에 추가하고
            parents[n].add(i[0])
            # 몇번째 만에 찾았는지 모르니까 순서도 저장하고
            order[n][i[0]] = count
            # 다시 돌린다.
            find_parent(n, i[0], count+1)

# 트리의 크기를 찾기위한 함수
def find_tree(n):
    global tree_size
    # 반복문 돌려보자
    for i in tree[n]:
        # 자식노드만 찾으면 되니까 i[0]이 0인거 찾는다.
        if not i[1]:
            # 찾았으면 트리사이즈 하나늘리고
            tree_size += 1
            # 다시 돌린다
            find_tree(i[0])


for t in range(int(input())):
    # 결과 출력용 변수
    # 시작하는 노드 포함이니까 1로 셋팅
    tree_size = 1
    my_parent = -1
    # 입력받고
    V, E, A, B = map(int, input().split())
    temp = list(map(int, input().split()))
    # 필요한 변수 만들어주고
    # 공통찾기용
    parents = {A:set(), B:set()}
    # 순서찾기용
    order = {A:{}, B:{}}

    # 그래프 리스트화
    tree = [[] for _ in range(V+1)]
    for i in range(0, len(temp), 2):
        a, b = temp[i], temp[i+1]
        tree[a].append((b, 0))
        tree[b].append((a, 1))
    # 자기 부모노드 찾고
    find_parent(A, A)
    find_parent(B, B)
    # 교집합으로 후보군 정리하고
    candidatekey = list(parents[A] & parents[B])
    distance = 999
    # 제일 가까운 조상 찾기
    for i in candidatekey:
        if order[A][i] < distance:
            distance = order[A][i]
            my_parent = i
    # 트리 크기 찾아주고
    find_tree(my_parent)
    #결과출력
    print('#{} {} {}'.format(t+1, my_parent, tree_size))