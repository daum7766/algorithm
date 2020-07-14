# silver 5 좌표정렬하기

N = int(input())

position = [tuple(map(int, input().split())) for _ in range(N)]

position.sort()

for p in position:
    print(*p)