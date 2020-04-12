# D3 1220 Magnetic
T = 10
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for j in range(N):
        temp_stack = []
        check = False
        #아래부터 위로 진행하면서 찾는다.
        for i in range(N):
            if map_list[i][j] == 1:
                temp_stack.append(1)
            if map_list[i][j] == 2 and temp_stack:
                temp_stack.clear()
                count += 1

    print("#{} {}".format(t, count)) 