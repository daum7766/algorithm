#2001 D2 파리퇴치
#누적합을 이용한 계산
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Flys = [list(map(int, input().split())) for _ in range(N)]
    sum_Flays = [[0 for i in range(N+1)] for j in range(N)]
    for i in range(N):
        for j in range(1, N+1):
            sum_Flays[i][j] = sum_Flays[i][j-1] + Flys[i][j-1]
    max_sum = 0
    for i in range(N-M+1):
        for j in range(M, N+1):
            current_sum = 0
            for k in range(M):
                current_sum += sum_Flays[i+k][j] - sum_Flays[i+k][j-M]
            max_sum = max(max_sum, current_sum)

            
    print("#{} {}".format(t, max_sum))
