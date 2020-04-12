#D4 1865 동철이의 일 분배
#N = 일의 개수 1 <= N <= 16
#각줄은 직원의 성공 확률

def bfs(idx, answer = 100):
    global max_value
    #값이 계산한 이전값보다 작다면 리턴
    if max_value != -1 and answer <= max_value: return
    #위에서 걸러지므로 여기까지 왔다면 그냥 값을 넣는다.
    if idx >= N:
        max_value = answer
        return
    #조합을 구해서 bfs하기
    for i in range(N):
        if use_check[i]:
            use_check[i] = False
            bfs(idx+1, answer * (success_list[idx][i]) )
            use_check[i] = True


T = int(input())
for t in range(1, T+1):
    N = int(input())
    #람다식을 이용하여 넣을때부터 100으로 나누어 사용
    success_list = [list(map(lambda x : int(x)/100, input().split())) for _ in range(N)]
    use_check = [True for _ in range(N)]
    max_value = -1
    bfs(0)
    #6자리수로 제한하여 출력
    print('#{} {:6f}'.format(t, max_value))