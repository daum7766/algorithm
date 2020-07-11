# bronze 3 직각삼각형

while(True):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    # 위치교체
    max_num = max(a, b, c)
    if a == max_num:
        a, c = c, a
    elif b == max_num:
        b, c = c, b

    if a*a + b*b == c*c:
        print('right')
    else:
        print('wrong')