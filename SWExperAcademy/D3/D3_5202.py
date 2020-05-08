#D3 5202 화물 도크

for t in range(int(input())):
    answer = 1
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]
    #끝나는 시간으로 정렬
    time_list.sort(key=lambda x: x[1], reverse=True)
    #제일빨리 끝나는 화물 가져오기
    end_time = time_list.pop()[1]
    #화물이 빌때까지 반복
    while time_list:
        s, e = time_list.pop()
        #이전화물끝나는 시간보다 늦게시작하면
        if end_time <= s:
            #끝나는 시간 갱신하고 answer 증가
            end_time = e
            answer += 1
    
    print('#{} {}'.format(t+1, answer))