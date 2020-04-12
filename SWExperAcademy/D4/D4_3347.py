#D4 3347 올림픽 종목 투표

for t in range(1, int(input()) + 1):
    #올림픽 종목과 심사위원 입력받기
    N, M = map(int, input().split())
    #올림픽 종목 비용 입력받기
    N_list = list(map(int, input().split()))
    #심사위원 생각비용 입력받기
    M_list = list(map(int, input().split()))
    #각종목당 투표갯수 저장변수
    count_list = [0]*N
    #심사위원을 기준으로 돈다
    for m in M_list:
        #올림픽 종목을 순회하면서 투표횟수를 카운팅한다.
        for i in range(len(N_list)):
            if N_list[i] <= m:
                count_list[i] += 1
                break
    #제일 많은 투표횟수를 얻은 인덱스를 구한다.
    result = count_list.index(max(count_list)) + 1
    print('#{} {}'.format(t, result))