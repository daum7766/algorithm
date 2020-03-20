#D4 3378 스타일리쉬 들여쓰기

for t in range(1, int(input()) + 1):
    p, q = map(int, input().split()
    p_lsit = [input() _ for in range(p)]
    q_list = [input() _ for in range(q)]
    p_count = [0 for _ in range(p)]
    RCS_list = []
    a = b = c = 0
    for temp in p_list:
        check = True
        count = 0
        for i in temp:
            if i != '.': check = False
            if check: count+=1
            elif i == '(': a += 1
            elif i == ')': a -= 1
            elif i == '{': b += 1
            elif i == '}': b -= 1
            elif i == '[': c += 1
            elif i == ']': c -= 1
        RCS_list.append([a, b, c, count])
    org = []
    for i in range(p):
        for R in range(1, 21):
            for C in range(1, 21):
                for S in range(1, 21):
                    if p == 1:
                        org.append([R, C, S])
                    elif R*RCS_list[i][3]
                        org.append([R, C, S])