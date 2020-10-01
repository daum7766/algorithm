import copy
# gold 3 청소년 상어
def dfs(fishs, shark_y, shark_x, _sum):
    global answer
    # 물고기 위치조정
    fish_move(fishs)
    # 상어 위치 구하기
    # 상어 이동방향 구하기
    move_index = fishs[shark_y][shark_x][1]
    # 상어 이동 계산
    dy, dx = move[move_index]
    move_y, move_x = shark_y, shark_x
    # 가능한지 시도해보기
    # for _ in range(3):
    while 1:
        move_y, move_x = move_y + dy, move_x + dx
        # 이동이 가능하다면
        if 0 <= move_y < 4 and 0 <= move_x < 4 :
            if fishs[move_y][move_x][1] == 0:
                continue
            temp = copy.deepcopy(fishs)
            # 물고기 잡아먹고 방향변경하기
            point, direction = temp[move_y][move_x]
            temp[move_y][move_x] = (-1, direction)
            # 기존 상어위치는 빈공간으로 변경
            temp[shark_y][shark_x] = (point, 0)
            # dfs 호출하기
            dfs(temp, move_y, move_x, _sum + point)
        else:
            break
    answer = max(answer, _sum)



def fish_move(fishs):
    fish_pos = {}
    for i in range(4):
        for j in range(4):
            fish_pos[fishs[i][j][0]] = (i, j)
    
    fish_value = sorted(fish_pos.keys())
    for value in fish_value:
        i, j = fish_pos[value]
        # 상어이거나 비어있는 공간이라면 패스
        if fishs[i][j][0] == -1 or fishs[i][j][1] == 0:
            continue
        while 1:
            # 이동한 인덱스 추출
            move_index = fishs[i][j][1]
            # 이동경로 계산하기
            dy, dx = move[move_index]
            # 가능한지 시도해보기
            move_y, move_x = i + dy, j + dx
            # 이동이 가능하다면(벗어나지 않고, 상어도 아니어야 함)
            if 0 <= move_y < 4 and 0 <= move_x < 4 and fishs[move_y][move_x][0] != -1:
                fish_pos[value] = (move_y, move_x)
                fish_pos[fishs[move_y][move_x][0]] = (i, j)
                fishs[i][j], fishs[move_y][move_x] = fishs[move_y][move_x], fishs[i][j]
                break
            else:
                # 다르다면 다시 계산 반회전
                move_index += 1
                if move_index > 8:
                    move_index -= 8
                fishs[i][j] = (fishs[i][j][0], move_index)


move = [(0, 0), (-1, 0), (-1 ,-1), (0 , -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

fishs_list = []

for _ in range(4):
    user_input = list(map(int, input().split()))
    temp = []
    for i in range(0, 8, 2):
        temp.append((user_input[i], user_input[i+1]))
    fishs_list.append(temp)

answer = fishs_list[0][0][0]
fishs_list[0][0] = (-1, fishs_list[0][0][1])

dfs(fishs_list, 0, 0, answer)
print(answer)