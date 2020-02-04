#D3 4843 특별한 정렬
T = int(input())
for t in range(1, T+1):
    abc = input()
    num_list = list(map(int, input().split()))
    num_list.sort()
    result = []
    count = 0
    while count<10:
        if count & 1:
            result.append(num_list.pop(0))
        else:
            result.append(num_list.pop())
        count+=1
    print("#{} ".format(t), end='')
    print(*result)