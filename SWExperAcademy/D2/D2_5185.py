#D2 5185 이진수

hexa_to_decimal = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15}

for t in range(int(input())):
    N, octa = input().split()
    answer = ''
    #들어온 16진수만큼 반복
    for i in octa:
        # hexa to decimal 하기
        if '0'<= i <= '9':
            temp = int(i)
        else:
            temp = hexa_to_decimal[i]
        #16진수는 2진수 4글자이므로 8을 이용함
        num = 8
        for _ in range(4):
            #비트연산해서 값이 나오면 1
            if temp & num:
                answer += '1'
            #값이 안나오면 0
            else: answer += '0'
            #비트연산하는 값을 반절 줄이기
            num >>= 1

    print('#{} {}'.format(t+1, answer))