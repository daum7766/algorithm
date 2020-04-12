#D3 5688 세제곱근을 찾아라.
arr = [i**3 for i in range(1000001)]

for t in range(1, int(input()) + 1):
    N = int(input())
    start, end = 0, 1000000
    answer = -1
    while start <= end:
        avg = (start+end)//2
        if arr[avg] == N:
            answer = avg
            break
        elif arr[avg] > N:
            end = avg - 1
        else :
            start = avg + 1
    print('#{} {}'.format(t, answer))