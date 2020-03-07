# 1952 수영장

T = int(input())
for t in range(1, T+1):
    #일, 1달, 3달, 1년 이용권
    price_list = list(map(int, input().split()))
    #월별 이용날
    month_list = list(map(int, input().split()))
    #결과 저장 변수 그 달의 최저값을 저장한다.
    result_list = [0] * 13
    for n in range(1, 13):
        #가격을 저장할 임시변수
        a = [0, 0, 987654321, 987654321]
        #일권으로 계산했을때, 전달비용 + 참여일수 * 일비
        a[0] = result_list[n-1] + month_list[n-1] * price_list[0]
        #1달권으로 계산했을때, 전달비용 + 1달권 비용
        a[1] = result_list[n-1] + price_list[1]
        #3달권으로 계산했을때, 3달 전비용 + 3달권비용
        if n >= 3:   a[2] = result_list[n-3] + price_list[2]
        #1년권으로 계산했을때, 1년비용
        if n >= 12:   a[3] = price_list[3]
        #현시점에서 제일 적은 비용의 값을 넣는다.
        result_list[n] = min(a)
    print('#{} {}'.format(t, result_list[12]))