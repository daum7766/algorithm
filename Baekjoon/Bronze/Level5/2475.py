# bronze 5 검증수

user_input = list(map(int, input().split()))
answer = 0
for i in user_input:
    answer += i*i

print(answer % 10)