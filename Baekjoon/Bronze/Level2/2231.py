# bronze 2 분해합

N = int(input())
case = {}
answer = 0
for i in range(N//2, N):
    str_num = str(i)
    temp_num = i
    for s in str_num:
        temp_num += int(s)
    if temp_num == N:
        answer = i
        break
    
print(answer)