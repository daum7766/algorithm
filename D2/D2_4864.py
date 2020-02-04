#D2 4864 문자열 비교
T = int(input())
for t in range(1, T+1):
    s = input()
    string = input()
    result = 0
    if s in string:
        result = 1
    print("#{} {}".format(t, result))