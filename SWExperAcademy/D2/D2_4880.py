#4880 D2 토너먼트 카드게임

# 1 : 가위,  2 : 바위,  3 : 보
#같은카드일시 작은번호가 승자

#가위바위보 승자찾기
#이기거나 비기면 작은번호가 승리
def whoWin(a, b):
    answer = (a - b) % 3
    # 0 비김 1 승리 2 패배(a 기준)
    if answer == 1 or answer == 0:
        return True
    return False

#그룹을 계속쪼개서 계산한다.
#작은번호를 a 에 넣고 계산한다.
def battle(group):
    if len(group) < 2:
        return group[0]
    a_group, b_group = [], []
    j = len(group)
    for i in range(j):
        if i <= (j-1)//2:
            a_group.append(group[i])
        else :  b_group.append(group[i])
    a = battle(a_group)
    b = battle(b_group)
    if whoWin(a[0], b[0]): return a
    else: return b


T = int(input())
for t in range(1, T+1):
    N = int(input())
    player = list(map(int, input().split()))
    player = [(i, idx) for idx, i in enumerate(player)]
    result = battle(player)
    print('#{} {}'.format(t, result[1]+1))