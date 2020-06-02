#D4 1238 Contact

#BFS를 이용한 풀이
def bfs(queue):
    global result
    #큐가 빌때까지 반복
    while queue:
        second_queue = []
        temp_result = 0
        while queue:
            #꺼내서 사용하고 사용체크
            temp = queue.pop()
            use_check[temp] = True
            #현재 전파상태에서 최댓값 찾기
            if temp > temp_result:
                temp_result = temp
            #연결되어있는부분 큐에 넣기
            while connect_list[temp]:
                s_temp = connect_list[temp].pop()
                #이미 들른곳이라면 패스
                if use_check[s_temp]: continue
                second_queue.append(s_temp)
        #가야할 장소가 있다면 bfs다시 돌리기
        if second_queue:
            queue = second_queue
    #큐가 비어있다면 마지막 전파단계이다.
    result = temp_result


for t in range(10):
    connect_list = [set() for _ in range(101)]
    use_check = [False] * 101
    length, start = map(int, input().split())
    temp_list = list(map(int, input().split()))
    for i in range(0, length, 2):
        connect_list[temp_list[i]].add(temp_list[i+1])
    result = 0
    bfs([start])
    print('#{} {}'.format(t+1, result))