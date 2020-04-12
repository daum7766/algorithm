#D3 1208 Flatten
#10번 반복
for l in range(1, 11):
    #덤프횟수
    dump = int(input())
    #박스 높이
    box_list = list(map(int, input().split()))
    #덤프횟수가 0이 될때까지 반복
    while dump:
        #최대 위치의 값을 1개 감소
        box_list[box_list.index(max(box_list))] -= 1
        #최소 위치의 값을 1개 증가
        box_list[box_list.index(min(box_list))] += 1
        #덤프횟수 감소
        dump -= 1
    #결과값 출력
    print("#{} {}".format(l,max(box_list) - min(box_list)))