# silver 5 좌표 정렬하기 2

N = int(input())

position = [tuple(map(int, input().split())) for _ in range(N)]

position.sort(key=lambda x : (x[1], x[0]))

for p in position:
    print(*p)