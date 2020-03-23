"""
트리 (Tree) 구조
    트리: Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조

    실제로 어디에 많이 사용되나?
        트리 중 이진 트리 (Binary Tree) 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

<용어>
    Node: 트리에서 데이터를 저장하는 기본 요소 (데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
    Root Node: 트리 맨 위에 있는 노드
    Level: 최상위 노드를 Level 0으로 하였을 때, 하위 Branch로 연결된 노드의 깊이를 나타냄
    Parent Node: 어떤 노드의 상위 레벨에 연결된 노드
    Child Node: 어떤 노드의 다음 레벨에 연결된 노드
    Leaf Node (Terminal Node): Child Node가 하나도 없는 노드
    Sibling (Brother Node): 동일한 Parent Node를 가진 노드
    Depth: 트리에서 Node가 가질 수 있는 최대 Level

이진 트리와 이진 탐색 트리 (Binary Search Tree)
    - 이진 트리: 노드의 최대 Branch가 2인 트리
    - 이진 탐색 트리 (Binary Search Tree, BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
       ~> 왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음!
"""
# Node
class Node:
    def __init__(self, value):
        """
        value를 가진 노드 생성
        """
        self.value = value
        self.left = None        # 노드의 왼쪽 자식
        self.right = None       # 노드의 오른쪽 자식

# 이진 탐색 트리에 데이터 넣기 / 찾기 ~> 반드시 이진 탐색 트리 조건에 부합해야 한다.(작으면 왼쪽 자식으로, 크면 오른쪽 자식으로)
class NodeMgmt:
    def __init__(self, head):
        self.head = head    # Root Node

    def insert(self, value):
        self.current_node = self.head   # Root node부터 현재 노드로 가져와 시작
        while True:
            if value < self.current_node.value:                 # 들어온 값이 현재 노드의 값보다 작다면 왼쪽으로 가야한다.
                if self.current_node.left != None:              # 왼쪽이 비어있지 않다면(이미 노드가 있다면)
                    self.current_node = self.current_node.left  # 기존에 있던 노드와 들어온 값 비교를 위해 현재 노드를 이동
                else:                                           # 왼쪽이 비어있다면
                    self.current_node.left = Node(value)        # 왼쪽에 들어온 값을 갖는 노드 생성
                    break
            else:                                                # 들어온 값이 현재 노드의 값보다 작다면 오른쪽으로 가야한다.
                if self.current_node.right != None:              # 오른쪽이 비어있지 않다면(이미 노드가 있다면)
                    self.current_node = self.current_node.right  # 기존에 있던 노드와 들어온 값 비교를 위해 현재 노드를 이동
                else:                                            # 오른쪽이 비어있다면
                    self.current_node.right = Node(value)        # 오른쪽에 들어온 값을 갖는 노드 생성
                    break

    def search(self, value):
        self.current_node = self.head                           # Root Node부터 시작
        while self.current_node:                                # 노드가 있는 동안
            if value == self.current_node.value:                # 찾고자 하는 값이 현재 노드와 같다
                return True                                     # True 리턴
            elif value < self.current_node.value:               # 찾고자 하는 값이 현재 노드보다 작다면
                self.current_node = self.current_node.left      # 현재 노드를 왼쪽 자식으로 이동
            else:                                               # 찾고자 하는 값이 현재 노드보다 크다면
                self.current_node = self.current_node.right     # 현재 노드를 오른쪽 자식으로 이동
        return False                                            # 모든 노드를 찾았는데 없다면 False 리턴

    def delete(self, value):
        # 0. 삭제할 노드 탐색 ~> 삭제할 노드가 없는 경우에도 처리하기 위해서 없다면 False를 리턴하고 함수를 종료
        searched = False
        self.current_node = self.head                           # Root 노드에서 시작
        self.parent = self.head                                 # Root 노드부터 시작하므로 시작하는 부모 노드는 Root 노드
        while self.current_node:                                # 노드 탐색
            if self.current_node.value == value:                # 현재 노드가 삭제 하고자 하는 값이면
                searched = True                                 # 찾았다고 알려주고 while 종료
                break
            elif value < self.current_node.value:               # 삭제하려는 값이 현재 노드 값보다 작다면
                self.parent = self.current_node                 # 현재 노드를 부모 노드로 삼고
                self.current_node = self.current_node.left      # 왼쪽 자식노드로 이동하고 그 노드를 현재 노드로
            else:                                               # 삭제하려는 값이 현재 노드 값보다 크다면
                self.parent = self.current_node                 # 현재 노드를 부모 노드로 삼고
                self.current_node = self.current_node.right     # 현재 노드의 오른쪽 자식으로 이동
        if searched == False:                                   # 찾는 노드가 없다면
            return False                                        # False 리턴

       # case 1. leaf 노드 삭제
       # self.current_node 가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None:  # 왼쪽도 오른쪽도 자식이 없는 leaf 노드라면
            if value < self.parent.value:           # 삭제하려는 값이 부모 노드 값보다 작다면
                self.parent.left = None             # 부모 노드의 왼쪽 자식을 None으로
            else:                                   # 삭제하려는 값이 부모 노드 값보다 크다면
                self.parent.right = None            # 부모 노드의 오른쪽 자식을 None으로
            del self.current_node                   # 노드 삭제

        # case 2. 자식 노드가 1개인 노드 삭제
        if self.current_node.left != None and self.current_node.right == None:      # 왼쪽 자식은 없고 오른쪽 자식이 있다면
            if value < self.parent.value:                   # 삭제하려는 값이 부모 노드의 값보다 작다면
                self.parent.left = self.current_node.left   # 삭제하려는 노드의 왼쪽 자식 노드를 삭제하려는 노드의 부모 노드의 왼쪽 가지가 가리키게 함(부모보다는 작으니까)
            else:                                           # 삭제하려는 값이 부모 노드의 값보다 크다면
                self.parent.right = self.current_node.left  # 삭제하려는 노드의 왼쪽 자식 노드를 삭제하려는 노드의 부모 노드의 오른쪽 가지가 가리키게 함(부모보다는 크니까)
        elif self.current_node.left == None and self.current_node.right != None:    # 왼쪽 자식은 있고 오른쪽 자식은 없다면
            if value < self.parent.value:                   # 삭제하려는 값이 부모 노드의 값보다 작다면
                self.parent.left = self.current_node.right  # 삭제하려는 노드의 오른쪽 자식 노드를 삭제하려는 노드의 부모 노드의 왼쪽 가지가 가리키게 함(부모보다는 작으니까)
            else:                                           # 삭제하려는 값이 부모 노드의 값보다 크다면
                self.parent.right = self.current_node.right # 삭제하려는 노드의 오른쪽 자식 노드를 삭제하려는 노드의 부모 노드의 오른쪽 가지가 가리키게 함(부모보다는 크니까)

        # case 3. 자식 노드가 2개인 노드 삭제
        # 3-1: 삭제할 Node가 Child Node를 두 개 가지고 있을 경우 (삭제할 Node가 Parent Node 왼쪽에 있을 때)
        #       3-1-1) 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
        #       3-1-2) 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.

        # 우리는 3-1-1 전략 사용. 그러나 이때 또 2가지 경우가 있다.
        # 3-1-1-1: 삭제할 Node가 Parent Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node가 없을 때
        # 3-1-1-2: 삭제할 Node가 Parent Node의 왼쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
        # 가장 작은 값을 가진 Node의 Child Node가 왼쪽에 있을 경우는 없음, 왜냐하면 왼쪽 Node가 있다는 것은 해당 Node보다 더 작은 값을 가진 Node가 있다는 뜻이기 때문임.
        if self.current_node.left != None and self.current_node.right != None:  # 삭제하려는 노드의 자식 노드가 왼쪽 오른쪽에 다 있는 경우
            if value < self.parent.value:                                   # 삭제하려는 값이 현재 부모 노드 값보다 작다면(삭제하려는 노드가 왼쪽 자식)
                self.change_node = self.current_node.right                  # 삭제하려는 노드 자리에 들어올 바꿀 노드는 삭제하려는 노드의 오른쪽에 있고 거기서 가장 작은 값.
                self.change_node_parent = self.current_node.right           # 바꿀 노드의 부모 노드는 삭제하려는 노드의 오른쪽에 있을 것
                # 삭제하려는 노드의 오른쪽에서 가장 작은 값 찾기.
                while self.change_node.left != None:                        # 바꿀 노드의 왼쪽 자식이 있다면 바꿀 노드보다 더 작은 값이므로
                    self.change_node_parent = self.change_node              # 기존의 바꿀 노드는 더 작은 값이 나왔으므로 그 노드의 부모가 되고
                    self.change_node = self.change_node.left                # 새롭게 찾은 더 작은 값의 노드는 새로운 바꿀 노드가 된다.
                # 이제 가장 작은 값은 change_node이고 이 노드를 찾았으므로 위로 올리자.
                if self.change_node.right != None:                          # 바꿀 노드의 오른쪽에 자식이 있다면 바꿀 노드보다 더 큰 값이고
                    self.change_node_parent.left = self.change_node.right   # 바꿀 노드의 부모보다는 작은 값이므로 왼쪽에 연결
                else:                                                       # 바꿀 노드의 오른쪽에 자식이 없다면
                    self.change_node_parent.left = None                     # 바꿀 노드의 부모 왼쪽은 None
                # 이제 가장 작은 값을 삭제하려는 노드 대신 그 자리로 올렸으니 삭제하려는 노드의 양쪽 자식을 이 새로운 노드에 연결
                self.parent.left = self.change_node.right                   # 삭제하려는 노드의 부모 노드 왼쪽 자식은 바꿀 노드의 오른쪽 자식
                self.change_node.right = self.current_node.right            # 바꿀 노드의 오른쪽 자식은 삭제하려는 노드의 오른쪽 자식
                self.change_node.left = self.current_node.left              # 바꿀 노드의 왼쪽 자식은 삭제하려는 노드의 왼쪽 자식

        # 3-2 삭제할 Node가 Child Node를 두 개 가지고 있을 경우 (삭제할 Node가 Parent Node 오른쪽에 있을 때)
        #       3-2-1) 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
        #       3-2-2) 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.

        # 우리는 3-2-1 전략 사용. 그러나 이때 또 2가지 경우가 있다.
        # 3-2-1-1: 삭제할 Node가 Parent Node의 오른쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 Child Node가 없을 때
        # 3-2-1-2: 삭제할 Node가 Parent Node의 오른쪽에 있고, 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 가진 Node의 오른쪽에 Child Node가 있을 때
        # 가장 작은 값을 가진 Node의 Child Node가 왼쪽에 있을 경우는 없음, 왜냐하면 왼쪽 Node가 있다는 것은 해당 Node보다 더 작은 값을 가진 Node가 있다는 뜻이기 때문임
            else:                                                           # 삭제하려는 값이 현재 부모 노드 값보다 크다면(삭제하려는 노드가 오른쪽 자식)
                self.change_node = self.current_node.right                  # 삭제하려는 노드 자리에 들어올 바꿀 노드는 삭제하려는 노드의 오른쪽에 있고 거기서 가장 작은 값.
                self.change_node_parent = self.current_node.right           # 바꿀 노드의 부모 노드는 삭제하려는 노드의 오른쪽에 있을 것.
                # 삭제하려는 노드의 오른쪽에서 가장 작은 값 찾기.
                while self.change_node.left != None:                        # 바꿀 노드의 왼쪽 자식이 있다면 더 작은 값이므로 그 값을 선택해야 하니까
                    self.change_node_parent = self.change_node              # 기존의 바꿀 노드는 더 작은 값의 노드의 부모 노드가 되고
                    self.change_node = self.change_node.left                # 새롭게 찾은 더 작은 값의 노드는 바꿀 노드가 된다.
                # 이제 가장 작은 값의 노드를 change_node로 찾았으니 위로 올리자.
                if self.change_node.right != None:                          # 만약 바꿀 노드의 오른쪽 자식이 있다면, 바꿀 노드보다 큰 값인데
                    self.change_node_parent.left = self.change_node.right   # 부모보다는 작을테니까  바꿀 노드의 부모 노드 왼쪽에 연결한다.
                else:                                                       # 바꿀 노드의 오른쪽에 자식이 없다면
                    self.change_node_parent.left = None                     # 바꿀 노드의 부모 왼쪽은 None
                # 이제 가장 작은 값을 삭제하려는 노드 대신 그 자리로 올렸으니 삭제하려는 노드의 양쪽 자식을 이 새로운 노드에 연결
                self.parent.right = self.change_node                        # 삭제하려는 노드의 부모 노드 오른쪽에 새롭게 바꾼 노드 연결
                self.change_node.left = self.current_node.left              # 새롭게 바꾼 노드의 왼쪽에 삭제하려는 노드의 왼쪽 자식 연결
                self.change_node.right = self.current_node.right            # 새롭게 바꾼 노드의 오른쪽에 삭제하려는 노드의 오른쪽 자식 연결
        return True

# ~~~> 결론적으로 우리 전략에서(삭제하려는 노드의 오른쪽에서 가장 작은 값을 찾아 대체하자는 전략)
# 1. 삭제하려는 노드가 부모 노드보다 큰지 작은지를 생각하고,
# 2. 이 삭제하려는 노드의 오른쪽에서 가장 작은 값을 찾아서
# 3. 이 노드를 삭제하려는 노드 자리로 바꾼다.
# 4. 그리고 이 새롭게 대체되는 노드의 자식이 있다면, 그 자식은 오른쪽에만 존재 할 것이다.
#    왜냐하면 왼쪽에 있다는 말은 새롭게 바꿀 노드보다 작은것이므로 그것이 선택 되었을 것이다.
# 5. 새롭게 바꾼 노드의 오른쪽 자식은 새롭게 바꾼 노드의 부모보다는 작으니까 왼쪽에 연결해 준다.
#    왜냐하면 새롭게 바뀌는 노드는 그 부모의 왼쪽에 연결 되어 있었고, 그 자리로 대체 해주는 것이다.
# 6. 이제 삭제하려는 노드 대신 바뀔 노드가 들어갔다. 따라서 삭제하려는 노드의 양쪽 자식을 새롭데 바뀐 노드 양쪽에 연결 해준다.


head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)

print(BST.search(-1))   # False
print(BST.search(2))    # True

# 이진 탐색 트리에서 노드 삭제 ~> 매우 복잡하므로 경우를 나누어서 생각하자.
# Case 1. Leaf Node(terminal node) 삭제 ---> 자식 노드가 없는 마지막 종단 노드
# 주의 사항! 삭제할 노드의 부모 노드가 삭제할 노드를 가리키지 않도록 한다.(삭제 할 것이므로)

# Case 2. 자식 노드가 1개인 노드 삭제
# 주의 사항! 삭제할 노드의 부모 노드가 삭제할 노드의 자식노드를 가리키게 한다.(A -> B -> C에서 B를 삭제하고 A -> C로 구성)

# Case 3. 자식 노드가 2개인 노드 삭제
# 주의 사항!
# - 삭제할 노드의 오른쪽 자식 중 '가장 작은 값의 노드'를 삭제할 노드의 부모 노드가 가리키게 한다.
# - 삭제할 노드의 왼쪽 자식 중 '가장 큰 값의 노드'를 삭제할 노드의 부모 노드가 가리키게 한다.
# 둘 중의 한 방법을 구현하면, 기능은 결과적으로 같음.
# ~~> 삭제할 Node의 오른쪽 자식중, '가장 작은 값'을 삭제할 Node의 Parent Node가 가리키게 할 경우
#       1) 삭제할 Node의 오른쪽 자식 선택
#       2) 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
#       3) 해당 Node(2번에서 선택한 노드)를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
#       4) 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
#       5) 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
# 즉, 오른쪽 자식의 왼쪽 자식 끝까지 가서, 삭제할 노드의 부모 노드가 이 노드를 가리키게 한다.
# 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는, 해당 Node의 본래 Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함

# 테스트 ~> 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
import random

# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
#print(bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)