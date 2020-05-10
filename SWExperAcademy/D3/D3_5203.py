#D3 5203 베이비진 게임

#우승자가 나왔는지 체크
def card_check(number, index):
    global answer
    #플레이어 캐스팅하기
    if number & 1:
        player = player1
    else:
        player = player2
    #카드가 3장이라면
    if  player[index] == 3 :
        answer = number
    #카드가 8보다 작다면 자신기준으로 우측확인
    if index < 8 and player[index] and player[index+1] and player[index+2]:
        answer = number
    #카드가 1보다 크다면 자신기준으로 좌측확인
    if index > 1 and player[index] and player[index-1] and player[index-2]:
        answer = number
    #양쪽으로 1개씩 볼수있다면 자신기준으로 양쪽확인
    if 0 < index < 9 and player[index-1] and player[index] and player[index+1]:
        answer = number

for t in range(int(input())):
    answer = 0
    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    card_list = list(map(int, input().split()))
    for i in range(12):
        #2번 유저라면
        if i & 1:
            #카드얻은거 표시해주고
            player2[card_list[i]] += 1
            #체크
            card_check(2, card_list[i])
        # 1번 유저라면
        else:
            #카드얻은거 표시해주고
            player1[card_list[i]] += 1
            체크
            card_check(1, card_list[i])
        #우승자가 정해졌다면 반복문 중지
        if answer: break
    print('#{} {}'.format(t+1, answer))