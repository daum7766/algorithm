#D3 4522 세상의 모든 팰린드롬

for t in range(1, int(input()) + 1):
    string = input()
    answer = 'Exist'
    length = len(string)
    for i in range(length//2):
        if string[i] != string[length - 1 - i ] and string[i] != '?' and string[length - 1 - i ] !='?':
            answer = 'Not exist'
            break
    print('#{} {}'.format(t, answer))