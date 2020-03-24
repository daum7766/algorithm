#D3 4047 영준이의 카드 카운팅
#카드 리스트 셋팅
for t in range(1, int(input())+1):
    t_str = input()
    t_lst = []
    #카드갯수
    counts = {'S': 13, 'D': 13, 'H': 13, 'C' : 13}
    #3칸씩 분리해서 저장
    for i in range(0, len(t_str), 3): t_lst.append(t_str[i:i+3])
    #겹치는게 있다면 에러 출력
    if len(set(t_lst)) != len(t_lst): print("#{} ERROR".format(t))
    #안겹치면 카드깍고 원소 출력
    else:
        for k in t_lst: counts[k[0]] -= 1
        print("#{} ".format(t), end='')
        print(*counts.values())