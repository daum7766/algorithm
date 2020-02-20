#D2 4874 Forth
T = int(input())

def cal(t1, t, t2):
    t1 = int(t1)
    t2 = int(t2)
    if t == '+':
        return t1 + t2
    elif t == '-':
        return t1 - t2
    elif t == '*':
        return t1 * t2
    elif t == '/':
        return t1 // t2

for a in range(1, T+1):
    stack_result = input().split()
    stack_result.pop()
    stack_operater = []
    #후위연산 스택을 순회하면서 확인
    for t in stack_result:
        #숫자라면 임시저장
        if '0' <= t <= '9':
            stack_operater.append(t)
        else:
            if len(stack_operater) < 2:
                print('#{} error'.format(a))
                break
            #연산자면 2개를 꺼내서 계산한다.
            t2 = stack_operater.pop()
            t1 = stack_operater.pop()
            stack_operater.append(cal(t1, t, t2))
    else:
        #결과값 출력
        if len(stack_operater) != 1:
            print('#{} error'.format(a))
            continue
        print('#{} {}'.format(a, stack_operater[0]))