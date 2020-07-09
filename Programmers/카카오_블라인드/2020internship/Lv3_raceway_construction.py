from collections import deque

def solution(board):
    answer = 0
    # 오른쪽, 왼쪽, 아래, 위
    move = [(0, 1, 0), (0, -1, 0), (1, 0, 1), (-1, 0, 1)]
    dq = deque()
    length = len(board)
    inf = float('inf')
    price_board = [[inf for _ in range(length)] for _ in range(length)]

    board[0][0] = 1
    if board[0][1] == 0:
        # y, x, 방향(가로0, 세로1), 누적금액
        dq.append((0, 1, 0, 100))
        board[0][1] = 1
    if board[1][0] == 0:
        dq.append((1, 0, 1, 100))
        board[1][0] = 1
    while len(dq):
        y, x, pos, price = dq.popleft()
        for dy, dx, move_pos in move:
            move_y = y + dy
            move_x = x + dx
            # 이동하려는 장소의 이동이 가능하다면
            if 0 <= move_y < length and 0 <= move_x < length and board[move_y][move_x] == 0:
                temp_price = price + 100
                if pos != move_pos:
                    temp_price += 500
                if price_board[move_y][move_x] >= temp_price:
                    price_board[move_y][move_x] = temp_price
                    dq.append((move_y, move_x, move_pos, temp_price))

    answer = price_board[length-1][length-1]
    return answer


if __name__ == "__main__":
    board_list = [
        [[0,0,0],[0,0,0],[0,0,0]],
        [
            [0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],
            [0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]
        ],
        [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
        [
            [0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],
            [1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]
        ]
    ]
    result_list = [900, 3800, 2100, 3200]
    length = len(result_list)
    for i in range(length):
        answer = solution(board_list[i])
        if answer == result_list[i]:
            print('{}번 정답'.format(i+1))
        else:
            print('{}번 실패'.format(i+1))
            print('{} != {}'.format(answer, result_list[i]))