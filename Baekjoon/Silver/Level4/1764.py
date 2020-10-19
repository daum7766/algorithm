# Silver 4 듣보잡

N, M = map(int, input().split())

a = set()
b = set()

for _ in range(N):
    a.add(input())

for _ in range(M):
    b.add(input())

c = list(a & b)
c.sort()
print(len(c))
for name in c:
    print(name)