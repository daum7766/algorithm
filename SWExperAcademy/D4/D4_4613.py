#D4 4613 러시아 국기 같은 깃발
targets = ['W', 'B', 'R']

def dfs(idx, color, _sum):
    global result
    #가치지기
    if result <= _sum : return
    #결과 더하기
    if idx >= N-1: 
        result = _sum
        return
    #다음색상까지, 넘어온게 흰색이라면  흰색, 파랑만
    #인덱스때문에 최댓값은 3으로 설정
    for i in range(color, min(3, color+2)):
        temp = 0
        #마지막줄까지 왔는데 컬러가 흰색이라면 다음으로 넘어가기
        if idx >= N-2 and i == 0: continue
        for j in Flag[idx]:
            #색상이 다른것들 카운트
            if j != targets[i]: temp += 1
        dfs(idx+1, i, _sum + temp)

#제일 윗줄과 아랫줄 체크하기
def init():
    global result
    for i in Flag[0]:
        if i != 'W': result += 1
    for i in Flag[N-1]:
        if i != 'R': result += 1

for t in range(1, int(input()) + 1):
    #입력받기
    N, M = map(int, input().split())
    Flag = [list(input()) for _ in range(N)]
    #최종 결과값
    result = 987654
    #갯수 체크하기
    dfs(1, 0, 0)
    #제일 위와 아래줄 체크하기
    init()
    print('#{} {}'.format(t, result))