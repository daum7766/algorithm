#D3 5189 전자카트
def dfs(idx, _sum, count):
    global answer
    # 이미 넘어갔다면 계산하지 않음
    if _sum >= answer:
        return
    #마지막전까지 계산되었다면
    if count == bound-1:
        #처음꺼로 돌아가야하니 0번재를 더하고
        _sum += board[idx][0]
        #작다면 갱신
        if _sum < answer:
            answer = _sum
        return
    #반복문을 돌리며 체크, 0은 마지막에 해야함으로 1부터 시작
    for i in range(1, bound):
        #두개가 같은곳은 넣으면 안되고, 방문하지 않은장소만
        if idx != i and visited[i]:
            visited[i] = 0
            dfs(i, _sum + board[idx][i], count+1)
            visited[i] = 1

for t in range(int(input())):
    answer = 987654321
    bound = int(input())
    board = [list(map(int, input().split())) for _ in range(bound)]
    visited = [1 for _ in range(bound)]
    dfs(0, 0, 0)
    print('#{} {}'.format(t+1, answer))