def solution(s):
    answer = len(s)
    # 1개짜리부터 길이의 반절까지 분절하여 체크
    for i in range(1, (len(s)//2)+1):
        temp_len = len(s)
        j = 0
        # 길이를 벗어날때까지 반복
        while j+i <= len(s):
            count = 0
            # 이전꺼를 기준으로 슬라이싱해서 문자열 비교
            for k in range(j+i, len(s), i):
                if k+i > len(s):
                    break
                if s[j:j+i] == s[k:k+i]:
                    count += 1
                else:
                    break
            # 카운트 된만큼 감소
            if count:
                # 10개면 2자리, 100개면 3자리가 추가되어야 함
                temp_len += len(str(count+1))
                temp_len -= count*i
                # 줄인 길이만큼 인덱스 위치조절
                j += count*i
            j += i
        # 현재 길이가 더 짧다면 갱신
        if answer > temp_len:
            answer = temp_len

    return answer


if __name__ == "__main__":
    s_list = [
        "aabbaccc",
        "ababcdcdababcdcd",
        "abcabcdede",
        "abcabcabcabcdededededede",
        "xababcdcdababcdcd",
        "xxxxxxxxxxyyy",
    ]

result_list = [
        7, 
        9, 
        8, 
        14, 
        17,
        5,
    ]

for i in range(len(result_list)):
    answer = solution(s_list[i])
    if answer == result_list[i]:
        print('{}번 정답'.format(i+1))
    else:
        print('{}번 실패 {} != {}'.format(i+1, answer, result_list[i]))