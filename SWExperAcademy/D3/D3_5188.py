#D3 5188 최소합
from collections import deque

for t in range(int(input())):
    answer = 987654321
    bound = int(input())
    board = [list(map(int, input().split())) for _ in range(bound)]
    stack = deque()
    stack.append((0,0,board[0][0]))
    while stack:
        y, x, t_sum = stack.pop()
        #목표지점에 도착했고 합이 answer보다 적다면 갱신
        if y == bound-1 and x == bound-1 and answer > t_sum:
            answer = t_sum
            continue
        #아래로 내려갈수있다면 내려가기
        if y+1 < bound:
            stack.append((y+1, x, t_sum + board[y+1][x]))
        #우측으로 갈수있다면 가기
        if x+1 < bound:
            stack.append((y, x+1, t_sum + board[y][x+1]))
    print('#{} {}'.format(t+1, answer))