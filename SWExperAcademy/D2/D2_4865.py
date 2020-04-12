#D2 4865 글자수세기
T = int(input())
for t in range(1, T+1):
    lst = []
    for i in range(2):
        lst.append(list(input()))
    dic_t = {}
    for s in lst[1]:
        if s in lst[0]:
            dic_t[s] = dic_t.get(s, 0) + 1
    print("#{} {}".format(t, max(list(dic_t.values()))))