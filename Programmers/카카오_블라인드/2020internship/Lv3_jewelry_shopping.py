def bound_check(answer, start, i):
    a = i - start
    if answer[1] - answer[0] > a:
        answer[0], answer[1] = start, i

def solution(gems):
    gems_list = list(set(gems))
    gems_size = len(gems_list)
    gems_dict = {}
    length = len(gems)

    for i in gems_list:
        gems_dict[i] = 0
    
    answer = [0, length-1]
    start, end, gems_count = 0, 0, 0
    
    while start < length and end < length:
        # 지금까지 없었던 보석이라면
        if gems_dict[gems[end]] == 0:
            gems_count += 1
        # 카운팅 개수 추가
        gems_dict[gems[end]] += 1
        # 모든 보석이 포함되었다면
        if gems_count == gems_size:
            bound_check(answer, start, end)
            # 앞에서 땡기기
            while gems_count == gems_size:
                gems_dict[gems[start]] -= 1
                if gems_dict[gems[start]] == 0:
                    gems_count -= 1
                    bound_check(answer, start, end)
                start += 1
        end += 1
    answer[0] += 1
    answer[1] += 1
    return answer


if __name__ == "__main__":
    gems_list = [
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
        ["AA", "AB", "AC", "AA", "AC"],
        ["XYZ", "XYZ", "XYZ"],
        ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
        ['DIA', 'EM', 'EM', 'RUB', 'DIA']
        ]
    result_list = [[3, 7], 	[1, 3], [1, 1], [1, 5], [3, 5]]

    length = len(result_list)
    for i in range(length):
        answer = solution(gems_list[i])
        if answer == result_list[i]:
            print('{}번 정답'.format(i+1))
        else:
            print('{}번 실패'.format(i+1))
            print('{} != {}'.format(answer, result_list[i]))