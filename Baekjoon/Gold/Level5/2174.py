# Gold 5 2174 로봇 시뮬레이션

direction_num = {'N': 0, 'E': 1, 'S': 2, 'W':3, 0:'N', 1:'E', 2:'S', 3:'W'}
direction_to_position = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W':(0, -1)}
def find_direction(start, command, repeat):
    repeat %= 4 
    start_num = direction_num[start]
    if command == 'L':
        start_num-=repeat
        if start_num < 0: start_num += 4
    else:
        start_num+=repeat
        if start_num > 3: start_num -= 4
    return direction_num[start_num]
answer = None
A, B = map(int, input().split())
field = [[0 for _ in range(A)] for _ in range(B)]
robots = [0]
N,M = map(int, input().split())
for i in range(N):
    x, y, direction = input().split()
    x, y = int(x)-1, int(y)
    robots.append([B-y, x, direction])
    field[B-y][x] = i+1
for i in range(M):
    idx, command, repeat = input().split()
    idx, repeat = int(idx), int(repeat)
    y, x, direction = robots[idx]
    if command == 'F':
        dy, dx = direction_to_position[direction]
        for i in range(repeat):
            move_y, move_x = y+dy, x+dx
            if 0 <= move_y < B and 0 <= move_x < A:
                if field[move_y][move_x]:
                    answer = 'Robot {} crashes into robot {}'.format(idx, field[move_y][move_x])
                    break
                else:
                    field[y][x]=0
                    field[move_y][move_x] = idx
                    y, x = move_y, move_x
                    robots[idx] = [move_y, move_x, direction]
            else:
                answer = 'Robot {} crashes into the wall'.format(idx)
                break
    else:
        robots[idx][2] = find_direction(direction, command, repeat)
    if answer: break
if not answer: answer = 'OK'
print(answer)