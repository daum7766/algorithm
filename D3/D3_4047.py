#D3 4047 영준이의 카드 카운팅
#카드 리스트 셋팅

import sys
sys.stdin = open('sample_input.txt', 'r')

def solution(t):
    t_str = input()
    t_lst = []
    cards = {'S': [True for i in range(13)], 'D': [True for i in range(13)], 'H': [True for i in range(13)], 'C' : [True for i in range(13)]}
    counts = {'S': 13, 'D': 13, 'H': 13, 'C' : 13}
    for i in range(0, len(t_str), 3):
        t_lst.append(t_str[i:i+3])
    result = ''
    for lst in t_lst:
        if cards[lst[0]][int(lst[1:3])-1]:
            cards[lst[0]][int(lst[1:3])-1] = False
            counts[lst[0]] -= 1
        else: result = 'ERROR'
    print('#{} '.format(t), end='')
    if result: print(result)
    else : print(*counts.values())

def solution2(t):
    t_str = input()
    t_lst = []
    counts = {'S': 13, 'D': 13, 'H': 13, 'C' : 13}
    for i in range(0, len(t_str), 3): 
        t_lst.append(t_str[i:i+3])
        
    if len(set(t_lst)) != len(t_lst): print("#{} ERROR".format(t))
    else:
        for k in t_lst: counts[k[0]] -= 1
        print("#{} ".format(t), end='')
        print(*counts.values())

T = int(input())
for t in range(1, T+1):
    t_str = input()[::3]
    print(t_str)
    #solution2(t)