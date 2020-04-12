# 4008 숫자 만들기
modul = ['+', '-', '*', '/']

def cal(a, b, _modul):
    if _modul == 0:
        return a + b
    elif _modul == 1:
        return a - b
    elif _modul == 2:
        return a * b
    #//를 하게되면 내림으로 되기때문에 버림으로 처리
    else : return int(a / b)

def dfs(idx, _ans):
    if idx >= N:
        global max_n, min_n
        if _ans > max_n:
            max_n = _ans
        if _ans < min_n:
            min_n = _ans
        return
    for i in range(4):
        if moduls[i]:
            moduls[i] -= 1
            dfs(idx+1, cal(_ans, numbers[idx+1], i))
            moduls[i] += 1


T = int(input())
for t in range(1, T+1):
    N = int(input()) - 1
    moduls = list(map(int, input().split()))
    max_n = -987654321
    min_n = 987654321
    numbers = list(map(int, input().split()))
    dfs(0, numbers[0])
    print('#{} {}'.format(t, max_n - min_n))