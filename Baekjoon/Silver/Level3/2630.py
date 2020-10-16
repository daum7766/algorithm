# Silver 3 색종이 만들기
from sys import stdin

def dfs(y, x, size):
    color = maps[y][x]
    m_size = size // 2
    for i in range(y, y+size):
        for j in range(x, x+size):
            if maps[i][j] != color:
                dfs(y, x, m_size)
                dfs(y, x + m_size, m_size)
                dfs(y + m_size, x, m_size)
                dfs(y + m_size, x + m_size, m_size)
                return
    answer[color] += 1


N = int(stdin.readline())
# 하얀색, 파란색
answer = [0, 0]
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]

dfs(0, 0, N)
print('{}\n{}'.format(answer[0], answer[1]))