#5648 모의역량테스트 원자소멸 시뮬레이션
position_list = [[0 for _ in range(4001)] for _ in range(4001)]
T = int(input())
for t in range(1, T+1):
    #상 하 좌 우
    move_list = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    atom_list = []
    length = int(input())
    remove_list = set()
    energy_sum = 0
    
    #위치보정
    #0.5구간이 생길수있어서 2배로 늘려준다.
    #인덱스 접근을 위해 양수로 보정한다.
    for _ in range(length):
        x, y, move , energy = map(int, input().split())
        y = (y+1000)*2
        x = (x+1000)*2
        atom_list.append([y, x, move, energy])
        position_list[y][x] += 1
        pop_list = []
#모든원소가 사라질때까지 반복한다.
    while atom_list:
        for i in range(len(atom_list)):
            y, x, move, energy = atom_list[i]
            move_y = y + move_list[move][0]
            move_x = x + move_list[move][1]
            #배열밖으로 벗어난다면 없애버리기
            if move_x < 0 or move_x > 4000 or move_y < 0 or move_y > 4000:
                pop_list.append(i)
                continue
            #현재위치에서 삭제하고
            position_list[y][x] -= 1
            #다음위치로이동
            position_list[move_y][move_x] += 1
            #위치 표시해주기
            atom_list[i][0], atom_list[i][1] = move_y, move_x
        #위치를 벗어났다면 리스트에서 제거
        if pop_list:
            for _ in range(len(pop_list)):
                index = pop_list.pop()
                t_y, t_x =  atom_list[index][0], atom_list[index][1]
                position_list[t_y][t_x] -=1
                atom_list.pop(index)
        
        #리스트를 돌면서 원소가 2개이상인곳 찾기
        for i in atom_list:
            y, x = i[0], i[1]
            if position_list[y][x] > 1:
                remove_list.add((y,x))
        #원소가 충돌던위치와 같은 원소를찾아 에너지 더해주기
        if remove_list:
            for y, x in remove_list:
                for i in range(len(atom_list)-1, -1, -1):
                    t_y, t_x, t_e = atom_list[i][0], atom_list[i][1], atom_list[i][3]
                    if t_y == y and t_x == x:
                        position_list[t_y][t_x] -=1
                        energy_sum += t_e
                        atom_list.pop(i)
            remove_list.clear()

    print("#{} {}".format(t, energy_sum))