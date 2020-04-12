#D2 4835 구간합
length = int(input())
for l in range(1, length+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    #누적합을 구하기
    sumnumbers = [0] * (N+1)
    for i in range(1, N+1):
        sumnumbers[i] = numbers[i-1] + sumnumbers[i-1]
    #M번째를 최댓값과 최솟값으로 설정
    minnum = maxnum = sumnumbers[M]
    #반복을 돌면서 최솟값과 최댓값 찾기
    for i in range(M, N+1):
        minnum = min(minnum, sumnumbers[i] - sumnumbers[i-M])
        maxnum = max(maxnum, sumnumbers[i] - sumnumbers[i-M])
    #결과출력
    print("#{} {}".format(l, maxnum - minnum))