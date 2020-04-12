#D4 1258 행렬찾기
#옆으로 어디까지 갈수있나 길이체크
def width(i, j):
    count = 1
    dx = j
    while True:
        dx += 1
        if dx >= N: break
        if map_list[i][dx]: count+=1
        else: break
    return count
#아래로 얼마까지 갈수있나 길이체크
def height(i, j):
    count = 1
    dy = i
    while True:
        dy += 1
        if dy >= N: break
        if map_list[dy][j]: count+=1
        else: break
    return count

#이미 체크한 영역은 다시검사하지 않기위해 0으로 바꿈
def change(s_y, s_x, e_y, e_x):
    for i in range(s_y, e_y):
        for j in range(s_x, e_x):
            map_list[i][j] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    #리스트 내포기능으로 반복해서 입력받음
    map_list = [list(map(int, input().split())) for _ in range(N)]
    answer_list = []
    for i in range(N):
        for j in range(N):
            #값이 있다면
            if map_list[i][j]:
                #가로길이 받아오고
                w = width(i, j)
                #세로길이 받아와서
                h = height(i, j)
                #리스트 내용바꿔주고
                change(i, j, i+h, j+w)
                #행열 크기 넣어주고 곱한값 넣어주고
                answer_list.append([h, w, h*w])
    #출력해야 하니까 정렬해야 하는데 곱한값 기준으로 오름차순, 다음은 행렬 크기로 오름차순
    answer_list = sorted(answer_list, key=lambda x: (x[2], x[0]))
    #이 밑에는 출력하기
    print('#{} {}'.format(t, len(answer_list)), end= ' ')
    for r, c, _ in answer_list:
        print('{} {}'.format(r, c), end=' ')
    print()