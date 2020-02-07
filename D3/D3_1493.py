#D3 1493 수의 새로운 연산

num = 400
#인덱스 0~399까지 첫줄의 데이터를 구한다.
position_list = [0 for _ in range(num)]
for i in range(1, num-1):
    position_list[i] = position_list[i-1] + i

T = int(input())
for t in range(1, T+1):
    #pq값을 받아온다.
    p, q = map(int ,input().split())
    position = [[], []]
    #반복을 돌면서 자신보다 같거나 큰값을 찾아 좌표를 계산한다.
    for i in range(1, len(position_list)):
        if not position[0] and p <= position_list[i]:
            gab_p = position_list[i] - p
            position[0] = [1 + gab_p, i - gab_p]
        if not position[1] and q <= position_list[i]:
            gab_q = position_list[i] - q
            position[1] = [1 + gab_q, i - gab_q]
        if position[0] and position[1]:
            break
    #계산된 자표를 더한다.
    y = position[0][0] + position[1][0]
    x = position[0][1] + position[1][1]
    add_num = 0
    #찾는 위치의 갭만큼 계산한다.
    for i in range(y-1):
        add_num += x + i
    #계산한 데이터를 합하여 출력
    print('#{} {}'.format(t, position_list[x] + add_num))