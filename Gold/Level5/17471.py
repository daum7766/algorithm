#골드5 게리멘더링
#인구수 계산하기
def caculate(first_ward, second_ward) :
    global result
    sum1, sum2 = 0, 0
    for a in first_ward:
        sum1 += Population[a]
    for b in second_ward:
        sum2 += Population[b]
    if sum1 < sum2:
        temp = sum2 - sum1
    else: 
        temp = sum1 - sum2
    return min(result, temp)

def is_check(ward, temp_check,idx):
    if temp_check[idx]:
        temp_check[idx] = False
        for k in connect[idx]:
            is_check(ward, temp_check,k-1)


#연결이 안되어있다면 True리턴
def is_not_connect(ward):
    temp_check = [True for _ in range(N)]
    is_check(ward, temp_check,ward[0])
    for w in ward:
        if temp_check[w]:
            return True
    return False


#두개의 선거구로 나누는 경우의수를 구한다.
def dfs(idx):
    if idx == N:
        global result
        first_ward = []
        second_ward = []
        #체크되어있는 값에따라 선거구를 나눈다.
        for i in range(N):
            if check[i]: first_ward.append(i)
            else: second_ward.append(i)
        #선거구중 하나라도 0이라면 리턴
        if not first_ward or not second_ward:
            return
        #선거구들이 연결되어 있지 않다면 리턴
        if is_not_connect(first_ward) or is_not_connect(second_ward):
            return
        #두개의 선거구들 차이를 계산한다.
        result = caculate(first_ward, second_ward)
        return
    check[idx] = True
    dfs(idx+1)
    check[idx] = False
    dfs(idx+1)

#연결안된 선거구가 1개이상일때 동작
def zero_check():
    global sum1, sum2
    #연결이 안되어있는 선거구가 2개이상이라면
    #연결할수 없으므로 -1을 리턴한다.
    if zero_count > 1:
        print(-1)
        return False
    #연결되어있지 않은 선거구가 1개라면
    #연결되어있지 않은 선거구1개와 나머지로 구분된다.
    if zero_count == 1:
        for i in range(N):
            if i != zero_index:
                sum1 += Population[i]
        sum2 = Population[zero_index]
        #두개의 선거구 차이만큼 출력한다.
        print(abs(sum1 - sum2))
        #뒤에 내용이 동작하지 않도록 False를 반환한다.
        return False
    #위의 조건에 걸리지 않았다면 True를 리턴한다.
    return True



N = int(input())
Population = list(map(int, input().split()))
connect = []

#연결이 안된섬의 개수 카운트
zero_count = 0
zero_index = 0
result = 1000
for i in range(N):
    connect.append(list(map(int, input().split())))
    if not connect[i].pop(0):
        zero_count += 1
        zero_index = i

#선거구를 나눌수 있을때 동작
if zero_check():
    #경우의 수를 찾기위해 사용
    check = [False for i in range(N)]
    #0번 자치구부터 N-1 자치구까지 경의우수 탐색
    for i in range(N):
        dfs(0)
    #result가 바뀌지 않았다면 연결이 불가능하다.
    if result == 1000:
        result = -1
    #결과값을 출력한다.
    print(result)