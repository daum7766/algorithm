# silver 4 괄호

N = int(input())

for _ in range(N):
    vps = input()
    stack = []
    answer = 'YES'
    for i in vps:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'NO'
                break
    if len(stack) > 0:
        answer = 'NO'
    print(answer)