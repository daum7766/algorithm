#D5 1247 최적경로
def dfs(index, lastX, lastY, distance):
    global min_count
    if min_count < distance:
        return
    #모든경로 탐색이 완료되었다면
    if index == length:
        #거리를 계산한다.
        distance += abs(lastX - home_position[0]) + abs(lastY - home_position[1])
        #제일짧은거리 리턴
        min_count = min(distance, min_count)
        return
    #경로를 하나씩 추가한다.
    for i in range(length):
        #탐색하지 않았다면
        if check[i]:
            #사용했다고 체크하기
            check[i] = False
            #재귀하기
            temp = distance + abs(lastX - position_list[i][0]) + abs(lastY - position_list[i][1])
            dfs(index+1, position_list[i][0], position_list[i][1], temp)
            #돌아오면 사용체크 해제
            check[i] = True


T = int(input())
for t in range(1, T+1):
    #위치 입력받기
    length = int(input())
    #좌표값을 받는 임시리스트
    temp_list = list(map(int, input().split()))
    #각각의 위치를 저장하는 리스트
    position_list = []
    #방문여부 체크리스트
    check = [True for _ in range(length)]
    #최소값 카운트용
    min_count = 1000

    company_position = []
    home_position = []
    #각사람의 위치더하기
    for i in range(0, len(temp_list), 2):
        position_list.append([temp_list[i], temp_list[i+1]])
    company_position = position_list.pop(0)
    home_position = position_list.pop(0)
    #경로찾기 시작
    dfs(0, company_position[0], company_position[1], 0)
    print("#{} {}".format(t, min_count))
    