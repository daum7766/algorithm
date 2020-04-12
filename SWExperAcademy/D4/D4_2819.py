#D4 2819 격자판의 숫자 이어 붙이기
#상하좌우 이동 리스트
move_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for t in range(1, int(input())+1):
    numlist = [input().split() for _ in range(4)]
    #중복을 없애기 위한 셋
    result = set()
    stack = []
    #각자리마다 만들수 있는 수가 다르므로 각 자리마다 계산
    for i in range(4):
        for j in range(4):
            stack.append((i, j, 0, numlist[i][j]))
            while stack:
                y, x, count, ans = stack.pop()
                #마지막인덱스까지 갔다면 결과 추가하기
                if count >= 6:
                    result.add(ans)
                    continue
                #상하좌우 데이터 넣기
                for d_y, d_x, in move:
                    dy = d_y + y
                    dx = d_x + x
                    if 0 <= dy < 4 and 0 <= dx < 4:
                        stack.append((dy, dx, count+1, ans + numlist[dy][dx]))
                    
    print('#{} {}'.format(t, len(result)))

# 함수를 이용한 풀이

""" #벽넘어갔는지 확인하기
def iswall(y, x):
    if x < 0 or y < 0 or x >=num or y >= 4:
        return False
    return True

#dfs를 이용한 이동
def dfs(y, x, idx, ans):
    #이동이 7번이 되었다면 set에 추가하고 멈추기
    if idx >= 7:
        result.add(ans + numlist[y][x])
        return
    #상하좌우 이동하면서 가능하면 추가
    for d_y, d_x, in move_list:
        dy = d_y + y
        dx = d_x + x
        #왔던곳을 중복이동 가능하므로 값을 바꾸거나 하지는 않는다.
        if iswall(dy, dx):
            dfs(dy, dx, idx+1, ans + numlist[dy][dx])

T = int(input())
for t in range(1, T+1):
    numlist = [input().split() for _ in range(4)]
    result = set()
    num = 4
    #각자리마다 만들수 있는 수가 다르므로 각 자리마다 계산
    for y in range(4):
        for x in range(4):
            dfs(y, x, 0, '')
    print('#{} {}'.format(t, len(result))) """