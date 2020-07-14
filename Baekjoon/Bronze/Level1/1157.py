# bronze 1 단어 공부

word = input().upper()
max_count = 0
check = {}
answer = ''

for i in word:
    count = check.get(i, 0) + 1
    check[i] = count
    if max_count < count:
        max_count = count
        answer = i
    elif max_count == count:
        answer = '?'

print(answer)