#D4 1486 장훈이의 높은선반

def bfs(idx, _sum):
    global min_num
    #합계가 이미 최소치를 넘어가면 계산안함
    if _sum >= min_num:
        return
    #마지막 까지 왔다면
    if idx >= N:
        #선반이상이고 최솟값보다 작을때 값갱신
        if _sum >= B and _sum < min_num:
            min_num = _sum
        return
    visited[idx] = True
    bfs(idx+1, _sum + height[idx])
    visited[idx] = False
    bfs(idx+1, _sum)


T = int(input())
for t in range(1, T+1):
    #N = 점원수, B = 선반높이
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_num = 987654321
    visited = [False] * N
    bfs(0, 0)
    print('#{} {}'.format(t, min_num - B))