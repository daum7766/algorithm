#D3 6190 정곤이의 단조 증가하는 수

#계산된 값이 단조증가인지 확인한다.
def check(number):
    temp_str = str(number)
    for k in range(len(temp_str)-1):
        if temp_str[k] > temp_str[k+1]:
            return False
    return True
T = int(input())
for t in range(1, T+1):
    N = input()
    a_list = list(map(int, input().split()))
    result = -1
    for i in range(len(a_list)):
        for j in range(i+1, len(a_list)):
            num = a_list[i]*a_list[j]
			#두수를 곱한값이 결과값보다 커야하고, 곱한값은 단조증가수여야 한다.
            if result < num and check(num):
                result = num
    print("#{} {}".format(t, result))