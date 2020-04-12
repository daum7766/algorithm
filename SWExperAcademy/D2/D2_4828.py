#d2 4828 min, max
#제일큰값 과 제일작은값의 차구하기
length = int(input())
for l in range(1, length+1):
    t = input()
    n = list(map(int,input().split()))
    print("#{} {}".format(l, max(n) - min(n)))