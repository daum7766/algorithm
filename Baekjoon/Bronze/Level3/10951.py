import sys

#B3 10951 A+B - 4

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)