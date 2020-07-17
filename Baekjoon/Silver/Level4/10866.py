# silver 4 덱

from collections import deque

dq = deque()

N = int(input())
answer = []
for _ in range(N):
    user_input = input().split()
    if user_input[0] == 'push_front':
        dq.appendleft(int(user_input[1]))
    elif user_input[0] == 'push_back':
        dq.append(int(user_input[1]))
    elif user_input[0] == 'pop_front':
        if len(dq):
            answer.append(dq.popleft())
        else:
            answer.append(-1)
    elif user_input[0] == 'pop_back':
        if len(dq):
            answer.append(dq.pop())
        else:
            answer.append(-1)
    elif user_input[0] == 'size':
        answer.append(len(dq))
    elif user_input[0] == 'empty':
        if len(dq):
            answer.append(0)
        else:
            answer.append(1)
    elif user_input[0] == 'front':
        if len(dq):
            answer.append(dq[0])
        else:
            answer.append(-1)
    elif user_input[0] == 'back':
        if len(dq):
            answer.append(dq[-1])
        else:
            answer.append(-1)
    

for i in answer:
    print(i)