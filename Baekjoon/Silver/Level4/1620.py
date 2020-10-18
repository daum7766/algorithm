# Silver 4 나는야 포켓몬 마스터 이다솜

N, M = map(int, input().split())

poketmon = {}

for i in range(N):
    name = input()
    poketmon[name] = i + 1
    poketmon[str(i+1)] = name

for _ in range(M):
    print(poketmon[input()])