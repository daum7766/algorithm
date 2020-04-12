# D3 5105 미로의 거리
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    global queue
    count = 0
    # 큐가 빌때까지 반복한다.
    # 세컨드 큐까지 비어있다면 이동을 못하는것이므로 0을 리턴하게 된다.
    while queue:
        seceond_queue = []
        #큐가 빌때까지 반복
        while queue:
            #x, y 좌표를 꺼내서
            y,x = queue.pop()
            #상 하 좌우로 이동해보자
            for i, j in move:
                dy = y+i
                dx = x+j
                #맵을 벗어나지 않는다면 체크
                if 0 <= dy < N and 0 <= dx < N:
                    #통로라면 지나왔다고 표시하고 큐에 추가
                    if not map_list[dy][dx]:
                        map_list[dy][dx] = 1
                        seceond_queue.append((dy, dx))
                    #도착지라면 현재까지 쌓인 카운트를 리턴
                    if map_list[dy][dx] == 3:
                        return count
        #큐가 빌때까지 반복되었다면 카운트를 늘려준다.
        count += 1
        #세컨큐를 기본큐에 넣어준다.
        queue = seceond_queue
    #여기까지 왔다면 통로는 찾을 수 없다.
    return 0

for t in range(1, 1+int(input())):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    queue = []
    for i in range(N):
        for j in range(N):
            #2를 찾는다면 큐에 넣고 브레이크
            if map_list[i][j] == 2:
                queue.append((i, j))
                break
        #esle는 브레이크에 걸리지 않았을때만 동작한다.
        #못찾았다면 위로 올린다.
        else: continue
        #2를 찾았다면 더이상의 반복문은 필요가 없으므로 정지
        break
    #결과값을 출력한다.
    print('#{} {}'.format(t, bfs()))