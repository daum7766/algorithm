#D2 4861 회문
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst, lst2 = [], []
    #입력데이터 넣기
    for i in range(N):
        lst.append(input())
    #세로를 계산하기위해 세로데이터 넣기.
    for k in range(N):
        str_temp = ''
        for i in range(N):
            str_temp += lst[i][k]
        lst2.append(str_temp)
    result = ''
    #회문이기 때문에 뒤집어서 비교를 해본다.
    for k in range(N):
        temp, temp2 = list(lst[k]), list(lst2[k])
        temp.reverse()
        temp2.reverse()
        s_temp, s_temp2 = "".join(temp), "".join(temp2)
        #리스트안에 회문이 있다면 result에 저장한다.
        for i in range(N-M+1):
            if s_temp[i:M+i] in lst[k]:
                result = s_temp[i:M+i]
                break
            if s_temp2[i:M+i] in lst2[k]:
                result = s_temp2[i:M+i]
                break
    print("#{} {}".format(t, result))