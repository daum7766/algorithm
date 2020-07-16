# silver 4 요세푸스 문제 0

N, K = map(int, input().split())

peoples = [i for i in range(1, N+1)]

answer = []
K -= 1
index = 0
while peoples:
    index += K
    if index >= len(peoples):
        index %= len(peoples)
    answer.append(peoples.pop(index))

result = ', '.join(map(str, answer))

print('<{}>'.format(result))