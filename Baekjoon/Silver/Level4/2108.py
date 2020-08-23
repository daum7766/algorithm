# silver 4 통계학

N = int(input())

numbers = [ int(input()) for _ in range(N)]
numbers.sort()
print(round(sum(numbers)/N))
print(numbers[N//2])

counting = {}
for number in numbers:
    counting[number] = counting.get(number, 0) + 1
items = list(counting.items())
items.sort(key=lambda x: -x[1])
if len(items) > 1 and items[0][1] == items[1][1]:
    print(items[1][0])
else:
    print(items[0][0])
print(numbers[-1] - numbers[0])