# bronze 2 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())

# 제일 마지막날은 A만큼 올라간다
day = 1
V -= A
# 두개의 차이
diff = A-B

# 두개의 차이만큼 일수가 생긴다
day += V // diff
# 나누고 남는다면 그만큼 더 올라가야 한다
if V % diff:
    day += 1

print(day)