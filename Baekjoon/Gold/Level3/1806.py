# gold 3 부분합

N, M = map(int, input().split())

user_input = list(map(int, input().split()))

end = 0
count = 0
answer = 100000001
for start in range(N):
    while count < M and end < N:
        count += user_input[end]
        end += 1
    if count >= M and answer > end - start:
        answer = end - start
    count -= user_input[start]

if answer == 100000001:
    answer = 0
print(answer)