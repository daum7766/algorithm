#D4 1861 정사각형 방

#상 하 좌 우
move_list = [(-1,0), (1, 0), (0, -1), (0, 1)]

#이동가능 카운트 세는함수
def check(i, j):
    x, y = j, i
    count = 0
    while True:
        #상하좌우로 이동해본다.
        for dy, dx in move_list:
            #이동이 불가능하다면 다른걸로 넘어간다.
            if y+dy <0 or x + dx <0 or y+dy >=N or x + dx >= N:
                continue
            #이동이 가능하다면 이동위치를 임시변수에 담고
            t_y = y+dy
            t_x = x+dx
            #이동위치가 현재보다 1큰지 비교한다.
            if map_list[t_y][t_x] == map_list[y][x]+1:
                #이동가능하면 count를 증가하고 현재위치 변경
                count += 1
                y = t_y
                x = t_x
                break
        else:
            #4방향을 갈동안 break가 안걸렸다면 이동이 불가능함.
            break
        #지금까지 누적된 count 리턴
    return count

T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split()))for _ in range(N)]
    minnum = 0
    max_count = 0
    for i in range(N):
        for j in range(N):
            #현재 좌표에서 이동가능한 거리계산
            count = check(i,j)
            #지금까지 이동거리가 최대이동거리보다 크다면
            if count > max_count:
                #이동거리 갱신
                max_count = count
                #방의 값을 넣어준다.
                minnum = map_list[i][j]
                #카운트가 같다면
            if count == max_count:
                #숫자가 작은걸 넣어준다.
                minnum = min(minnum, map_list[i][j])

    print("#{} {} {}".format(t, minnum, max_count+1))