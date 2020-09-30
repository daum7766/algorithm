# silver 3 마인크래프트

N, M, B = map(int, input().split())

fields = [list(map(int, input().split())) for _ in range(N)]

min_num = 0
max_num = 256
answer_hight = 0
answer_time = 99999999999

for h in range(257):
    block = B
    temp_time = 0
    for i in range(N):
        for j in range(M):
            if fields[i][j] < h:
                diff = h - fields[i][j]
                block -= diff
                temp_time += diff
            else:
                diff = fields[i][j] - h
                block += diff
                temp_time += diff * 2
    if block < 0:
        break
    if answer_time >= temp_time:
        answer_time = temp_time
        answer_hight = h

print('{} {}'.format(answer_time, answer_hight))