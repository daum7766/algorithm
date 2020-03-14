#D3 1873 상호의 배틀필드

'''
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)
'''
move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

command_dict = {'U' : 0, 'D' : 1, 'L' : 2, 'R' : 3, 'S' :4,
'^' : 0, 'v' : 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2:'<', 3:'>'}

serch_list = ['<', '>', '^', 'v']

for t in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    map_list = [list(input()) for _ in range(H)]
    #탱크의 위치를 찾는다.
    for i in range(H):
        for j in range(W):
           if map_list[i][j] in serch_list:
                tank_pos = (i, j, command_dict[map_list[i][j]])
                break
        #브레이크에 안걸렸다면 진행한다.
        else: continue
        #브레이크가 걸렸다면 모든 반복문을 나온다.
        break
    #N값은 안쓰니까 버린다.
    input()
    #명령어 저장
    commands = input()
    #명령어를 순회하면서 처리
    for command in commands:
        temp = command_dict[command]
        #포탄 발싸라면
        if temp == 4:
            #탱크 위치에서 탱크가 바라보는 방향의 위치를 얻는다.
            dy = tank_pos[0] 
            dx = tank_pos[1]
            #포탄은 계속 전진한다.
            while True:
                dy += move_list[tank_pos[2]][0]
                dx +=move_list[tank_pos[2]][1]
                #포탄이 밖으로 벋어나거나 강철벽을 만나면 아무처리도 안한다.
                if 0 > dy or dy >= H or 0 > dx or dx >= W or map_list[dy][dx] == '#':
                    break
                #돌벽을 만나게 된다면
                if map_list[dy][dx] == '*':
                    #평지로 바꿔준다.
                    map_list[dy][dx] = '.'
                    break
        #이동 명령이라면
        else:
            y = tank_pos[0]
            x = tank_pos[1]
            dy = y + move_list[temp][0]
            dx = x + move_list[temp][1]
            map_list[y][x] = command_dict[temp]
            tank_pos = (y, x, temp)
            #맵 범위 안에있고 평지여야함.
            if 0 <= dy < H and 0 <= dx < W and map_list[dy][dx] == '.':
                #기존위치를 평지로 바꾸고
                map_list[y][x] = '.'
                #가야하는 위치에 탱크 표시
                map_list[dy][dx] = command_dict[temp]
                #탱크위치 갱신
                tank_pos = (dy, dx, temp)
    print('#{}'.format(t), end=' ')
    for m in map_list:
        print(''.join(m))
