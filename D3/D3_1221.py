#D3 1221 GNS 

T = int(input())
for t in range(1, T+1):
    N = input()
    #각 개수를 저장하는 딕셔너리
    str_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    str_list = input().split()
    result = ''
    for s in str_list:
        #각각 카운팅한다.
        str_dict[s] += 1
    #각 원소가 몇개인지 나오기때문에 앞에서부터 개수만큼 생성한다.
    for key, value in str_dict.items():
        temp = ' '.join([key] * value)
        result += temp + ' '
    
    print("#{}".format(t))
    print(result[:len(result) - 1])