# silver 4 수 찾기

check = {}
input()
numbers = list(map(int, input().split()))
for number in numbers:
    check[number] = True

input()
numbers = list(map(int, input().split()))

for number in numbers:
    if check.get(number, False):
        print(1)
    else:
        print(0)