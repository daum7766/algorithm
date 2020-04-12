#D5 1259 금속막대

#반복횟수만큼 입력받고 반복
T = int(input())
for t in range(1, T+1):
    abc = input()
    #입력받고 공백을 기준으로 분리
    lst =list(map(int, input().split())) 
    temp = []
    result = []
    #숫나사, 암나사 가 한묶음이므로 2개씩 끊어서 넣는다.
    for i in range(0, len(lst), 2):
        temp.append((lst[i], lst[i+1]))
    #결과창에 제일앞내용을 넣는다.
    result.append(temp.pop(0))
    #인덱스 추적을 위한 변수 i
    i = 0
    #temp의 길이가 0이 될때까지 반복한다.
    while len(temp):
        #앞에 연결할수있다면 결과에 추가하고 인덱스 초기화
        if temp[i][1] == result[0][0]:
            result.insert(0, temp.pop(i))
            i = 0
        #뒤에 연결할 수 있다면 추가하고 인덱스 초기화
        elif temp[i][0] == result[len(result)-1][1]:
            result.append(temp.pop(i))
            i = 0
        #아무것도 연결못한다면 다음것을 확인
        else:
            i += 1
    #출력하기
    print("#{}".format(t), end='')
    for r in result:
        print(' ', end='')
        print(*r, end = '')
    print()
    