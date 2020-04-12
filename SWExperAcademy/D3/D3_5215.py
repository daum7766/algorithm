#D3 5215 햄버거 다이어트
#깊이우선탐색
def dfs(index, sum_flavor = 0, sum_kal = 0):
    global max_flavor
    #칼로리 넘어가면 리턴
    if sum_kal > L: return
    #최고 맛점수보다 높으면 갱신
    if max_flavor < sum_flavor: max_flavor = sum_flavor
    #마지막 인덱스까지 내려왔다면 리턴
    if index == N : return
    flavor, kal = kal_list[index]
    #재료를 사용했을때
    dfs(index+1, sum_flavor + flavor, sum_kal + kal)
    #재료를 사용하지 않았을때
    dfs(index+1, sum_flavor, sum_kal)

T = int(input())
for t in range(1,T+1):
    N, L = map(int, input().split())
    kal_list = [list(map(int, input().split())) for _ in range(N)]
    max_flavor = 0
    dfs(0)
    print("#{} {}".format(t, max_flavor))