#5021 D3 컨테이너 운반

for t in range(int(input())):
    answer = 0
    N, M = map(int, input().split())
    N_list = sorted(list(map(int, input().split())))
    M_list = sorted(list(map(int, input().split())))
    #트럭과 컨테이너가 남아있을때까지 반복
    while M_list and N_list:
        truck = M_list.pop()
        #컨테이너가 남아있을때까지 반복
        while N_list:
            container = N_list.pop()
            #트럭이 화물을 실을 수 있다면
            if truck >= container:
                #정답에 무게 추가
                answer += container
                break
    print('#{} {}'.format(t+1, answer))