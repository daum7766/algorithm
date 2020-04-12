#D4 5432 쇠막대 자르기
for t in range(1, int(input())+1):
    command = input()
    stack = answer = 0
    length = len(command)
    for i in range(length):
        if command[i] == '(': stack += 1
        else:
            stack -= 1
            if command[i-1] == '(': answer += stack
            else: answer += 1
    print('#{} {}'.format(t, answer))
