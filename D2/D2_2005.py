#D2 2005 파스칼삼각형
T = int(input())
for t in range(1, T+1):
    length = int(input())
    pascal = [[0 for i in range(length+1)] for k in range(length+1)]
    pascal[0][1] = 1
    for i in range(1, length+1):
        for j in range(1, length+1):
            pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
    print("#{}".format(t))
    for i in range(0, length):
        print(*pascal[i][1:2+i])