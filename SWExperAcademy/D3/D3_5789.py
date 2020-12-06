# D3 5789 현주의 상자 바꾸기

def solution(N, Q):
    boxes = [0 for _ in range(N)]
    for i in range(Q):
        start, end = map(int, input().split())
        for j in range(start-1, end):
            boxes[j] = i + 1
    return boxes
        

for t in range(int(input())):
    N, Q = map(int, input().split())
    answer = solution(N, Q)
    print('#{} '.format(t+1), end='')
    print(*answer)