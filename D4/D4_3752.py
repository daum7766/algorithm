#D4 3752 가능한 시험 점수

T = int(input())
for t in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    #수가 나왔는지 체크
    check = [1] + [0] * sum(scores)
    #나온 수 체크
    visit = [0]
    for i in scores:
        temp = visit[:]
        for j in temp:
            if not check[i + j]:
                #사용한 수는 체크
                check[i + j] = 1
                #이미 계산된 수에 더 계산하기 위해 추가한다.
                visit.append(i + j)
    print('#{} {}'.format(t, len(visit)))