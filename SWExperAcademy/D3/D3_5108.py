#D3 5108 숫자 추가

#연결리스트에 사용될 노드
class Node:
    def __init__(self, item):
        self.back_link = None
        self.item = item
        self.next_link = None

#연결리스트 클래스
class Linked_List:
    #생성시 첫시작부분과 마지막부분, 길이를 가진다.
    def __init__(self):
        self.head = None
        self.length = 0
        self.rear = None
    
    #특정 인덱스의 값을 바꾼다면
    def change(self, index, item):
        back_index = self.length - index
        #앞쪽부터 접근이 가깝다면
        if back_index > index:
            #헤드부터 접근한다.
            temp = self.head
            for i in range(index):
                temp = temp.next_link
        #뒤부터 접근이 가깝다면
        else:
            #뒤에서부터 접근한다.
            temp = self.rear
            for i in range(back_index-1):
                temp = temp.back_link
        #원소의 값 바꾸기
        temp.item = item

    #뒤에 추가하는 함수
    def append(self, item):
        node = Node(item)
        #노드가 하나라도 있다면
        if self.length:
            #생성한 노드 연결한다.
            self.rear.next_link = node
            node.back_link = self.rear
        #노드가 하나도 없다면 헤드가 노드를 가리키도록 한다.
        else:
            self.head = node
        #길이 하나 늘려주고
        self.length += 1
        #추가한 값을 꼬리부분으로 바꾸기
        self.rear = node
    
    #노드가 있다면 제일 앞부분의 데이터를 리턴한다.
    def getFirst(self):
        if not self.length:
            return None
        return self.head.item
    #노드가 있다면 제일 뒷부분의 데이터를 리턴한다.
    def getLast(self):
        if not self.length:
            return None
        return self.rear.item

    #인덱스를 이용한 데이터 얻기
    def get(self, index):
        #길이가 없다면 None을 리턴
        if not self.length:
            return None
        #접근하는 인덱스가 길이를 넘어가면 제일 마지막 값 리턴
        if index >= self.length:
            return self.rear.item
        #접근한 인덱스를 길이에서 빼본다.
        back_index = self.length - index
        #앞부분과 뒷부분 어디에서 접근하는게 빠른지 판단한다.
        #앞부분에서 빠르다면
        if back_index > index:
            temp = self.head
            for i in range(index):
                temp = temp.next_link
        #뒷부분에서 빠르다면
        else:
            temp = self.rear
            for i in range(back_index-1):
                temp = temp.back_link
        #결과값 리턴
        return temp.item

    #값을 추가하는 함수
    def insert(self, index, item):
        node = Node(item)
        #노드가 없다면
        if not self.length:
            self.head = node
            self.rear = node
        #인덱스가 길이를 넘어가면 마지막에 추가
        elif self.length <=index:
            self.rear.next_link = node
            node.back_link = self.rear
            self.rear = node
        #넣는 인덱스가 0번이라면
        elif not index:
            #제일 앞부분에 데이터를 넣고 주소위치를 바꿔준다.
            self.head.back_link = node
            node.next_link = self.head
            self.head = node
        #위의 상황이 아니라면
        else:
            #앞과 뒤쪽중 어디서 접근하는게 빠른지 찾는다.
            back_index = self.length - index
            #앞부분의 접근이 빠르다면
            if back_index > index:
                temp = self.head
                for i in range(index):
                    temp = temp.next_link
            #뒷부분의 접근이 빠르다면
            else:
                temp = self.rear
                for i in range(back_index-1):
                    temp = temp.back_link
            #찾은 값을 기준으로 노드를 추가하고 주소를 변경
            temp.back_link.next_link = node
            node.back_link = temp.back_link
            node.next_link = temp
            temp.back_link = node
        self.length += 1

    #원소를 꺼내며 가지고 있던 값 리턴
    def pop(self,index=-1):
        value = None
        #길이가 없다면 반환할 값이 없다.
        if not self.length:
            value = None
        #길이가 1이라면 원소가 하나이므로 head와 rear를 None으로 바꿔준다.
        elif self.length == 1:
            value = self.head.item
            self.head = None
            self.rear = None
        #0번 인덱스를 꺼낸다면 헤드를 1번인덱스에 연결해줘야 한다.
        elif not index :
            self.head = self.head.next_link
        #인덱스가 음수이거나 길이보다 크다면 제일 마지막 값을 리턴
        elif index < 0 or index >= self.length-1:
            value = self.rear.item
            self.rear = self.rear.back_link
            self.rear.next_link = None
        else :
            #앞쪽과 뒤쪽중 가까운곳 부터 찾아서 리턴
            back_index = self.length - index
            if back_index > index:
                temp = self.head
                for i in range(index):
                    temp = temp.next_link
            else:
                temp = self.rear
                for i in range(back_index-1):
                    temp = temp.back_link
            #주소 변경작업
            value = temp.item
            back_node = temp.back_link
            next_node = temp.next_link
            back_node.next_link = next_node
            next_node.back_link = back_node
        self.length -=1
        return value


'''
for t in range(1, int(input()) + 1):
    #N 수열길이, M 추가횟수, L 출력 인덱스
    N, M, L = map(int, input().split())
    linked_list = input().split()
    #삽입할 숫자 입력받기
    for _ in range(M):
        index, number = map(int, input().split())
        #insert함수를 이용하여 추가
        linked_list.insert(index, number)
    print('#{} {}'.format(t, linked_list[L]))
'''

for t in range(1, int(input()) + 1):
    #N 수열길이, M 추가횟수, L 출력 인덱스
    N, M, L = map(int, input().split())
    temp = input().split()
    linked_list = Linked_List()
    for i in temp:
        linked_list.append(i)
    #삽입할 숫자 입력받기
    for _ in range(M):
        index, number = map(int, input().split())
        #insert함수를 이용하여 추가
        linked_list.insert(index, number)
    print('#{} {}'.format(t, linked_list.get(L)))