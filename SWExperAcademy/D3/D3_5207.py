#D3 5207 이진탐색

for t in range(int(input())):
    answer = 0
    N, M = map(int, input().split())
    # 이분탐색은 정렬을 기본조건으로 한다.
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for b in B:
        # 중간을 탐색하기 때문에 최소점과 최대점을 잡아준다.
        min_idx = 0
        max_idx = N - 1
        # 왼쪽으로 갔는지 오른쪽으로 갔는지 체크하기 위한 용도
        flag = 0
        # 탐색범위가 같아지거나 엇갈릴때까지 반복한다.
        while min_idx <= max_idx:
            # 중간지점의 위치를 구한다.
            avg_idx = (min_idx+max_idx)//2
            # 중간지점의 값이 정답이라면 answer를 늘리고 반복문을 중지한다.
            if A[avg_idx] == b:
                answer += 1
                break
            # 선택한 인덱스 값이 찾는값보다 크다면
            elif A[avg_idx] > b:
                # 선택한 인덱스 위쪽은 필요없으므로 최대 인덱스 위치를 수정한다.
                max_idx = avg_idx - 1
                # 이전에도 왼쪽을 선택했다면 중지
                if flag == 1: break
                # 왼쪽으로 갔다고 표시한다.
                flag = 1
            else:
                # 반대의 상황이라면 최소값을 바꿔준다.
                min_idx = avg_idx + 1
                # 이전에 오른쪽으로 갔다면 중지
                if flag == -1: break
                # 오른쪽으로 갔다고 표시한다.
                flag = -1
    print('#{} {}'.format(t+1, answer)) 