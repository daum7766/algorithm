# Gold 5 이중 우선순위 큐

# 이진 탐색 알고리즘 해주는 라이브러리
import bisect
from collections import deque

for _ in range(int(input())):
    queue = deque()
    check = {}
    for _ in range(int(input())):
        command, number = input().split()
        number = int(number)
        if command == 'I':
            if check.get(number, 0):
                check[number] += 1
            else:
                check[number] = 1
                bisect.insort_left(queue, number)
        elif len(queue):
            # 최솟값 삭제
            if number == -1:
                num = queue[0]
                if check[num] == 1:
                    queue.popleft()
            # 최댓값 삭제
            else:
                num = queue[-1]
                if check[num] == 1:
                    queue.pop()
            check[num] -= 1
    if len(queue):
        print('{} {}'.format(queue[-1], queue[0]))
    else:
        print('EMPTY')