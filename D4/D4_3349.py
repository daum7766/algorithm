#D4 3349 최솟값으로 이동하기

#둘중 하나가 같다면 차이만큼 결과에 더하기
#기회비용 1
#둘다 크다면 x,y 늘리기
#둘다 작다면 x,y 줄이기
#둘중 하나만 작다면 작은것만 늘리기

for t in range(1, int(input()) + 1):
    W, H, N = map(int, input().split())
    pos_list = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for count in range(N-1):
        y, x = pos_list[count]
        end_y, end_x = pos_list[count+1]
        while True:
            if y == end_y:
                result += abs(end_x - x)
                break
            if x == end_x:
                result += abs(end_y - y)
                break
            result += 1
            if y > end_y and x > end_x :
                y -= 1
                x -= 1
            else:
                if x < end_x : x += 1
                if y < end_y : y += 1
    print('#{} {}'.format(t, result))