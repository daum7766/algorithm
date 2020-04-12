#SW 역량테스트 2383 점심 식사시간
def Calculation(stair_list, stair):
    count, d_count = 0, 0
    delete_queue = []
    #이동중인사람이나 대기중인사람, 내려가는 사람이있다면 반복
    while stair_list or delete_queue or d_count:
        #대기하는 사람이 있다면
        while d_count:
            #최대인원이 다찼다면 정지
            if len(delete_queue) == 3:
                break
            #내려가는 사람들에게 넣어주기
            delete_queue.append(stair[2])
            #한명 넣을때마다 대기인원 감소
            d_count -= 1

        #내려가는 인원이 있을때 동작
        for i in range(len(delete_queue)-1, -1, -1):
            #시간을 감소시키고
            delete_queue[i] -= 1
            #전부 내려갔다면 뺀다
            if delete_queue[i] <= 0:
                delete_queue.pop(i)
        
        #이동중인 사람이 있다면
        for i in range(len(stair_list)-1, -1, -1):
            #거리를 감소키고
            stair_list[i] -= 1
            #계단까지 갔다면
            if stair_list[i] <= 0:
                #빼버리고 대기인원 증가
                stair_list.pop(i)
                d_count += 1
        #1초 증가
        count+=1
    return count

#조합찾기
def dfs(idx):
    #조합이 결정되었다면
    if idx == Num:
        global min_count
        stair_list1, stair_list2 = [], []
        #1번계단, 2번계단 분리하기
        for i in range(Num):
            if check[i]: stair_list1.append(Peoples[i][0])
            else : stair_list2.append(Peoples[i][1])
        #시간계산하기, 두계단중 가장 긴시간을 가져온다.
        count = max(Calculation(sorted(stair_list1), Stairs[0]), Calculation(sorted(stair_list2), Stairs[1]))
        #제일 작은 시간으로 교체
        min_count = min(count, min_count)
        return
    check[idx] = False
    dfs(idx+1)
    check[idx] = True
    dfs(idx+1)
    

T = int(input())
for t in range(1, T+1):
    N = int(input())
    #지도 표시
    map_list = [list(map(int, input().split())) for _ in range(N)]
    #사람위치, 계단위치, 계단값
    Peoples, Stairs = [], []
    #사람수, 리턴할 시간
    Num, min_count = 0, 987654321
    for i in range(N):
        for j in range(N):
            temp_num = map_list[i][j]
            if temp_num:
                #사람이면 사람수추가하고 위치추가
                if temp_num == 1:
                    Num += 1
                    Peoples.append([i, j])
                #계단이라면 계단위치 추가하고 계단길이 추가
                else:
                    Stairs.append([i, j, temp_num])
    #사람의 계단마다 거리계산
    for i in range(len(Peoples)):
        distance1 = abs(Peoples[i][0] - Stairs[0][0]) + abs(Peoples[i][1] - Stairs[0][1])
        distance2 = abs(Peoples[i][0] - Stairs[1][0]) + abs(Peoples[i][1] - Stairs[1][1])
        Peoples[i][0] = distance1
        Peoples[i][1] = distance2
    #1번 계단으로 갈것인지, 2번계단으로 갈것인지
    check = [False for _ in range(Num)]
    #모든 경우의수 찾으러 가자
    dfs(0)
    print('#{} {}'.format(t, min_count+1))