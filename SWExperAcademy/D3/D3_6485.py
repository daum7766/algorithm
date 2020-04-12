#D3 6485 삼성시의 버스 노선
#풀이 1
T = int(input())
for t in range(1, T+1):
    N = int(input())
    #결과 저장용 딕셔너리
    result = {}
    #그냥 나오면 전부다 카운팅
    for i in range(N):
        a, b = map(int, input().split())
        for k in range(a, b+1):
            result[k] = result.get(k, 0) + 1
    #정류장 개수 입력받기
    P = int(input())
    #정류장 번호 입력받기
    C_list = []
    for _ in range(P):
        C_list.append(int(input()))
    print('#{} '.format(t), end='')
    #있는 정류장만 출력한다.
    for C in C_list:
        print(result.get(C, 0), end=' ')
    print()

'''
풀이 2
T = int(input())
for t in range(1, T+1):
    # N = 버스노선개수
    N = int(input())
    bus_list = []
    #버스 이동경로 받기
    for i in range(N):
        a, b = map(int, input().split())
        bus_list.append((a, b))
    #P = 버스 정류장 개수
    P = int(input())
    # C = 정류장 번호
    C_list = []
    # 결과 저장용 딕셔너리
    result = {}
    #정류장 번호가 다를 수 있다. 충격...
    for _ in range(P):
        C = int(input())
        C_list.append(C)
        result[C] = 0
    #이동 범위에 맞는 개수 증가
    for a, b in bus_list:
        for i in range(a, b+1):
            #범위안에 있는 정류장만 카운팅
            if i in result:
                result[i] += 1
    #i번째 버스노선은 번호가 Ai이상이고 Bi 이하인 모든 정류장만 다님
    print('#{} '.format(t), end='')
    for C in C_list:
        print(result[C], end=' ')
    print()
'''

'''
#풀이 3
T = int(input())
for t in range(1, T+1):
    N = int(input())
    #결과 저장용
    result = [0] * 5001
    #그냥 나오면 전부다 카운팅
    for i in range(N):
        a, b = map(int, input().split())
        for k in range(a, b+1):
            result[k] +=1
    #정류장 개수 입력받기
    P = int(input())
    print('#{} '.format(t), end='')
    for _ in range(P):
        print(result[int(input())], end=' ')
    print()
'''