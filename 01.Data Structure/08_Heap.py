"""
힙 (Heap)이란?
= 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)

완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

힙을 사용하는 이유
    배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n) 이 걸림
    이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면, O(logn) 이 걸림
    우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

힙은 최대값을 구하기 위한 구조 (최대 힙, Max Heap) 와, 최소값을 구하기 위한 구조 (최소 힙, Min Heap) 로 분류할 수 있음

힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조
    - 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
      최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음
    - 완전 이진 트리 형태를 가짐

힙과 이진 탐색 트리의 공통점과 차이점
공통점:
    힙과 이진 탐색 트리는 모두 이진 트리임
차이점:
    힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
    이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
    힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
    힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
    이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨

힙에 데이터 삽입하기
1. 기본 동작
    힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입
2. 삽입할 데이터가 힙의 데이터보다 클 경우 (Max Heap 의 예)
    먼저 삽입된 데이터는 완전 이진 트리 구조에 맞추어, 최하단부 왼쪽 노드부터 채워짐
    채워진 노드 위치에서, 부모 노드보다 값이 클 경우, 부모 노드와 위치를 바꿔주는 작업을 반복함 (swap)

힙에 데이터 삭제하기
    보통 삭제는 최상단 노드 (root 노드)를 삭제하는 것이 일반적임
        ~> 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
    상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드 (일반적으로 가장 마지막에 추가한 노드) 를 root 노드로 이동
    root 노드의 값이 child node 보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복함 (swap)

힙과 배열
일반적으로 힙 구현시 배열 자료구조를 활용함
배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 좀더 수월함
    - 부모 노드 인덱스 번호 (parent node's index) = 자식 노드 인덱스 번호 (child node's index) // 2
    - 왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2
    - 오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2 + 1
"""
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    # 힙에 데이터 삽입 구현(Max Heap 예)
    def insert(self, data):
        """
        인덱스 번호는 1부터 시작하도록 변경 ~~~> 힙 어레이의 0번은 None으로 설정해 사용하지 않게 한다.
        """
        if len(self.heap_array) == 1:       # 힙 어레이가 비어있다면(0번째에는 None이 있으므로 빈상태의 길이 == 1)
            self.heap_array.append(data)    # 힙 어레이에 전달받은 데이터 추가
            return True

        self.heap_array.append(data)        # 힙 어레이가 비어있지 않으면 그 뒤에 전달받은 데이터 추가

        # insert된 노드의 인덱스(마지막 자식 노드 인덱스) = 힙 배열 전체길이(전체 노드 수) - 1 ~> 마지막 노드 선택과 같음.
        inserted_idx = len(self.heap_array) - 1

        # insert된 노드의 이동을 위해 move_up() 함수 실행(부모 노드보다 insert된 노드가 커서 바뀌어야 한다면 반복 실행)
        while self.move_up(inserted_idx):
            # 부모 노드 인덱스 = insert된 노드(자식 노드) 인덱스 // 2
            parent_idx = inserted_idx // 2

            # insert된 노드와 부모 노드를 바꿈(swap)
            self.heap_array[inserted_idx], self.heap_array[parent_idx] \
                = self.heap_array[parent_idx], self.heap_array[inserted_idx]

            # 부모 노드가 insert된 노드와 바뀌어서 아래로 내려갔으므로 인덱스도 서로 바뀜
            inserted_idx = parent_idx

        return True

    # 힙 클래스 구현3 - insert2
    # 삽입한 노드가 부모 노드의 값보다 클 경우, 부모 노드와 삽입한 노드 위치를 바꿈
    # 삽입한 노드가 루트 노드가 되거나, 부모 노드보다 값이 작거나 같을 경우까지 반복
    # 특정 노드의 관련 노드 위치 알아내기
    #   - 부모 노드 인덱스 번호 (parent node's index) = 자식 노드 인덱스 번호 (child node's index) // 2
    #   - 왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2
    #   - 오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2 + 1
    def move_up(self, inserted_idx):
        """
        입력 받은 노드의 인덱스 inserted_idx에 해당하는 노드를 위로 올리기(부모 노드와 바꾸어야 하는지 판단)
        """
        # insert된 노드의 인덱스 번호가 1보다 작거나 같다면 더이상 올라갈 수 없으므로 False 리턴
        if inserted_idx <= 1:
            return False

        # insert된 노드의 부모 노드의 인덱스 = insert된 노드(자식 노드) 인덱스 번호 // 2
        parent_idx = inserted_idx // 2

        # 자식 인덱스 번호(insert된 노드의 인덱스)가 자신의 부모 노드 인덱스보다 크다면
        # insert() 함수에서 while문 실행을 위해 True 리턴(부모와 자식 노드 위치를 바꿈)
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def move_down(self, popped_idx):
        """
        popped_idx = pop으로 꺼낼 노드의 인덱스
        """
        # pop으로 꺼낼 노드의 왼쪽 자식 노드 인덱스 번호  = 부모 노드 인덱스 번호(pop으로 꺼낼 노드) * 2
        left_child_popped_idx = popped_idx * 2
        # pop으로 꺼낼 노드의 오른쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호(pop으로 꺼낼 노드) * 2 + 1
        right_child_popped_idx = popped_idx * 2 + 1

        # case 1: 왼쪽 자식 노드도 없을 때, 밑으로 내릴 필요가 없으므로 (len(self.heap_array)는 전체길이 - 1 (0번은 None이므로))
        if left_child_popped_idx >= len(self.heap_array):       # 만약 왼쪽 자식 노드의 인덱스가 힙 어레이의 크기보다 크다면
            return False                                        # 왼쪽 자식이 없으므로 False 리턴

        # case 2: 왼쪽 자식노드는 있지만 오른쪽 자식 노드는 없을 때, 오른쪽 자식노드와 비교를 해야하므로
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:    # pop한 노드의 인덱스가 왼쪽 자식보다 작다면(자식이 더 크다면)
                return True                                                             # 바꾸어 주어야 하므로
            else:
                return False

        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            # 두 자식 노드의 크기비교를 위해
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:    # 왼쪽 자식 노드가 오른쪽 자식 노드보다 크다면
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:            # 만약 왼쪽 노드가 부모 노드(pop한 노드)보다 크다면
                    return True                                                                     # 왼쪽 자식 노드가 부모 노드(pop한 노드) 자리로
                else:                                                                               # 부모 노드(pop한 노드)가 더 크다면
                    return False                                                                    # 바꿀 필요 없다.

            else:                                                                                   # 오른쪽 자식 노드가 왼쪽 자식 노드보다 크다면
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:           # 만약 오른쪽 노드가 부모 노드(pop한 노드)보다 크다면
                    return True                                                                     # 오른쪽 자식 노드가 부모 노드(pop한 노드) 자리로
                else:                                                                               # 부모 노드(pop한 노드)가 더 크다면
                    return False                                                                    # 바꿀 필요 없다.

   # 힙에 데이터 삭제 구현 (Max Heap 예)
    # 힙 클래스 구현4 - delete1
    # 보통 삭제는 최상단 노드 (root 노드)를 삭제하는 것이 일반적임
    # 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
    def pop(self):
        # 힙 어레이의 길이가 1보다 작거나 같다면 반환할 것이 없다.(0번은 None이므로)
        if len(self.heap_array) <= 1:
            return None

        # Max heap의 경우 맨 위의 Root 노드가 최대값이므로 root 노드 리턴
        returned_data = self.heap_array[1]

        # 마지막에 들어온 노드를 root로 올림
        self.heap_array[1] = self.heap_array[-1]

        # root로 올렸으므로 마지막에 들어온 노드 삭제
        del self.heap_array[-1]

        popped_idx = 1

        # move_down() 함수를 통해 pop한 노드(부모 노드)와 양쪽 자식 노드 간의 크기 비교를 통해 자리 교환
        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            # case 1: 왼쪽 / 오른쪽 자식이 모두 없다면 자리교환 할 필요 X.
            # case 2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx > len(self.heap_array):                                   # 오른쪽 자식이 없다면
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:        # pop한 노드(부모 노드)보다 왼쪽 자식 노드가 크다면
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] \
                        = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]   # 둘의 위치 교환
                    popped_idx = left_child_popped_idx                                          # 위치과 바뀌었으니 인덱스도 바뀜

        # case 3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:    # 만약 왼쪽 자식이 오른쪽 자식보다 크다면, 왼쪽 자식과 부모를 비교 해야한다.
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:            # 이번에는 왼쪽 자식과 부모 노드(pop한 노드)를 비교해 부모가 작다면 바꾸어야 하므로
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] \
                            = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]       # 둘의 위치 교환
                        popped_idx = left_child_popped_idx                                              # 위치가 바뀌었으니 인덱스도 바뀜

                else:                                                                                   # 만약 오른쪽 자식이 왼쪽 자식보다 크다면, 오른쪽 자식과 부모를 비교 해야한다.
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:           # 오른쪽 자식이 부모 노드(pop한 노드)와 바교해, 부모가 작다면 위로 올려야 하므로
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] \
                            = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]      # 둘의 위치 교환
                        popped_idx = right_child_popped_idx                                             # 위치가 바뀌었으니 인덱스도 바뀜

        return returned_data

    # 힙 클래스 구현4 - delete2
    # 상단의 데이터 삭제시, 가장 최하단부 왼쪽에 위치한 노드 (일반적으로 가장 마지막에 추가한 노드) 를 root 노드로 이동
    # root 노드의 값이 child node 보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복함 (swap)
    # 특정 노드의 관련 노드 위치 알아내기
    #   - 부모 노드 인덱스 번호 (parent node's index) = 자식 노드 인덱스 번호 (child node's index) // 2
    #   - 왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2
    #   - 오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) * 2 + 1

# 정리하자면, 힙은 부모 노드가 자식 노드보다 크거나 같아야하며(Max Heap) / 작거나 같아야하며(Min Heap)
# 힙에 노드를 새로 삽입 할 때는 반드시 왼쪽 하단부터 채워야 한다.
# 그리고 Max heap의 예에서 부모 노드와 비교하여 그 값이 크다면 부모와 위치를 교환하고, 또 그 부모와 비교하여 교환 여부를 판단하는 것을 반복한다.
# 이는 Root 노드까지 갔을 경우 또는 부모가 더이상 작지 않을 경우까지 반복한다.
# 힙에서 노드를 삭제할 경우에는 보통 최대값 또는 최소값을 삭제하므로 root 노드를 삭제하는 것이 일반적이고,
# 상단의 노드를 삭제했을 경우, 가장 마지막에 들어온(즉, 최하단 왼쪽 노드)를 삭제하려는 노드의 자리로 옮기고
# 양쪽 자식노드의 존재 여부와 그 크기를 비교하여, 자식이 더 크다면 그 자식 노드 중 더 큰 값을 가진 노드와 위치 교환을 반복한다.
# 자식이 없다면 더이상 위치 교환을 할 필요가 없는 것이고, 자식이 있다면 먼저 그 둘 간의 크기 비교를 하고, 더 큰 자식과 부모 노드를 비교한다.
# 힙에서 부모노드, 왼쪽 자식 노드, 오른쪽 자식 노드의 인덱스를 구하는 방법은 다음과 같다. 단, Root 노드의 인덱스는 1이다.
# - 부모 노드 인덱스 번호 = 자식 노드 인덱스 번호 // 2 (이때, 자식 노드는 왼쪽부터 채워지므로 왼쪽 자식 노드 인덱스를 의미)
# - 왼쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2
# - 오른쪽 자식 노드 인덱스 번호 = 부모 노드 인덱스 번호 * 2 + 1

heap = Heap(1)
print(heap.heap_array)  # [None, 1]

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)  # [None, 20, 10, 15, 5, 4, 8]

print(heap.pop())       # 20
print(heap.heap_array)  # [None, 15, 10, 8, 5, 4]

