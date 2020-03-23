"""
링크드 리스트 (Linked List) 구조
    - 연결 리스트라고도 함.
    - 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조.
    - 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조.

링크드 리스트 기본 구조와 용어
    - 노드(Node): 데이터 저장 단위 (데이터값, 포인터) 로 구성
    - 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간
"""
# 간단한 링크드 리스트
# Node 구현 - 보통 파이썬에서 링크드 리스트 구현시, 파이썬 클래스를 활용함
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 링크드 리스트로 데이터 추가하기
def add(data):
    node = head             # head 노드를 가져옴
    while node.next:        # 다음 노드가 있다면
        node = node.next    # 그 다음 노드로 이동. 또 다음이 있다면 그 다음 이동, ... 그리고 끝 노드에 도착하면 while문 종료
    node.next = Node(data)  # 끝에 도달 했으므로 node.next의 주소는 None. 따라서 None에 새로운 data를 가진 노드의 주소를 추가.

# Node와 Node 연결
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

# 링크드 리스트 데이터 추가
node1 = Node(1)
head = node1
for i in range(2, 10):
    add(i)

# 링크드 리스트 데이터 출력
node = head             # 맨 앞의 head 노드 가져옴
while node.next:        # 다음 노드가 존재하면
    print(node.next)    # 다음 노드 주소 출력
    node = node.next    # 다음 노드로 이동
    print(node.data)    # 그 노드가 가진 데이터 출력

print(' ============================================== ')

# 링크드 리스트 사이에 데이터 추가하기
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

print(' ============================================== ')


node3 = Node(1.5)           # 1.5이라는 데이터를 가진 노드가 1과 2 사이에 들어가야함
node = head                 # 맨 앞의 노드 가져옴
search = True
while search:               # search = True일 동안
    if node.data == 1:      # 노드 데이터가 1이라면
        search = False      # search를 False로 하고 while 종료
    else:                   # 데이터가 1이 아니라면
        node = node.next    # 다음 노드로 이동

next_node = node.next       # 노드가 가지고 있는 다음 노드의 주소(1은 2를 가리키는 중)
node.next = node3           # node3의 주소로 바꿈(1은 1.5를 가리키게 됨)
node3.next = next_node      # node3이 가리키는 다음 노드의 주소를 2를 가지고 있는 노드의 주소로 바꿈(1.5는 2를 가리키게 됨)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

print(' ============================================== ')

# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현
class Node:
    """
    노드 생성
    """
    def __init__(self, data, next=None):
        self.data = data    # 노드 데이터
        self.next = next    # 노드 주소

class NodeMgmt:
    """
    노드 매지니먼트(관리)
    """
    def __init__(self, data):
        self.head = Node(data)  # Node class에서 생성된 맨 앞의 노드

    def add(self, data):
        """
        노드 추가
        """
        if self.head == '':         # 맨 앞의 노드에 아무것도 없으면
            self.head = Node(data)  # 새로운 노드를 생성해라
        else:
            node = self.head        # 맨 앞의 노드 가지고 옴
            while node.next:        # 다음 노드가 존재하면
                node = node.next    # 다음 노드로 이동
            node.next = Node(data)  # 다음 노드가 마지막 노드라면 또 새로운 노드 생성

    def delete(self, data):
        """
        특정 노드 삭제

        if self.head.data == data: # 경우의 수1: self.head를 삭제해야할 경우 - self.head를 바꿔줘야 함
            temp = self.head # self.head 객체를 삭제하기 위해, 임시로 temp에 담아서 객체를 삭제했음
            self.head = self.head.next # 만약 self.head 객체를 삭제하면, 이 코드가 실행이 안되기 때문!
            del temp
        else:
            node = self.head
            while node.next: # 경우의 수2: self.head가 아닌 노드를 삭제해야할 경우
        """
        if self.head == '':                 # 맨 앞의 노드에 아무것도 없으면
            print('삭제할 노드가 없습니다.')
            return
        if self.head.data == data:          # 삭제 하려는 데이터가 맨 앞의 노드라면
            temp = self.head                # 맨 앞의 노드를 임시 변수 temp로 옮겨두고
            self.head = self.head.next      # 그 다음 노드를 head 노드로
            del temp                        # 옮겨둔 노드 삭제
        else:
            node = self.head                    # head 노드 가져옴
            while node.next:                    # 다음 노드가 있는 동안(삭제할 노드를 찾아야 하므로)
                if node.next.data == data:      # 다음 노드가 삭제할 데이터를 가지고 있다면
                    temp = node.next            # 임시변수 temp에 옮겨두고
                    node.next = node.next.next  # 그 노드의 다음노드를 가져와 당긴다.
                    del temp                    # 임시변수에 옮겨둔 노드 삭제
                    pass
                else:
                    node = node.next            # 노드를 가져와 찾는다.

    def search_node(self, data):
        """
        특정 데이터를 가진 노드 찾기
        """
        node = self.head                        # 맨 앞의 head 노드 가져옴
        while node:                             # 노드가 있는동안(노드들을 탐색)
            if node.data == data:               # 찾고자 하는 데이터를 가진 노드를 찾으면
                return node                     # 그 노드를 리턴
            else:
                node = node.next                # 다음 노드로 계속 이동

    def desc(self):
        """
        노드 출력
        """
        node = self.head        # head 노드 가지고 옴
        while node:
            print(node.data)    # node 데이터 출력
            node = node.next    # 다음 노드로 이동


linked_list_1 = NodeMgmt(0)     # 첫번째 0 노드 생성
linked_list_1.desc()            # 만들어진 노드 출력

for data in range(1, 10):       # 1 ~ 9까지 데이터 추가
    linked_list_1.add(data)

linked_list_1.desc()            # 만들어진 노드 출력

linked_list_2 = NodeMgmt(0)     # 삭제 테스트 위해 노드를 하나만 만들어 봄
linked_list_2.desc()
print(linked_list_2.head)

linked_list_2.delete(0)         # 데이터가 0인 노드 삭제
print(linked_list_2.head)       # None 출력(정상 삭제)

linked_list_3 = NodeMgmt(1)     # 이번에는 데이터가 1인 노드 하나 만듦
linked_list_3.desc()

for data in range(2, 11):       # 2 ~ 10까지 데이터를 가진 노드들 추가
    linked_list_3.add(data)
linked_list_3.desc()

linked_list_3.delete(5)         # 데이터가 5인 노드 하나 삭제
linked_list_3.desc()            # 1 2 3 4 6 7 8 9 10 출력됨

# 연습1: 위 코드에서 노드 데이터가 2인 노드 삭제해보기
linked_list_3.delete(2)
linked_list_3.desc()            # 1 3 4 5 6 7 8 9 10

# 연습2: 위 코드에서 노드 데이터가 특정 숫자인 노드를 찾는 함수를 만들고, 테스트해보기
# 테스트: 임의로 1 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 4인 노드의 데이터 값 출력해보기
linked_list_4 = NodeMgmt(1)
for data in range(2, 10):
    linked_list_4.add(data)
linked_list_4.desc()

node_4 = linked_list_4.search_node(4)
print(node_4.data)

print(' ============================================== ')

# 더블 링크드 리스트(Doubly linked list)
class Node:
    """
    노드 생성
    """
    def __init__(self, data, prev=None, next=None):
        self.prev = prev    # 이전 노드
        self.next = next    # 다음 노드
        self.data = data    # 노드가 가질 데이터

class double_NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)      # 노드 생성
        self.tail = self.head       # 더블 링크드 리스트는 '양방향'이므로 head는 tail이 될 수 있음

    def insert(self, data):
        """
        노드 삽입
        """
        if self.head == None:       # 노드가 없다면
            self.head = Node(data)  # 노드 생성
            self.tail = self.head   # 양방향 리스트이므로 tail 존재
        else:
            node = self.head        # head 노드 가져옴
            while node.next:        # 다음 노드가 있다면
                node = node.next    # 다음 노드를 가져옴(리스트의 끝까지)
            new = Node(data)        # 다음 노드가 없다면(끝까지 간 경우), 새롭게 노드 생성
            node.next = new         # 새로운 노드가 생성되었으므로 다음 노드는 새로운 노드
            new.prev = node         # 새로운 노드는 기존의 마지막 노드를 이전 노드로 가리켜야 함.
            self.tail = new         # 링크드 리스트의 tail로 새로운 노드 지정

    def desc(self):
        """
        리스트 안의 노드 출력
        """
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        """
        head 노드부터 탐색
        """
        if self.head == None:           # head 노드가 없다면
            return False                # Flase 리턴

        node = self.head                # head 노드 가져옴
        while node:                     # 리스트 내의 노드들 중
            if node.data == data:       # 특정 데이터를 가진 노드를 찾으면
                return node             # 그 노드 리턴
            else:                       # 아니라면
                node = node.next        # 다음 노드로 이동
        return False                    # while에서 리턴이 안된거라면 그 노드가 없는 것.

    def search_from_tail(self, data):
        """
        tail 노드부터 탐색
        """
        if self.head == None:           # head가 없다면 tail도 없는것이다.(노드가 없는 빈 리스트)
            return False

        node = self.tail                # tail 노드 가져옴
        while node:                     # 리스트 내의 노드들 중
            if node.data == data:       # 특정 데이터를 가진 노드를 찾으면
                return node             # 그 노드 리턴
            else:                       # 아니라면
                node = node.prev        # 이전 노드로 이동
        return False                    # while에서 리턴이 안된거라면 그 노드가 없는 것.

    # 연습3: 위 코드에서 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수를 만들고, 테스트해보기
    # - 더블 링크드 리스트의 tail 에서부터 뒤로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
    # - 테스트: 임의로 0 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 2인 노드 앞에 1.5 데이터 값을 가진 노드를 추가해보기
    def insert_before(self, data, before_data):
        """
        특정 데이터 뒤에 노드 삽입(data를 before_data 뒤에 삽입)
        """
        if self.head == None:           # head 노드가 없다면(빈 리스트)
            self.head = Node(data)      # 전달 받은 데이터를 가진 head 노드 생성
            return True
        else:
            node = self.tail                    # tail 노드 가져옴(맨 뒤에서부터 노드 검색)
            while node.data != before_data:     # tail 노드의 데이터가 before_data가 아니라면
                node = node.prev                # 이전 노드(앞의 노드)를 가져옴
                if node == None:                # 이전 노드가 없다면
                    return False                # False 반환
            new_node = Node(data)               # 전달 받은 데이터를 가진 새로운 노드 생성
            before_new = node.prev              # 기존 이전 노드를 새롭게 생성한 노드의 이전 노드로
            before_new.next = new_node          # 기존의 이전 노드의 다음 노드는 새롭게 생성한 노드가 되므로(둘을 양방향 연결)
            new_node.prev = before_new          # 새롭게 생성한 노드의 이전 노드는 기존에 있던 노드의 이전 노드
            new_node.next = node                # 새롭게 생성한 노드의 다음 노드는 원래 노드
            # 예를 들어 현재 A-C가 연결 되어 있는데 B를 사이에 넣고 싶다. ~> insert_before(B, C)
            # 그럼 tail 노드인 C를 가져오고 우리는 C 뒤에 B를 넣고자 하므로 (before_data=C) while문이 실행 되지 않는다.
            # 만약 C가 아닌 D, E, F등이 tail 노드였다면 C를 찾을 때 까지 while문이 실행 될 것이다.
            # 전달 받은 B라는 데이터를 가진 노드가 새롭게 생성되고,
            # 지금 tail 노드는 C니까 node = C이므로 before_new에 A를 저장하고
            # A의 다음 노드는 새롭게 생성된 B가 되고
            # A는 B의 이전 노드가 되고
            # C는 B의 다음 노드가 된다.

    # 연습4: 위 코드에서 노드 데이터가 특정 숫자인 노드 뒤에 데이터를 추가하는 함수를 만들고, 테스트해보기
    # - 더블 링크드 리스트의 head 에서부터 다음으로 이동하며, 특정 숫자인 노드를 찾는 방식으로 함수를 구현하기
    # - 테스트: 임의로 0 ~ 9까지 데이터를 링크드 리스트에 넣어보고, 데이터 값이 1인 노드 다음에 1.7 데이터 값을 가진 노드를 추가해보기
    def insert_after(self, data, after_data):
        """
        특정 데이터 앞에 노드 추가
        """
        if self.head == None:                   # head 노드가 없다면(빈 리스트이므로)
            self.head = Node(data)              # 전달 받은 데이터를 갖는 새로운 노드 생성
            return True
        else:
            node = self.head                    # head 노드 가져옴
            while node.data != after_data:      # head 노드가 after_data가 아니라면
                node = node.next                # 다음 노드를 가져옴
                if node == None:                # 다음 노드가 없다면
                    return False                # False 리턴
            new_node = Node(data)
            after_new = node.next
            new_node.next = after_new
            new_node.prev = node
            node.next = new_node
        return True
        # 예를 들어 현재 A-C가 연결 되어 있는데 B를 사이에 넣고 싶다. ~> insert_after(B, A)
        # 그럼 head 노드인 A를 가져오고 우리는 A 뒤에 B를 넣고자 하므로 (after_data=A) while문이 실행 되지 않는다.
        # 만약 A가 아닌 D, E, F등의 뒤에 넣고자 했다면 그것을 찾을 때 까지 while문이 실행 될 것이다.
        # 전달 받은 B라는 데이터를 가진 노드가 새롭게 생성되고,
        # 지금 head 노드는 A니까 node = A이므로 after_new에 C를 저장하고(원래의 다음노드)
        # 새롭게 생성된 B의 다음 노드는 C가 되고
        # A는 B의 이전 노드가 되고
        # B는 A의 다음 노드가 된다.

double_linked_list = double_NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)

double_linked_list.desc()

print(double_linked_list.search_from_head(3))
print(double_linked_list.search_from_head(3).data)

print(double_linked_list.search_from_tail(7))
print(double_linked_list.search_from_head(7).data)


node_mgmt = double_NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.insert(data)

node_mgmt.desc()

node_mgmt.insert_before(1.5, 2)
node_mgmt.desc()

node_mgmt.insert_after(7.5, 7)
node_mgmt.desc()
