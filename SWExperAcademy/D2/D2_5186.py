#D2 5186 이진수2

for t in range(int(input())):
    #결과 저장 변수
    answer = ''
    #계산해야 하는 숫자 받기
    number = float(input())
    #나누기 위한 값
    sub_num = 1
    #최대 12자리까지 출력
    for _ in range(12):
        #진행이 될수록 크기는 반절이 된다.
        sub_num *= 0.5
        #값을 빼보았을때 0보다 크다면 뺀고 결과출력
        if number - sub_num >= 0:
            answer += '1'
            number -= sub_num
            #숫자가 나눠떨어졌다면 반복문 종료
            if not number:
                break
        else:
            #계산이 안된다면 0추가
            answer += '0'
    #모든 반복문이 끝났는데 값이 남아있다면 overflow 넣기
    if number: answer = 'overflow'
    print('#{} {}'.format(t+1, answer))