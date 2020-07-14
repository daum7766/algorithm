# bronze 1 설탕 배달

N = int(input())

count5 = N // 5
count3 = 0
N = N % 5
answer = -1
while N >= 0:
    if N % 3 == 0:
        count3 = N // 3
        answer = count5 + count3
        break

    if count5 == 0:
        break
    count5 -= 1
    N += 5

print(answer)