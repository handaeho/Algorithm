import queue

# Queue()로 큐 만들기 (가장 일반적인 큐, FIFO(First-In, First-Out)
data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())

# LifoQueue()로 큐 만들기 (LIFO(Last-In, First-Out))
data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())

# PriorityQueue()로 큐 만들기 ~~~> 우선 순위를 지어하고, 순위에 따라 가져온다. 파라미터로 (우선순위, 데이터)의 '튜플'을 전달.
data_queue = queue.PriorityQueue()

data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())

# 연습: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()


def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]

    return data


for index in range(10):
    enqueue(index)

print(len(queue_list))

for _ in range(len(queue_list)):
    print(dequeue())
