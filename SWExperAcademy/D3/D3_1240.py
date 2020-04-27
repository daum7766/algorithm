#D3 1240 단순 2진 암호코드
to_num = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

for t in range(int(input())):
    answer = 0
    #가로 세로 받고
    N, M = map(int, input().split())
    #배열 받고
    array = [input() for _ in range(N)]
    # 몇번 끊어서 할지
    for i in range(N-5):
        temp_str = ''
        if answer: break
        for j in range(M-1, -1, -1):
            #정답이 이미 나와있다면 멈추기
            if answer: break
            #남은 길이가 55자 이하라면 멈추기
            if M-55 < 0: break
            # 숫자가 1이 나올때까지 찾는다
            if array[i][j] == '0': continue
            #7*8 = 56글자이므로 56글자로 끊는다.
            temp_array = array[i][j-55: j+1]
            #암호는 8글자로 되어있으므로 8번 반복
            for z in range(8):
                temp_num = to_num.get(temp_array[z*7:(z+1)*7], -1)
                #정상적인 값이 아니라면 멈추기
                if temp_num == -1: break
                else:
                    #위에서 통과했다면 임시로 저장하기
                    temp_str += temp_num
                    #길이가 8이 되었다면
                    if len(temp_str) == 8:
                        #밑에 4개가 자신과 같은지 확인한다.
                        for k in range(4):
                            if temp_array != array[i+k+1][j-55: j+1]: break
                        #브레이크가 걸리지 않았을때
                        else:
                            #결과 저장용 임시 변수
                            check_num = 0
                            #홀수자리만 더하기(여기서는 0부터 시작해서 짝수)
                            for k in range(0, 7, 2): check_num += int(temp_str[k])
                            #값 3배 해주기
                            check_num *= 3
                            #짝수 자리만 더하기
                            for k in range(1, 8, 2):check_num += int(temp_str[k])
                            # 10 으로 나눠지는지 확인
                            if not check_num % 10:
                                for k in range(8):
                                    answer += int(temp_str[k])
                                break
        
    print('#{} {}'.format(t+1, answer))