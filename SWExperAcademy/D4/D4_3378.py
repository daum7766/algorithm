#D4 3378 스타일리쉬 들여쓰기

#괄호 개수 세는함수
def A_F(code, l):
    ab = cd = ef = 0
    for i in range(0, l):
        for j in range(len(code[i])):
            if code[i][j] == '(' : ab += 1
            elif code[i][j] == ')' : ab -= 1
            elif code[i][j] == '{' : cd += 1
            elif code[i][j] == '}' : cd -= 1
            elif code[i][j] == '[' : ef += 1
            elif code[i][j] == ']' : ef -= 1
        af.append((ab, cd, ef))

#조합 찾는 함수
def RCS(af, indenp, p):
    org = []
    ab, cd, ef = af[0]
    #처음 줄의 조합을 찾는다.
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                if p == 1:
                    org,append((R, C, S))
                elif R*ab + C*cd + S*ef == indenp[1]:
                    org.append((R,C,S))

    #경우의 수와 맞는 조합을 찾는다.
    for i in range(2, p):
        ab, cd ,ef = af[i-1]
        dest = []
        for R, C, S in org:
            if R*ab + C*cd + S*ef == indenp[i]:
                dest.append((R,C,S))
        org = dest
    return org


for t in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    indenp = [0 for _ in range(p)]
    p_code = [input() for _ in range(p)]
    q_code = [input() for _ in range(q)]
    af = []
    A_F(p_code, p)

    #점의 개수 새기
    for i in range(p):
        count = 0
        while p_code[i][count] == '.':
            count += 1
        indenp[i] = count
    #가능한 조합 찾고
    rcs = RCS(af, indenp, p)
    af = []
    A_F(q_code, q)
    indenq = [0 for _ in range(q)]

    #위에서 구한 값으로 결과 구하기
    for i in range(1, q):
        ab, cd, ef = af[i-1]
        if rcs:
            R, C, S = rcs[0]
            ans = R*ab + C*cd + S*ef
            for x in rcs[1:]:
                R, C, S = x
                if R*ab + C*cd + S*ef != ans:
                    indenq[i] = -1
                    break
            if indenp[i] != -1:
                indenq[i] = ans
            else:
                indenq[i] = -1
                break
    print('#{}'.format(t), end=' ')
    print(*indenq)