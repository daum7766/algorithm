#D3 2805 농작물 수확하기
T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    t_N = N//2
    change = -1
    answer = 0
    for i in range(N):
        if i >= N//2:
            change = 1
        for j in range(abs(i-N//2), abs(N-t_N)):
            answer += map_list[i][j]
        t_N += change
    print('#{} {}'.format(t, answer))