#2001 D2 파리퇴치
#누적합을 이용한 계산

def data_init():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for i in range(N):
        for j in range(N):
            sum_arr[i][j+1] = arr[i][j] + sum_arr[i][j]

    return N, M, arr, sum_arr


def solution():
    max_data = 0
    N, M, arr, sum_arr = data_init()

    for y in range(N-M+1):
        for x in range(N-M+1):
            data = 0
            for i in range(M):
                data += sum_arr[y+i][x+M] - sum_arr[y+i][x]
            max_data = max(max_data, data)

    return max_data


test_case_size = int(input())
for t in range(test_case_size):
    answer = solution()
    print('#{} {}'.format(t+1, answer))