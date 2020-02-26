#D3 1225 암호생성기
T = 10
for t in range(1, T+1):
    input()
    password = list(map(int, input().split()))
    i = 1
    while True:
        a = password.pop(0) - i
        #0보다 작아지면 0으로 바꿔준다.
        if a < 0: a = 0
        password.append(a)
        #마지막 숫자가 0이 되었다면 그암호가 되므로 반복문 종료
        if a <= 0: break
        i += 1
        #한사이클은 5까지이므로 숫자 갱신
        if i > 5: i = 1
    print('#{} '.format(t), end='')
    print(*password)