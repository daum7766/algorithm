# silver 5 체스판 다시 칠하기

def check(temp_chess, A, B):
    global answer
    count = 0
    for i in range(8):
        for j in range(8):
            # 짝수일때
            if i % 2 == 0:
                # j가 짝수일때
                if j % 2 == 0:
                    if temp_chess[i][j] == B:
                        count += 1
                else:
                    if temp_chess[i][j] == A:
                        count += 1
            else:
                if j % 2 == 0:
                    if temp_chess[i][j] == A:
                        count += 1
                else:
                    if temp_chess[i][j] == B:
                        count += 1
    if answer > count:
        answer = count
        

N, M = map(int, input().split())

chess = [list(input()) for _ in range(N)]
answer = 250
for i in range(N-7):
    for j in range(M-7):
        temp_chess = chess[i:i+8]
        for k in range(8):
            temp_chess[k] = temp_chess[k][j:j+8]

        check(temp_chess, 'W', 'B')
        check(temp_chess, 'B', 'W')

print(answer)