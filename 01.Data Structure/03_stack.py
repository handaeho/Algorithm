# 재귀함수로 스택 구조 이해
def recursive(data):
    if data < 0:
        print('END')
    else:
        print(data)
        recursive(data - 1)
        print('RETURN', data)


recursive(5)

# 리스트 구조로 스택 이해
stack = list()

# append = push
for i in range(10):
    stack.append(i)

print(stack)

# pop() ~> pop()은 인덱스를 지정해 주지 않을 경우 맨 마지막 원소를 가져온다. 즉, '스택'의 기능과 같음
print(stack.pop())

# 연습: 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수 사용하지 않고 직접 구현해보기)
stack_list = list()


def push(data):
    stack_list.append(data)
    print(stack_list)


def pop():
    data = stack_list[-1]  # 스택은 '마지막 원소를 가장 먼저' 가지고 온다!
    del stack_list[-1]
    print(data)

    return data


for i in range(10):
    push(i)

for i in range(len(stack_list)):
    pop()