# bronze 2 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_cards = cards[i] + cards[j] + cards[k]
            if sum_cards <= M and answer < sum_cards:
                answer = sum_cards
print(answer)