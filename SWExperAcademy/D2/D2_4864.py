#D2 4864 문자열 비교
# T = int(input())
# for t in range(1, T+1):
#     s = input()
#     string = input()
#     result = 0
#     if s in string:
#         result = 1
#     print("#{} {}".format(t, result))


#보이어 무어 알고리즘
def pattonmatch(p, t):
    pattonLength = len(p)
    targetLength = len(t)
    #인덱스 위치를 나타내는 변수
    i = 0
    #두 길이의 차만큼만 반복한다.
    while i <= targetLength-pattonLength:
        #뒤에서부터 확인하므로 길이 -1
        j = pattonLength - 1
        # 반복하여 확인
        while j >= 0:
            #패턴이 일치하지 않는다면
            if p[j] != t[i+j]:
                #이동할 거리를 계산한다.
                #비교할 문자는 처음 비교하던 위치의 뒷글자를 넘긴다.
                st = find(p, t[i + pattonLength - 1])
                break
            #위의 조건이 무시되었다면 맞는것이므로 앞으로 이동한다.
            j = j - 1
        #-1까지 갔다면 모든 문자열이 일치한다.
        if j == -1:
            return True
        #j가 -1이 되지않았다면 문자열이 일치하지 않은것이므로
        #위에서 계산한 이동값만큼 인덱스에 더해준다.
        else:
            i += st
    #모든 반복동안 찾지못했다면 일치하는 부분이 없다.
    return False

#맞는 위치를 찾아 이동한다.
def find(p, v):
    #원래는 -1부터 시작하는데 처음부분은 무조건 맞지않으므로
    #-2부터 시작하여 불필요한 연산을 줄인다.
    for i in range(len(p)-2, -1, -1):
        if p[i] == v:
            return len(p) -i -1
    return len(p)

for t in range(1, int(input())+1):
    s = input()
    string = input()
    result = 0
    if pattonmatch(s, string):
        result = 1
    print("#{} {}".format(t, result))