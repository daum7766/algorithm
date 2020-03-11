#D3 4676 늘어지는 소리

for t in range(1, int(input()) + 1):
    #편집을 쉽게 하기위해 리스트로 변환한다.
    string = list(input())
    #하이픈의 개수를 입력받는다.
    H = int(input())
    #큰수부터 넣어 인덱스상에 문제가 없도록 한다.
    pos = sorted(list(map(int, input().split())), reverse=True)
    #큰쪽 인덱스부터 처리한다.
    for idx in pos:
        string.insert(idx, '-')
    print('#{} {}'.format(t, ''.join(string)))