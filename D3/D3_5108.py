#D3 5108 숫자 추가

class Node:
    def __init__(self, item):
        self.back_link = None
        self.item = item
        self.next_link = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0
        self.rear = None

    def change(self, index, item):
        temp = self.head
        for i in range(index):
            temp = temp.next_link
        temp.item = item

    def append(self, item):
        self.length += 1
        node = Node(item)
        if self.head != None:
            self.rear.next_link = node
            node.back_link = self.rear
        else:
            self.head = node
        self.rear = node
    
    def getFirst(self):
        if self.head == None:
            return None
        return self.head.item

    def getLast(self):
        if self.head == None:
            return None
        return self.rear.item

    def get(self, index):
        if self.rear == None:
            return None
        if index >= self.length:
            return self.rear.item
        temp = self.head
        for i in range(index):
            temp = temp.next_link
        return temp.item

    def insert(self, index, item):
        node = Node(item)
        if self.head == None:
            self.head = node
        elif self.length <=index:
            self.rear.next_link = node
            node.back_link = self.rear
            self.rear = node
        elif not index:
            self.head.back_link = node
            node.next_link = self.head
            self.head = node
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next_link
            temp.back_link.next_link = node
            node.back_link = temp.back_link
            node.next_link = temp
            temp.back_link = node
        self.length += 1

    def pop(self,index=-1):
        value = None
        if not self.length:
            value = None
        elif self.length == 1:
            value = self.head.item
            self.head = None
            self.rear = None
        elif not index :
            self.head = self.head.next_link
        elif (index < 0 or index >= self.length-1) and self.rear != None:
            value = self.rear.item
            self.rear = self.rear.back_link
            self.rear.next_link = None
        else :
            temp = self.head
            for i in range(index):
                temp = temp.next_link
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