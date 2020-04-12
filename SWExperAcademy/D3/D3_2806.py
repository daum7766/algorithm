#D3 2806 N-Queen

#대각선 체크 함수
def possible(idx, c):
    for i in range(idx):
        #행과 열의 차이가 같다면
        if idx - i == abs(c - map_list[i]): return True
    return False
    
def dfs(idx):
    if idx == N:
        global answer
        answer += 1
        return
    for i in range(N):
        #이미 사용한 열이라면 넘어감
        if visit[i] : continue
        #대각선이 겹친다면 넘어감
        if possible(idx, i) : continue
        visit[i] = 1
        map_list[idx] = i
        dfs(idx + 1)
        visit[i] = 0

for t in range(1, int(input()) + 1):
    N = int(input())
    #대각선은 어떻게 체크하지?
    map_list = [0 for _ in range(N)]
    visit = [0 for _ in range(N)]
    answer = 0
    dfs(0)
    print('#{} {}'.format(t, answer))