#SW 역량테스트 2383 점심 식사시간

def Calculation(stair_list, stair):
    count = 0
    return count

def What_tiem(stair_list1, stair_list2):
    wait_list1 = []
    wait_list2 = []
    for y, x in stair_list1:
        distance = abs(y - Stairs[0][0]) + abs(x - Stairs[0][1])
        wait_list1.append(distance)
    for y, x in stair_list2:
        distance = abs(y - Stairs[1][0]) + abs(x - Stairs[1][1])
        wait_list2.append(distance)
    wait_list1.sort()
    wait_list2.sort()
    count = [0, 0]
    count[0] = Calculation(stair_list1, Stairs[0])
    count[1] = Calculation(stair_list2, Stairs[1])
    return min(count)
    

#조합찾기
def dfs(idx):
    if idx == N:
        stair_list1 = []
        stair_list2 = []
        for i in range(Num):
            if check[i]: stair_list1.append(Peoples[i])
            else : stair_list2.append(Peoples[i])
            count = What_tiem(stair_list1, stair_list2)
            min_count = min(count, min_count)
    check[idx] = False
    dfs(idx+1)
    check[idx] = True
    dfs(idx+1)
    

T = int(input())
for t in range(1, T+1):
    N = int(input)
    #지도 표시
    map_list = [list(map(int, input().split())) for _ in range(N)]
    #사람수
    Num = 0
    #사람위치
    Peoples = []
    #계단위치, 계단값
    Stairs = []
    #리턴할 시간
    min_count = 987654321
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
    #1번 계단으로 갈것인지, 2번계단으로 갈것인지
    check = [False for _ in range(Num)]
    #모든 경우의수 찾으러 가자
    dfs(0)
    print('#{} {}'.format(t, min_count))