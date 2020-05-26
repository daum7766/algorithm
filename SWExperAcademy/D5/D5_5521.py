# D5 5521 상원이의 생일파티
from collections import deque

# bfs를 이용하여 탐색
def bfs(queue):
    global answer
    # 큐가 빌대까지
    while len(queue):
        # 탐색할 인덱스와 깊이
        idx, depth = queue.popleft()
        # 탐색 시작
        for i in tree[idx]:
            # 아직 초대장을 안줬다면
            if visited[i]:
                # 초대장 챙겨주고
                visited[i] = 0
                answer += 1
                # 친한친구의 친구인지 확인
                # 친한친구의 친구까지니까 깊이를 한단계만 갈수있도록 설정
                if depth < 1:
                    queue.append((i, depth+1))


for t in range(int(input())):
    answer = 0
    # 입력받고
    N, M = map(int, input().split())
    # 트리는 연결리스트로 표현하고
    tree = [[] for _ in range(N+1)]
    # 방문체크용도 만들어 주고
    visited = [1] * (N+1)
    # 트리 연결도 해주고
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    # 앞에서 부터 꺼낼꺼니까 디큐 사용
    queue = deque()
    # 1번이 상원이니까 1번이랑 깊이 0으로 추가
    queue.append((1, 0))
    # 사용했다고 표시하고
    visited[1] = 0
    # 탐색시작
    bfs(queue)
    # 결과값 출력
    print('#{} {}'.format(t+1 , answer))