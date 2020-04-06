#D3 5108 숫자 추가

for t in range(1, int(input()) + 1):
    #N 수열길이, M 추가횟수, L 출력 인덱스
    N, M, L = map(int, input().split())
    linked_list = input().split()
    #삽입할 숫자 입력받기
    for _ in range(M):
        index, number = map(int, input().split())
        #insert함수를 이용하여 추가
        linked_list.insert(index, number)
    print('#{} {}'.format(t, linked_list[L]))