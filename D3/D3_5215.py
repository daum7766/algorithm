#D3 5215 햄버거 다이어트
#깊이우선탐색
def dfs(index, L):
    global kal_list
    #전역변수 사용선언
    global max_box, sum_score, sum_kal
    #현재들어온 깊이가 마지막이라면 리턴
    if index == len(kal_list):
        return
    dfs(index+1, L)
    #경우의 수에 넣겠다면 칼로리 검사
    #칼로리가 넘어간다면 계산중지
    if sum_kal + kal_list[index][1] > L:
        return
    #칼로리가 넘지않는다면 변수값 갱신
    sum_score += kal_list[index][0]
    sum_kal += kal_list[index][1]
    #현재값과 이전값중 높은것을 저장
    max_box = max(max_box, sum_score)
    dfs(index+1, L)
    #재귀에서 나오면 값 빼기
    sum_score -= kal_list[index][0]
    sum_kal -= kal_list[index][1]


T = int(input())
for t in range(1,T+1):
    N, L = map(int, input().split())
    max_box, sum_score, sum_kal = 0, 0, 0
    kal_list = [list(map(int, input().split())) for _ in range(N)]
    dfs(0, L)
    print("#{} {}".format(t, max_box))
    max_box = 0