# silver 2 유기농 배추
from collections import deque

move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

queue = deque()

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    maps = [[0 for _ in range(N)] for _ in range(M)]
    answer = 0
    for _ in range(K):
        y, x = map(int, input().split())
        maps[y][x] = 1
    
    for i in range(M):
        for j in range(N):
            if maps[i][j] == 1:
                maps[i][j] = 0
                queue.append((i, j))
                while len(queue):
                    y, x = queue.popleft()
                    for dy, dx in move:
                        move_y, move_x = y + dy, x + dx
                        if 0 <= move_y < M and 0 <= move_x < N and maps[move_y][move_x] == 1:
                            maps[move_y][move_x] = 0
                            queue.append((move_y, move_x))
                answer += 1
    print(answer)