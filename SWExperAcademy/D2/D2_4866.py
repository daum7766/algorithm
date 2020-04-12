#D2 4866 괄호검사
class Stack:
    #자료를 저장할 리스트 생성
    def __init__(self):
        self.data = []
    
    #들어온 데이터를 리스트에 추가
    def push(self, data):
        self.data.append(data)
    #들어온 데이터를 뒤에서부터 삭제
    def pop(self):
        return self.data.pop()
    #현재 스택의 데이터 개수를 출력
    def length(self):
        return len(self.data)
    #현재 스택이 비어있는지 검사
    def empty(self):
        if len(self.data):
            return False
        else:
            return True

t_dict = {'}' : '{' , ')' : '('}

def check(abc):
    for a in abc:
        #여는것이면 스택에 추가
        if a == '(' or a == '{':
            stack.push(a)
        #닫는괄호라면 스택의 길이를 확인하고 짝이 맞는지 확인한다.
        #비어있거나 작이안맞으면 0을 리턴한다.
        elif a == ')' or a == '}' :
            if stack.empty() or t_dict[a] != stack.pop():
                return 0
    #모든 반복이 끝났고 스택이 비어있다면 1을 리턴한다.
    if stack.empty():  return 1
    #비어있지 않다면 여는괄호가 더많으므로 0을 리턴한다.
    else:  return 0


T = int(input())
for t in range(1, T+1):
    stack = Stack()
    print('#{} {}'.format(t, check(input())))