# silver 4 스택

stack = []

N = int(input())
answer = []
for _ in range(N):
    user_input = input().split()
    if user_input[0] == 'push':
        stack.append(int(user_input[1]))
    elif user_input[0] == 'pop':
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    elif user_input[0] == 'size':
        answer.append(len(stack))
    elif user_input[0] == 'empty':
        if stack:
            answer.append(0)
        else:
            answer.append(1)
    elif user_input[0] == 'top':
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)

for i in answer:
    print(i)