# silver 5 최대공약수와 최소공배수

# 유클리드 알고리즘

# 최대공약수
def gcd(a, b):
    while b != 0:
       a, b = b, a % b
    return a

def lcm(a, b, c):
    return a * b // c

a, b = map(int, input().split())

greatest_common_divisor = gcd(a, b)
least_common_multiple = lcm(a, b, greatest_common_divisor)
print(greatest_common_divisor)
print(least_common_multiple)