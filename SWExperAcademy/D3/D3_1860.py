# D3 1860 진기의 최고급 붕어빵
possible = 'Possible'
improssible = "Impossible"


def solution(N, M, K, peoples):
    peoples.sort()
    for i in range(N):
        total_bread = (peoples[i] // M) * K
        if total_bread < i + 1:
            return improssible
    return possible


for t in range(int(input())):
    N, M, K = map(int, input().split())
    peoples = list(map(int, input().split()))
    answer = solution(N, M, K, peoples)
    print('#{} {}'.format(t+1, answer))