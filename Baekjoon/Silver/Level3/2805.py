# silver 3 나무자르기
from sys import stdin

N, M = map(int, stdin.readline().split())

woods = list(map(int, stdin.readline().split()))
min_num = 1
max_num = sum(woods)
answer = 0
while min_num <= max_num:
    mid_num = (min_num + max_num) // 2
    wood_count = 0
    for wood in woods:
        diff = wood - mid_num
        if diff > 0:
            wood_count += diff
    if M == wood_count:
        answer = mid_num
        break
    if wood_count > M:
        answer = mid_num
        min_num = mid_num + 1
    else:
        max_num = mid_num - 1

print(answer)