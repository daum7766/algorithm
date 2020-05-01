#D5 1242 암호코드 스캔
secret = {
    211:0, 221:1, 122:2, 411:3, 132:4, 231:5, 114:6, 312:7, 213:8, 112:9,
}
 
hex_to_bin = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A': '1010', 'B': '1011', 
    'C': '1100', 'D': '1101', 'E': '1110', 'F':'1111',
}
 
 
for t in range(int(input())):
    answer = 0
    #가로 세로 받고
    N, M = map(int, input().split())
    #배열 받고
    array = [input() for _ in range(N)]
    board = ['' for _ in range(N)]
    for i in range(N):
        for j in range(M):
            board[i] += hex_to_bin[array[i][j]]
 
    for i in range(0, len(board)-4):
        j = (M*4) - 1
        while j > 56:
            if board[i][j] == '1' and board[i-1][j] == '0':
                c = [0 for _ in range(8)]
                for k in range(7, -1, -1):
                    x=y=z=0
                    while board[i][j] == '1': 
                        z+=1
                        j-=1 
                    while board[i][j] == '0':
                        y+=1
                        j-=1
                    while board[i][j] == '1':
                        x+=1
                        j-=1
                    while board[i][j] == '0':
                        j-=1
                    min_num = min(x, y, z)
                    temp = (x // min_num) * 100 + (y // min_num) * 10 + z // min_num
                    c[k] = secret.get(temp, -1)
                    if c[k] == -1: continue
                temp = (c[0]+c[2]+c[4]+c[6])*3 +c[1]+c[3]+c[5]+c[7]
                if not temp % 10:
                    answer += c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]
                j+=1
            j -= 1
             
    print('#{} {}'.format(t+1, answer))