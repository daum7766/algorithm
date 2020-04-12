#D4 1211 Ladder2

T = 10
for t in range(T):
    test = int(input())
    #100번돌면서 데이터를 받는다.
    ladder = [list(map(int, input().split())) for _ in range(100)]
    #사다리 길이중 제일 적은길이 저장용
    min_count = 10000
    #제일짧은 사다리의 위치를 저장
    return_x = 0
    #제일뒤부터 앞까지 1인위치를 찾아 저장한다.
    #그냥 range(100)으로 넣어도 상관이없다. 그냥 뒤로했다.
    start_list = [i for i in range(99, -1, -1) if ladder[0][i]]
    #시작할수있는 포인트만큼 반복
    for start in start_list:
        #이동을 위해 좌표셋팅
        #제일 위에서부터 시작하므로 y좌표는 0이다.
        d_y = 0
        #x좌표는 1인곳에서 시작해야하고 그것은 start에 들어있다.
        d_x = start
        #현재 사다리의 이동칸수를 저장하기 위한 변수
        count = 0
        #좌우이동을 방지하기 위한 변수이다.
        move = 0
        #y축이 99가 될때까지 반복한다.
        #99라면 제일 밑이므로 더이상 계산할 필요가 없다.
        down = 0
        left = 1
        right = 2
        while d_y < 99:
            #밑으로 내려갔거나 왼쪽으로 이동했었다면
            #왼쪽으로 갈때 벽이 아닌지 확인하고
            #벽이 아니라면 1인지 체크한다.
            if (move == down or move == left) and d_x > 0 and ladder[d_y][d_x-1]:
                #위의 조건을 통과했다면 왼쪽으로 이동후
                #이동했던 행동을 left로 기록한다.
                d_x -= 1
                move = left
            #밑으로 내려갔거나 오른쪽으로 이동했었다면
            #오른쪽으로 갈때 벽이 아닌지 확인하고
            #벽이 아니라면 1인지 체크한다.
            elif (move == down or move == right) and d_x < 99 and ladder[d_y][d_x+1]:
                #위의 조건을 통과했다면 오른쪽으로 이동후
                #이동했던 행동을 right로 기록한다.
                d_x += 1
                move = right
            #왼쪽도 오른쪽도 못간다면 아래로 내려간다.
            #내려갈수있는지 체크했지만 그냥 else로 적어도 무방하다.
            elif ladder[d_y + 1][d_x]:
                #아래로 이동하고 행동을 down으로 바꾼다.
                d_y += 1
                move = down
            #이동을 할때마다 count를 기록해준다.
            count +=1
            #이동행동을 체크하는 이유는
            #오른쪽으로 이동후 왼쪽과 오른쪽이 1인경우가 생긴다.
            #그때 무한루프에 빠질수있으므로 단방향으로 이동하기위해 사용한다.
        #끝까지 내려왔다면 이동했던 count를 현재 최소카운트와 비교한다.
        if min_count > count: 
            #현재 거리가 더짧다면 count를 갱신한다.
            min_count = count
            #출발했던 좌표또한 기록한다.
            return_x = start
    #모두 반복하여 여기까지 왔다면 결과를 출력한다.
    print("#{} {}".format(test, return_x))