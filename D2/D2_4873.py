#D2 4873 반복문자 지우기
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
    def top(self):
        return self.data[self.length()-1]

T = int(input())
for t in range(1, T+1):
    text = input()
    stack = Stack()
    for a in text:
        #비어있다면 넣는다.
        if stack.empty():
            stack.push(a)
        else:
            #같으면 꺼내고
            if stack.top() == a:
                stack.pop()
            #다르면 넣는다.
            else:
                stack.push(a)
    print("#{} {}".format(t, len(stack.data)))