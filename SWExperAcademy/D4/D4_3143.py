# D4 3143 가장 빠른 문자열 타이핑

for t in range(1, int(input())+1):
    a,b = input().split()
    print(f'#{t} {len(a)-(len(b)-1)*a.count(b)}')