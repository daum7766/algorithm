# Gold 3 17472 다리만들기2

#상 하 좌 우
move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#섬정보를 변경한다.
def change_number(y, x, idx):
    for dy, dx in move_list:
        d_y, d_x = y+dy, x+dx
        if d_y < 0 or d_x < 0 or d_y >= row or d_x >= col:
            continue
        if island_map[d_y][d_x] == 0:
            continue
        if island_map[d_y][d_x] == 1:
            island_map[d_y][d_x] = idx
            change_number(d_y, d_x, idx)

#간선의 정보를 가져온다.
def find_edge(y, x, idx):
    for dy, dx in move_list:
        d_y, d_x = y+dy, x+dx
        count = 0
        while True:
            #밖으로 벗어나면 취소
            if d_y < 0 or d_x < 0 or d_y >= row or d_x >= col:  break
            #자기자신과 만나면 취소
            if island_map[d_y][d_x] == idx: break
            #진행방향이 바다라면 한번더 진행하고 거리 count
            if island_map[d_y][d_x] == 0:
                d_y += dy
                d_x += dx
                count += 1
                continue
            #그외의 경우이다.

            #길이가 2 이하라면 취소
            if count < 2: break
            #그게 아니라면 거리 추가하기
            num = island_map[d_y][d_x]
            cost = distances[idx-2][num-2]
            if cost == 0:  distances[idx-2][num-2] = count
            else: distances[idx-2][num-2] = min(cost, count)
            break

#부모의 정보를 가져온다.
def getParent(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = getParent(parent[idx])
    return parent[idx]

#부모를 병합한다. 작은 부모에게 병합
def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

#부모가 같은지 확인한다.
def find(a, b):
    a = getParent(a)
    b = getParent(b)
    return a == b


#가로세로 크기입력받기
row , col = map(int, input().split())
#부모노드 확인용
parent = [i for i in range(6)]
#각 이동 거리에 대한 배열
distances = [[0 for j in range(6)] for i in range(6)]
#노드 연결 비용
costs = []
#최단거리
answer = 0

#섬정보 저장
island_map = []
for i in range(row):
    island_map.append(list(map(int, input().split())))

number = 2

#섬정보 바꾸기
for i in range(row):
    for j in range(col):
        if island_map[i][j] == 1:
            island_map[i][j] = number
            change_number(i, j, number)
            number += 1

#섬과 연결되있는 부분 찾기
for i in range(row):
    for j in range(col):
        if island_map[i][j]:
            find_edge(i, j, island_map[i][j])

#관리하기 쉽도록 데이터 구조 편집
for i in range(6):
    for j in range(6):
        if distances[i][j] and [j, i, distances[i][j]] not in costs:
            costs.append([i, j, distances[i][j]])

#거리를 기준으로 정렬한다.
costs = sorted(costs, key = lambda x : x[2])

#거리계산하고 부모노드 병합하기
for cost in costs:
    if not find(cost[0], cost[1]):
        answer += cost[2]
        unionParent(cost[0], cost[1])

#모든섬이 연결되었나 확인한다.
for i in range(number-2):
    #하나라도 연결이 되어있지 않다면 -1로 바꾼다
    if getParent(i) != 0:
        answer = -1
        break

print(answer)