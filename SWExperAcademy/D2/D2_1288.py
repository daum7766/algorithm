#D2 1288 새로운 불면증 치료법

T = int(input())
for t in range(1, T+1):
    #셋의 중복미허용을 이용한 풀이
    set_list = set()
    N = int(input())
    count = 0
    #셋의 길이가 10이라면 모두 포함된것이다.
    while len(set_list) < 10:
        count += 1
        temp = N * count
        #스트링으로 바꿔서 각자리를 쪼개고 셋으로바꾸어 넣는다.
        temp = set(map(int, list(str(temp))))
        #합집합을 이용하여 처리
        set_list |= temp
    #출력은 N*횟수를 이용하여 출력
    print('#{} {}'.format(t, N*count))