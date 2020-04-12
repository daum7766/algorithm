#D2 4836 색칠하기
T = int(input())
for t in range(T):
    case = int(input())
    #색상 1, 2의 위치를 저장하는 리스트, 내부값은 셋이다.
    position = [set({}), set({})]
    #케이스만큼 반복
    for i in range(case):
        x1, y1, x2, y2, color = map(int, input().split())
        #x, y를 돌면서 set에 넣는다.
        for a in range(x1, x2+1):
            for b in range(y1, y2+1):
                position[color-1].add((a, b))
    #교집합을 이용하여 겹치는 부분만 꺼낸다.
    result = position[0] & position[1]
    #겹치는 만큼 출력
    print('#{} {}'.format(t+1, len(result)))