pascal_triangle = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    pascal_triangle[i][0] = 1


for y in range(1, 10):
    for x in range(1, 10):
        pascal_triangle[y][x] = pascal_triangle[y-1][x] + pascal_triangle[y-1][x-1]


for t in range(int(input())):
    N = int(input())
    print('#{}'.format(t+1))
    for y in range(N):
        for x in range(y+1):
            print(pascal_triangle[y][x], end=' ')
        print()