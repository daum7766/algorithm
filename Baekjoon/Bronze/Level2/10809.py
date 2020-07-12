# bronze 2 알파벳 찾기

user_input = input()
check = [-1 for _ in range(26)]

for i in range(len(user_input)):
    index = ord(user_input[i]) - 97
    if check[index] == -1:
        check[index] = i

print(*check)
