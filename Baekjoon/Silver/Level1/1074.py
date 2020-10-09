# Silver 1 Z

def dfs(start_y, start_x, size):
    global count
    m_size = size // 2
    if size <= 2:
        for i in range(start_y, start_y + size):
            for j in range(start_x, start_x + size):
                if i == r and j == c:
                    return count
                count += 1
    if start_y <= r < start_y + m_size and start_x <= c < start_x + m_size:
        dfs(start_y, start_x, m_size)
    elif start_y <= r < start_y + m_size and start_x + m_size <= c < start_x + size:
        count += m_size ** 2
        dfs(start_y, start_x + m_size, m_size)
    elif start_y + m_size <= r < start_y + size and start_x <= c < start_x + m_size:
        count += (m_size ** 2) * 2
        dfs(start_y + m_size, start_x, m_size)
    else :
        count += (m_size ** 2) * 3
        dfs(start_y + m_size, start_x + m_size, m_size)

N, r, c = map(int, input().split())
size = 2 ** N
count = 0
check = False
dfs(0, 0, size)
print(count)