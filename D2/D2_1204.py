#D2 1204 최빈수 구하기
t = int(input())
while t:
    #반복횟수를 감소시킴(반복문으로 처리해도 무방함)
    t -= 1
    #몇번째 케이스인지
    case = int(input())
    grade = list(map(int, input().split()))
    lst = [0]*101
    #각 자리수마다 카운팅한다.
    #숫자 1번이 나오면 1번 인덱스에 +1 이런식으로
    for g in grade:
        lst[g] += 1
    #최대값을 찾는다.
    max_num = max(list)
    #최대값과 같은값을 뒤에서부터 찾는다.
    #앞에서 부터 찾으면 정답이 틀릴 수 있다.
    for i in range(100, -1, -1):
        if max_num == lst[i]:
            print(f"#{case} {i}")
            break