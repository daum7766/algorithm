#5648 모의역량테스트 원자소멸 시뮬레이션

T = int(input())
for t in range(1, T+1):
    position_list = [[0 for _ in range(4001)] for _ in range(4001)]
    #상 하 좌 우
    move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    atom_list = []
    length = int(input)
    remove_list = set()
    result_energy = 0
    
    #위치보정
    #0.5구간이 생길수있어서 2배로 늘려준다.
    #인덱스 접근을 위해 양수로 보정한다.
    for _ in range(length):
        y, x, move , energy = map(int, input().split())
        y = (y+1000)*2
        x = (x+1000)*2
        atom_list.append([y, x, move, energy])
        position_list[y][x] += 1

    while atom_list:
        if remove_list:
            remove_list.sort()
            remove_num = []
            for y, x in remove_list:
                for _ in range(len(remove_list))



        for i in range(len(atom_list)):
            y, x, move, energy = atom_list[i]
            move_y = y + move_list[move][0]
            move_x = x + move_list[move][1]
            if move_x < 0 or move_x > 4000 or move_y < 0 or move_y > 4000:
                remove_list.add([y, x])
                continue
            position_list[y][x] -= 1
            if position_list[move_y][move_x]:
                remove_list.add([move_y,move_x])
            position_list[move_y][move_x] += 1

