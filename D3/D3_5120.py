#D3 5120 암호

for t in range(1, int(input()) + 1):
    #숫자 N개, M번째칸 추가, K회 반복
    N, M, K = map(int, input().split())
    linked_lisd = list(map(int, input().split()))
    index = 0
    for i in range(K):
        index += M
        #크기가 길이를 넘어가면 길이만큼 빼준다.
        if index > len(linked_lisd):
            index -= len(linked_lisd)
        # 위치가 0일경우
        if not index :
            linked_lisd.insert(0, linked_lisd[-1] + linked_lisd[0])
        #길이 위치에 있다면 제일마지막에 추가한다.
        elif index == len(linked_lisd):
            linked_lisd.append(linked_lisd[-1] + linked_lisd[0]) 
        #평범한 경우
        else : linked_lisd.insert(index, linked_lisd[index-1] + linked_lisd[index])
    #10개가 최대이므로 끊어서 뒤집어준다.
    result = reversed(linked_lisd[-10:])
    print('#{} '.format(t), end='')
    print(*result)