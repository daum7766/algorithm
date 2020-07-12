# bronze 2 벌집

# 처음에만 주의하면 풀수있다.
# 한바퀴 돌때마다 6개씩 커진다.

N = int(input())
count = 6
distance = 1
while N > 1:
    N -= count
    distance += 1
    count += 6

print(distance)