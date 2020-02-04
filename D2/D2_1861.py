#D2 4861 회문
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst, lst2 = [], []
    for i in range(N):
        lst.append(input())
    for k in range(N):
        str_temp = ''
        for i in range(N):
            str_temp += lst[i][k]
        lst2.append(str_temp)
    result = ''
    for k in range(N):
        temp, temp2 = list(lst[k]), list(lst2[k])
        temp.reverse()
        temp2.reverse()
        s_temp, s_temp2 = "".join(temp), "".join(temp2)
        for i in range(N-M+1):
            if s_temp[i:M+i] in lst[k]:
                result = s_temp[i:M+i]
                break
            if s_temp2[i:M+i] in lst2[k]:
                result = s_temp2[i:M+i]
                break
    print("#{} {}".format(t, result))