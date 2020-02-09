#골드5 게리멘더링
import sys

sys.stdin = open('input.txt', 'r')

#연결안된 선거구가 1개이상일때 동작
def zero_check():
    global sum1, sum2
    if zero_count > 1:
        print('#{} '.format(t), end = '')
        print(-1)
        return True

    if zero_count == 1:
        for i in range(N):
            if i != zero_index:
                sum1 += Population[i]
        sum2 = Population[zero_index]
        print('#{} '.format(t), end = '')
        print(abs(sum1 - sum2))
        return True
    return False

T = int(input())
for t in range(1, T+1):
    N = int(input())
    Population = list(map(int, input().split()))
    connect = []

    #연결이 안된섬의 개수 카운트
    zero_count = 0
    zero_index = 0
    #각 선거구의 합
    sum1, sum2 = 0, 0
    result = 1000
    for i in range(N):
        connect.append(list(map(int, input().split())))
        if not connect[i].pop(0):
            zero_count += 1
            zero_index = i

    if zero_check():
        continue
    print('#{} '.format(t), end = '')
    print(result)