# silver 수 정렬하기2
import sys
N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()

for number in numbers:
    print(number)