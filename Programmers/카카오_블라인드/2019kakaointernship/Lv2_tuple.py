def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.split('}')
    for i in range(len(s)-1, -1, -1):
        if s[i] == '':
            s.pop(i)
        else:
            s[i] = s[i].split(',')
            if i:
                s[i].pop(0)
            s[i] = list(map(int, s[i]))
    s = sorted(s, key=len)
    for i in s:
        for j in i:
            if dic.get(j, -1) == -1:
                answer.append(j)
                dic[j] = 1
    return answer


s = '{{1,2,3},{2,1},{1,2,4,3},{2}}'
print(solution(s))