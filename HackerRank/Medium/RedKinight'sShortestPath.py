from collections import deque

dq = deque()

n = int(input())
s_y, s_x, e_y, e_x = map(int, input().split())
# 우선순위 순서대로 넣어주기
move = [(-2, -1, 'UL'), (-2, 1,'UR'), (0, 2, 'R'), (2, 1, 'LR'), (2, -1,'LL'), (0, -2,'L')]
# 시작위치와 이동한 순서
dq.append((s_y, s_x, []))
# 정답 리스트
answer = []
# 중복방지용
check_dict = {(s_y, s_x): True}
# 큐에 데이터가 남아있거나 answer가 없는동안만 반복
while len(dq) and not answer:
    # 데이터를 꺼내서
    y, x, _list = dq.popleft()
    # 이동을 시켜본다.
    for _y, _x, command in move:
        dy, dx = y + _y, x + _x
        # 맵을 벗어나지 않았다면
        if 0 <= dy < n and 0 <= dx < n:
            # 이전에 간 장소인지 체크한다. 갔다면 다른곳으로
            if check_dict.get((dy, dx), False):
                continue
            # 방문체크 해주고
            check_dict[(dy, dx)] = True
            # 목표점이라면 결과저장하고 반복문 종료
            if dy == e_y and dx == e_x:
                _list.append(command)
                answer = _list
                break
            # 목표가 아니라면 경로 추가하기
            dq.append((dy, dx, _list[:]+[command]))
# 정답이 나왔다면 결과출력
if answer:
    print(len(answer))
    print(*answer)
# 이동할 수 있는 모든 거리를 이동했는데도 불구하고 안나왔다면 불가능 표시
else:
    print('Impossible')