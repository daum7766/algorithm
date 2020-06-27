# Silver LV3 오목

move_list = [(0, 1), (1, 0), (1, 1), (-1, 1)]

# 벽체크
def is_wall(x1, y1):
    if x1 < 0 or y1 < 0 or x1 >= N or y1 >= N:
        return True
    return False

def check(i, j):
    k = map_list[i][j]
    for y, x in move_list:
        count = 1
        d_y = i
        d_x = j
        while True:
            d_x += x
            d_y += y
            if is_wall(d_x, d_y):
                break
            if map_list[d_y][d_x] != k:
                break
            count+=1
        if count == 5:
            d_y = i - y
            d_x = j - x
            if is_wall(d_x, d_y) or map_list[d_y][d_x] != k:
                return True, k

    return False, 0

N = 19
map_list = [list(map(int, input().split())) for _ in range(N)]
is_end = False
result = 0
for i in range(N):
    for j in range(N):
        if map_list[i][j]:
            is_end, result = check(i,j)
            if is_end:
                break
    if is_end:
        break
        
print(result)
if is_end:
    print('{} {}'.format(i+1, j+1))