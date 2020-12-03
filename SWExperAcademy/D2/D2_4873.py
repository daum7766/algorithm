# D2 4876 반복문자 지우기

for t in range(int(input())):
    user_input = input()
    stack = []
    for s in user_input:
        if len(stack) == 0:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
    print('#{} {}'.format(t+1, len(stack)))