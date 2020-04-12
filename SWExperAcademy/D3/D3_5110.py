#D3 5110 수열 합치기

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    #첫 리스트 입력받기
    linked_list = list(map(int, input().split()))
    #리스트 하나 받았으니까 개수 -1
    for _ in range(M-1):
        #삽입할 리스트 받고
        temp = list(map(int, input().split()))
        check = True
        #반복해서 체크
        for i in range(len(linked_list)):
            #삽입할 원소보다 크다면
            if linked_list[i] > temp[0]:
                #슬라이싱을 이용하여 삽입
                linked_list[i:i] = temp
                #체크변수 변경하고
                check = False
                #반복문 탈출
                break
        #끝까지 못찾았다면 제일 뒤에 추가
        if check:
            linked_list.extend(temp)
    #뒤에 10개를 출력해야 하므로 슬라이싱 하고 뒤집기
    print_list = reversed(linked_list[len(linked_list)-10:])
    #결과 출력
    print('#{} '.format(t), end='')
    print(*print_list)
    