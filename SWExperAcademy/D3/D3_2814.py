#D3 2814 최장경로

def dfs(idx, ans):
    global answer
    #탐색한 노드는 체크하고
    visited[idx] = 0
    #이동횟수 증가
    ans += 1
    #최댓값 갱신
    if answer < ans: answer = ans
    #이동가능 노드 확인
    for i in graph[idx]:
        #이동가능하면 이동
        if visited[i]: dfs(i, ans)
    #사용 해제
    visited[idx] = 1

for t in range(1, int(input()) + 1):
    #노드와 간선 정보를 받고
    N, M = map(int, input().split())
    #방문 배열 만들고
    visited = [1 for _ in range(N+1)]
    #입력받아서
    temp = [list(map(int, input().split())) for _ in range(M)]
    #쉽게 사용하기위한 데이터 편집하기
    graph = [[] for _ in range(N+1)]
    answer = 0
    #노드간 이동 경로 표시
    for a, b, in temp:
        graph[a].append(b)
        graph[b].append(a)
    #시작노드를 다르게해서 최대 길이 찾기
    for i in range(N): dfs(i, 0)
    print('#{} {}'.format(t, answer))