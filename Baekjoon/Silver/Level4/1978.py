# silver 4 소수찾기

input()
numbers = list(map(int, input().split()))
answer = 0

max_num = max(numbers)
eratosthenes = [ True for _ in range(max_num+1)]
eratosthenes[1] = False
for i in range(2, max_num+1):
    for j in range(i*2, max_num+1, i):
        eratosthenes[j] = False

for number in numbers:
    if eratosthenes[number]:
        answer += 1

print(answer)