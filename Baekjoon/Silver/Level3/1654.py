# silver 3 랜선 자르기
from sys import stdin, stdout

K, N = map(int, input().split())

user_input = [int(stdin.readline()) for _ in range(K)]
min_num = 1
max_num = sum(user_input)
answer = 0
while min_num <= max_num:
    middle_num = (min_num + max_num) // 2
    count = 0
    for i in user_input:
        count += i // middle_num
    
    if count >= N:
        answer = middle_num
        min_num = middle_num + 1
    else:
        max_num = middle_num -1

stdout.write(str(answer))