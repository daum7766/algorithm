#D3 1216 회문2
def check(a):
    l = len(a)
    for i in range(l//2):
        if a[i] != a[l-i-1]:
            return False
    return True

T = 10
for t in range(1, T+1):
    input()
    length = 100
    map_list = []
    map_list2 = []
    N = 100
    for i in range(N):
        map_list.append(input())
    for i in range(N):
        str_temp = ''
        for k in range(N):
            str_temp += map_list[k][i]
        map_list2.append(str_temp)
    result = 0
    for t_len in range(length, 0, -1):
        if result >= t_len:
            break
        for i in range(N):
            if result == t_len:
                break
            for j in range(N-t_len+1):
                if check(map_list[i][j:j+t_len]) or check(map_list2[i][j:j+t_len]):
                    result = t_len
                    break
            
    print("#{} {}".format(t, result))