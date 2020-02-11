# D3 1215 회문1
def check(a):
    l = len(a)
    for i in range(l//2):
        if a[i] != a[l-i-1]:
            return False
    return True

T = 10
for t in range(1, T+1):
    length = int(input())
    map_list = []
    map_list2 = []
    N = 8
    for i in range(N):
        map_list.append(input())
    for i in range(N):
        str_temp = ''
        for k in range(N):
            str_temp += map_list[k][i]
        map_list2.append(str_temp)
    result = 0
    for i in range(N):
        for j in range(N-length+1):
            if check(map_list[i][j:j+length]):
                result += 1
            if check(map_list2[i][j:j+length]):
                result += 1
            
    print("#{} {}".format(t, result))