#D4 4366 정식이의 은행업무

#2진수와 3진수를 비교
def equleCheck(a, b):
    num_a = 0
    num_b = 0
    k = 0
    for i in range(len(a)-1, -1, -1):
        num_a += int(a[i])*(2**k)
        k+=1
    k = 0
    for i in range(len(b)-1, -1, -1):
        num_b += int(b[i])*(3**k)
        k+=1
    if num_a == num_b:
        return True, num_a
    return False, num_a

T = int(input())
for t in range(1, T + 1):
    num_2 = list(input())
    num_3 = list(input())
    list1 = []
    list2 = []
    #2진수가 틀린 경우의수 찾기
    for i in range(len(num_2)):
        temp = num_2[:]
        if temp[i] == '0':  temp[i] = '1'
        else:   temp[i] = '0'
        list1.append(''.join(temp))
    #진수가 틀린 경우의 수 찾기
    for i in range(len(num_3)):
        temp = num_3[:]
        if temp[i] == '0':
            temp[i] = '1'
            list2.append(''.join(temp))
            temp[i] = '2'
            list2.append(''.join(temp))
        elif temp[i] == '1':
            temp[i] = '0'
            list2.append(''.join(temp))
            temp[i] = '2'
            list2.append(''.join(temp))
        else:
            temp[i] = '0'
            list2.append(''.join(temp))
            temp[i] = '1'
            list2.append(''.join(temp))

    result = 0
    #경우의 수를 각각 비교하면서 찾기
    for a in list1:
        for b in list2:
            check, result = equleCheck(a, b)
            if check:
                break
        else:
            continue
        break
    print('#{} {}'.format(t, result))