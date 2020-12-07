# D3 11315 오목판정

four = 4
zero = 0
yes = 'YES'
no = 'NO'


def gomoku():
    N = int(input())
    field = []
    for i in range(N):
        field.append(input())
    return find(field, N)


def find(field, N):
    for y in range(N):
        for x in range(N):
            # o가 아닐때는 체크할 필요가 없음
            if field[y][x] != 'o':
                continue
            # 오른쪽 체크
            if x + four < N and five_check(field, 0, 1, y, x):
                return yes
            # 하단 체크
            if y + four < N and five_check(field, 1, 0, y, x):
                return yes
            # 좌측상단
            if x - four >= zero and y - four >= zero and five_check(field, -1, -1, y, x):
                return yes
            # 우측상단
            if x + four < N and y - four >= zero and five_check(field, -1, 1, y, x):
                return yes
    return no


def five_check(field, dy, dx, y, x):
    for z in range(1, 5):
        if field[y + (dy * z)][x + (dx * z)] != 'o':
            return False
    return True


for t in range(int(input())):
    answer = gomoku()
    print('#{} {}'.format(t+1, answer))