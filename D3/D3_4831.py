from queue import PriorityQueue
import copy
#D3 4831 전기버스
#우선순위 큐를 이용한 문제풀이
length = int(input())
for l in range(1, length+1):
    # n = 종점 정류장, k = 최대이동거리, m = 충전가능 정류장 
    temp = list(map(int, input().split()))
    #충전할 수 있는 정류장
    ch = list(map(int, input().split()))
    #우선순위 큐를 이용하기 위해 깊은복사
    ch_list = copy.deepcopy(ch)
    #현재 거리와 충전횟수 저장
    current = result = 0
    #충전할수 있는 정류장만큼 반복
    #그냥 반복도 가능하지만 최대수는 이만큼
    for c in ch:
        #우선순위 큐를 선언
        pq = PriorityQueue()
        #현재거리에 최대이동거리만큼 더해주기
        current += temp[0]
        #더해진거리가 최종 종착역을 넘어갔다면 정지
        if current >= temp[1]:  break
        #충전가능한 정류장이 남을때까지 반복
        while len(ch_list):
            #현재거리가 충전가능한 정류장을 지나갔다면
            if ch_list[0] <= current:
                #우선순위 큐에 넣어주고 리스트에서 빼기
                pq.put(-ch_list[0])
                ch_list.pop(0)
            #충전가능한 정류장이 없다면 반복문 나가기
            else: break
        #우선순위 큐가비어있다면
        if pq.empty():
            #충전가능한 정류장이 없는것이므로 결과를 0으로 넣어주고 반복문을 나간다
            result = 0
            break
        #위의 조건에 걸리지 않았다면 충전가능한 마지막정류장을 현재거리로 넣어준다.
        current = -pq.get()
        #충전을 했으므로 충전횟수를 증가시킨다
        result += 1
    #결과값을 출력한다.
    print("#{} {}".format(l, result))