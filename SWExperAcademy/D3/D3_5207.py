#D3 5207 이진탐색

for t in range(int(input())):
    answer = 0
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for b in B:
        min_idx = 0
        max_idx = N - 1
        flag = 0
        while min_idx <= max_idx:
            avg_idx = (min_idx+max_idx)//2
            if A[avg_idx] == b:
                answer += 1
                break
            elif A[avg_idx] > b:
                max_idx = avg_idx - 1
                if flag == 1: break
                flag = 1
            else:
                min_idx = avg_idx + 1
                if flag == -1: break
                flag = -1
    print('#{} {}'.format(t+1, answer))