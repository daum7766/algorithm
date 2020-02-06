#D3 5356 의석이의 세로로 말해요

T = int(input())
for t in range(T):
    line = 5
    str_list = [input() for _ in range(line)]
    print_str = ''
    max_length = 0
    for i in range(line):
        max_length = max(max_length, len(str_list[i]))
    for i in range(max_length):
        for j in range(line):
            if len(str_list[j]) > i:
                print_str += str_list[j][i]
    print("#{} {}".format(t+1, print_str))