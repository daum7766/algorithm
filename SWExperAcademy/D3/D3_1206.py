#D3 1206 view 조망권
#10회 반복
for l in range(1, 11):
    r = int(input())
    b = list(map(int, input().split()))
    c = 0
    #왼쪽2칸과 오른쪽 2칸은 비어있음
    for i in range(2, r-2):
        #왼쪽과 오른쪽 빌딩중에서 제일 빌딩을 찾음
        m = max(b[i+1], b[i+2], b[i-1], b[i-2])
        # 현재 빌딩과 제일큰빌딩을 비교할때 현재빌딩보다 작다면 차 만큼 결과에 더해주기
        if b[i] - m > 0 : c += b[i] - m
    print("#{} {}".format(l, c))