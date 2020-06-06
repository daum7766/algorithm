# D4 3143 가장 빠른 문자열 타이핑

for t in range(int(input())):
    a,b = input().split()
    print(f'#{t+1} {len(a)-(len(b)-1)*a.count(b)}')