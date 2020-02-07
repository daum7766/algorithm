#D4 6109 추억의 2048게임

import sys

sys.stdin = open('input.txt', 'r')
#up 혹은 down이면 좌표를 바꿔준다.
def swap(i, j):
    global command
    if command == 'up' or command == 'down':
        return j, i
    return i, j
#명령을 처리해주는 함수이다.
def start(n, command):
    data = dict_lst[command]
    #up down left right에 따라 반복문 조건을 바꾼다.
    for a in range(data[0], data[1], data[2]):
        temp = []
        for j in range(data[3], data[4], data[5]):
            i, j = swap(a, j)
            #데이터가 0이 아닌것들만 더한다.
            if list_2048[i][j]:
                temp.append(list_2048[i][j])
                list_2048[i][j] = 0
        k = 0
        #인근에 있는 값들을 더하고 팝시킨다.
        while len(temp) > k+1:
            if temp[k] == temp[k+1]:
                temp[k] += temp[k+1]
                temp.pop(k+1)
            k+=1
        #데이터를 처리했다면 다시 넣어준다.
        for j in range(data[3], data[4], data[5]):
            i, j = swap(a, j)
            if not temp:
                break
            list_2048[i][j] = temp.pop(0)

T = int(input())
for t in range(1, T+1):
    list_2048 = []
    n, command = input().split()
    n = int(n)
    dict_lst = {'up': (0, n, 1, 0, n, 1), 'down': (n-1, -1, -1, n-1, -1, -1), 'left' : (0, n, 1, 0, n, 1), 'right' : (0, n, 1, n-1, -1, -1)}
    #들어온 데이터를 리스트에 추가한다.
    for i in range(n):
        list_2048.append(list(map(int, input().split())))
    start(n, command)
    print("#{}".format(t))
    #결과출력
    for k in list_2048:
        print(*k)