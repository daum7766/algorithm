#4875 D2 미로

move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#바운더리 체크
def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False

T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    y, x = 0, 0
    result = 0
    #2가 있는 위치찾기
    for i in range(N):
        if 2 in map_list[i]:
            x = map_list[i].index(2)
            y = i
            break
    #스택에 시작위치 넣어주기
    stack = [(y, x)]
    #스택이 빌때까지 반복한다.
    while stack:
        temp_list = []
        #스택에 있는값을 꺼내서
        y, x = stack.pop()
        #현재위치는 갔다고 변경
        map_list[y][x] = 1
        #이동할 4방향을 검사한다.
        for _y, _x in move_list:
            dy = y + _y
            dx = x + _x
            #가는길이 바운더리 벗어나면 다음길로
            if iswall(dy, dx):
                continue
            #가는곳이 3이면 도착지점
            if map_list[dy][dx] == 3:
                #결과변경후 반복문 종료
                result = 1
                break
            #0이라면 갈수있는 장소를 스택에 추가
            elif not map_list[dy][dx]:
                stack.append((dy, dx))
        else:
            #브레이크 없이 끝났다면 다음것으로 진행
            continue
        #브레이크 문으로 여기까지 왔다면 반복 멈추기
        break
    #결과출력
    print('#{} {}'.format(t, result))
