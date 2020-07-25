# silver 4 큐

from collections import deque

queue = deque()

N = int(input())
answer = []
for _ in range(N):
    user_input = input().split()
    if user_input[0] == 'push':
        queue.append(int(user_input[1]))
    elif user_input[0] == 'pop':
        if len(queue):
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif user_input[0] == 'size':
        answer.append(len(queue))
    elif user_input[0] == 'empty':
        if len(queue):
            answer.append(0)
        else:
            answer.append(1)
    elif user_input[0] == 'front':
        if len(queue):
            answer.append(queue[0])
        else:
            answer.append(-1)
    elif user_input[0] == 'back':
        if len(queue):
            answer.append(queue[-1])
        else:
            answer.append(-1)
    

for i in answer:
    print(i)