# silver 4 카드2

from collections import deque

dq = deque(range(1, int(input())+1))

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())


print(dq.popleft())