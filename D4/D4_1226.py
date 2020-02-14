#D4 1226 미로1

#이동리스트
move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(y, x):
    global result
    #현재 위치가 도착점이라면
    #목표점에 도달했거나 결과가 이미나와있다면 리턴
    if map_list[y][x] == 3 or result:
        result = 1
        return
    for i, j in move_list:
        d_y = y + i
        d_x = x + j
        #반복하다가 결과가 나왔다면 리턴
        if result: 
            return
        #벽이아니거나 왔던 위치가 아니라면
        if map_list[d_y][d_x] != 1 :
            #현재위치를 벽으로 체크하고 재귀
            map_list[y][x] = 1
            dfs(d_y, d_x)
        

T = 10
for _ in range(T):
    t = int(input())
    N = 16
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    result = 0
    #1,1 위치부터 탐색시작
    dfs(1,1)
    print('#{} {}'.format(t, result))