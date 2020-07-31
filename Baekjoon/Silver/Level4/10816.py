# silver 4 숫자카드 2

input()
numbers = list(map(int, input().split()))

num_dict = {}
for i in numbers:
    num_dict[i] = num_dict.get(i, 0) + 1

input()
numbers = list(map(int, input().split()))

answer = []
for i in numbers:
    answer.append(num_dict.get(i, 0))

print(*answer)