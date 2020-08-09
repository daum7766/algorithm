# silver 4 균형잡힌 세상

while True:
    line = input()
    stack = []
    answer = 'yes'
    if line == '.':
        break
    for i in line:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break
        elif i == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
    if len(stack):
        answer = 'no'
    print(answer)
        