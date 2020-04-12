#D2 4869 종이붙이기
#최대 넓이는 30이다.
data = [0 for _ in range(31)]

def dp(num):
    if not num :
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 3
    if not data[num]:
        data[num] = dp(num-1) + 2*dp(num-2) 

    return data[num]

T = int(input())
for t in range(1, T+1):
    N = int(input())//10
    print('#{} {}'.format(t, dp(N)))