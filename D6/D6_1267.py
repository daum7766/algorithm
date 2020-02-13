#D6 1267 작업순서
T = 10
for t in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [True for _ in range(v+1)]
    temp_list = list(map(int, input().split()))
    count = v
    #그래프 만들기, 선행순서이므로 반대로 넣어준다.
    #ex a가 1이고 b가 2라면
    #2번노드는 1번노드가 수행완료가 되어야 가능하다.
    for i in range(0, len(temp_list), 2):
        a = temp_list[i]
        b = temp_list[i+1]
        graph[b].append(a)
    #결과누적 리스트
    result = []
    #노드가 모두 수행될때까지 반복한다.
    while count:
        #1번노드부터 마지막 노드까지 반복
        for i in range(1, len(graph)):
            #현재노드가 수행되지 않았다면
            if visited[i]:
                #선행노드를 확인한다.
                for j in graph[i]:
                    #선행노드가 아직 수행되지 않았다면 멈춘다.
                    if visited[j]:
                        break
                else:
                    #선행노드가 모두 수행되었다면
                    #현재노드를 수행했다고 바꾸고 결과에 추가한다.
                    #노드가 수행되었으므로 count를 감소시킨다.
                    visited[i] = False
                    result.append(i)
                    count -= 1
    print('#{} '.format(t), end='')
    print(*result)