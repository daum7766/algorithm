def solution(N, stages):
    answer = []
    users = [ 0 for _ in range(N+1) ]
    failed_percent = []
    size = len(stages)
    for i in stages:
        users[i-1] += 1
    for i in range(N):
        if size == 0 or users[i] == 0 :
            failed_percent.append((i+1, 0))
        else:
            failed_percent.append((i+1, users[i]/size))
            size -= users[i]
    failed_percent.sort(key = lambda x : (-x[1], x[0]))
    for i, j in failed_percent:
        answer.append(i)
    return answer


if __name__ == "__main__":
    N_list = [5, 4, 2, 4]
    stages_list = [
        [2, 1, 2, 6, 2, 4, 3, 3], 
        [4, 4, 4, 4, 4],
        [2, 2, 3],
        [2, 2, 2, 2, 2]
    ]
    answer_list = [
        [3, 4, 2, 1, 5],
        [4, 1, 2, 3],
        [2, 1],
        [2, 1, 3, 4]
    ]
    for i in range(4):
        if solution(N_list[i], stages_list[i]) == answer_list[i]:
            print('{}번 정답'.format(i+1))
        else:
            print('{}번 틀림'.format(i+1))
    