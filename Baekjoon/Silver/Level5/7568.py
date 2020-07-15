# silver 5 덩치

N = int(input())

bulks = []
answer = []
for _ in range(N):
    x, y = map(int, input().split())
    bulks.append([x, y, 1])

for i in range(len(bulks)):
    for j in range(len(bulks)):
        if i != j and bulks[i][0] < bulks[j][0] and bulks[i][1] < bulks[j][1]:
            bulks[i][2] += 1


for bluk in bulks:
    answer.append(bluk[2])

print(*answer)