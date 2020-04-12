#가로세로 대각선합중 제일큰것 구하기
#D2_1209 sum
T = 10
for t in range(1, T+1):
    abc = input()
    lst = []
    for i in range(100):
        temp_lst = list(map(int, input().split()))
        lst.append(temp_lst)
    max_sum = 0
    #가로, 세로합
    for i in range(100):
        sum1, sum2 = 0, 0
        for j in range(100):
            sum1 += lst[i][j]
            sum2 += lst[j][i]
        max_sum = max(sum1, sum2, max_sum)
    #대각선합
    for i in range(100):
        sum1, sum2 = 0, 0
        sum1 += lst[i][i]
        sum2 += lst[i][99-i]
    max_sum = max(sum1, sum2, max_sum)
    print("#{} {}".format(t, max_sum))