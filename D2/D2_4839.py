#D2 4839 이진탐색
def binaryserch(p, key):
    start = 1
    end = p
    count = 0
    while start <= end:
        index = (start+end) // 2
        count += 1
        if index == key:
            return count
        elif index < key:
            start = index
        elif index > key:
            end = index
    return -1

T = int(input())
for t in range(1, T+1):
    p, a, b = map(int, input().split())
    a_c = binaryserch(p, a)
    b_c = binaryserch(p, b)
    result = ''
    if a_c < b_c:
        result = 'A'
    elif a_c > b_c : 
        result = 'B'
    else:
        result = '0'
    print("#{} {}".format(t, result))