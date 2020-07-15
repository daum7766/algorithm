# silver 5 영화감독 숌

N = int(input())

number = 666
answer = 0
while True:
    if str(number).find('666') != -1:
        answer += 1
    if N == answer:
        break
    number += 1

print(number)