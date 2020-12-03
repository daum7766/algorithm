# D2 4866 괄호검사

match_dict = {'}': '{', ')': '('}

def solution(user_input):
    arr = []
    for s in user_input:
        if s == '(' or s == '{':
           arr.append(s)
        elif s == ')' or s == '}':
            if len(arr) == 0 or arr[len(arr) - 1] != match_dict[s]:
                return 0
            arr.pop()
    if len(arr) != 0:
        return 0

    return 1


for t in range(int(input())):
    print('#{} {}'.format(t+1, solution(input())))