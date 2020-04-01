# D2 5097 회전
for t in range(1, 1+int(input())):
    N, count = map(int, input().split())
    queue = input().split()
    # N번 반복하면 원상태이므로 나머지 연산
    count %= N
    #남은것은 인덱스가 된다.
    print('#{} {}'.format(t, queue[count]))