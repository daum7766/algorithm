#D4 1226 미로1
from collections import deque 

#이동리스트
move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    queue = deque()
    queue.append((1, 1))
    map_list[1][1] = 1
    while len(queue):
        y, x = queue.popleft()
        if map_list[y][x] == 3:
            return 1
        map_list[y][x] = 1
        for i in move_list:
            my = i[0] + y
            mx = i[1] + x
            if 0 <= my < N and 0 <= mx < N and map_list[my][mx] != 1:
                queue.append((my, mx))
    return 0


for _ in range(10):
    t = int(input())
    N = 16
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    #1,1 위치부터 탐색시작
    print('#{} {}'.format(t, bfs()))