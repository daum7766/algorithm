#D2 5178 노드의 합
def dfs(idx):
    #만약 인덱스 범위를 벗어난다면 0을 리턴
    if idx > N + 1: return 0
    #값이 있다면 값을 리턴
    if Tree[idx]: return Tree[idx]
    #왼쪽 자식노드 위치찾기
    left = idx*2
    #오른쪽 자식노드 위치찾기
    right = left+1
    #재귀를 이용하여 구하기
    Tree[idx] = dfs(left) + dfs(right)
    #결과값 리턴
    return Tree[idx]


for t in range(int(input())):
    #별도 노드개수, 리프노드의 개수, 출력노드번호
    N, M, L = map(int, input().split())
    #누적합을 적어둔 리스트
    Tree = [0 for _ in range(N+2)]
    #입력값을 받아 노드의 값을 수정한다.
    for i in range(M):
        node, value = map(int, input().split())
        Tree[node] = value
    #재귀를 이용하여 계산시작
    result = dfs(L)
    #결과값 출력ㄴ
    print('#{} {}'.format(t+1, result))