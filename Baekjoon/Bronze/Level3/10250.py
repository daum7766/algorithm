# bronze 3 ACM호텔
num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())
    floor = N % H
    room = N // H + 1
    if floor == 0:
        room -= 1
        floor = H

    print(floor*100 + room)