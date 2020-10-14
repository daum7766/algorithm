# Silver 3 피보나치 함수
def fibonacci(n):
    if n in fibo:
        return fibo[n]
    f1 = fibonacci(n-1) 
    f2 = fibonacci(n-2)
    fibo[n] = (f1[0] + f2[0], f1[1] + f2[1])
    return fibo[n]


fibo = { 0: (1, 0), 1:(0, 1) }
for i in range(int(input())):
    n = int(input())
    answer = fibonacci(n)
    print('{} {}'.format(answer[0], answer[1]))
