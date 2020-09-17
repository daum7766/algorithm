# silver2 소수 구하기

start, end = map(int, input().split())

eratosthenes = [ True for _ in range(end+1)]
eratosthenes[1] = False
for i in range(2, end+1):
    if i >= start and eratosthenes[i]:
        print(i)
    for j in range(i*2, end+1, i):
        eratosthenes[j] = False
