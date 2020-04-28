"""
재귀 용법(Recursive Call, 재귀호출)
    - 함수 안에서 동일한 함수를 호출하는 형태
"""
"""
예제) 팩토리얼
2! = 1 x 2
3! = 1 x 2 x 3
4! = 1 x 2 x 3 x 4
...
n! = 1 x 2 x 3 x ... x n

~> 규칙
if n > 1:
    return n * function(n-1)
else:
    return n

>> 시간 복잡도 & 공간 복잡도
= factorial(n) 함수는 n-1번의 factorial() 함수를 호출한다.
    - 일종의 n-1번 반복문을 호출한 것과 동일
    - factorial() 함수를 호출할 때마다, 지역 변수 n이 생성된다.
따라서, 시간 복잡도 / 공간 복잡도 = O(n-1) = O(n)

>> 일반적인 형태 1.
def function(입력):
    if 입력 > 일정값:                        # 입력이 일정 값 이상이면
        return 입력 * function(입력 - 1)         
    else:
        return 일정값, 입력값, 또는 특정값    # 재귀 호출 종료
        
>> 일반적인 형태 2.
def function(입력):
    if 입력 <= 일정값:                       # 입력이 일정 값보다 작으면
        return 일정값, 입력값, 또는 특정값    # 재귀 호출 종료
    else:
        return 입력 * function(입력 - 1) 

> 재귀 호출은 '스택'처럼 관리된다.
> 파이썬에서 재귀호출은 '1000회 이하'이어야 한다.
"""
import random
random.seed(428)

# 일반적인 형태 1.
def factorial_1(num):
    if num > 1:
        return num * factorial_1(num - 1)
    else:
        return num

# 일반적인 형태 2.
def factorial_2(num):
    if num <= 1:
        return num
    else:
        return num * factorial_2(num - 1)


""" 
예제 1. 다음 함수를 재귀 함수를 활용해서 완성해서 1부터 num까지의 곱이 출력되게 만드세요
def muliple(data):
    if data <= 1:
        return data

    return -------------------------

multiple(10)
"""
def muliple(data):
    if data <= 1:
        return data
    else:
        return data * muliple(data - 1)

"""
예제 2. 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요
"""
def sum(list):
    total = 0
    for i in list:
        total += i
    return total

"""
예제 2-1. 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요 (재귀함수를 써보세요)
def sum_recur(list):
    if len(list) == 1:
        return list[0]

    return --------------------------------
"""
def sum_recur(list):
    if len(list) <= 1:
        return list[0]
    else:
        return list[0] + sum_recur(list[1:])

"""
예제 3. 
회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요
"""
def palindrome(str):
    return str == str[::-1]
    # [::-1] ~> 처음부터 끝까지 -1칸 간격으로 역순
    # 즉, 거꾸로 하나씩 문자를 가져와 처음부터 차려대로 문자와 비교
    # 결과는 True or False

""" 
예제 3-1. 
회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
회문을 판별할 수 있는 함수를 재귀함수를 활용해서 만드세요.
"""
def palindrome_rucur(str):
    if len(str) == 1:
        return True
    if str[0] == str[-1]:
        return palindrome(str[1:-1])
    else:
        return False

"""
예제 4.
정수 n에 대해 n이 홀수이면 3 X n + 1 을 하고, n이 짝수이면 n 을 2로 나눕니다.
이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.

예를 들어 n에 3을 넣으면,
3
10
5
16
8
4
2
1
이 됩니다.
이렇게 정수 n을 입력받아, 위 알고리즘에 의해 1이 되는 과정을 모두 출력하는 함수를 작성하세요.
"""
def func(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:                  # 홀수라면
        return func((3 * n) + 1)    # 계산하고 다시 func() 함수를 호출해 반복하며 'n == 1'이 되면 리턴하며 종료
    else:                           # 짝수라면
        return func((n / 2))        # 계산하고 다시 func() 함수를 호출해 반복하며 'n == 1'이 되면 리턴하며 종료

"""
예제 5.
문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오

힌트: 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n) 이라고 하면,
f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 패턴 찾기
출처: ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Taejon 2001

~> 
N[1] = 1
N[2] = 2 (1+1, 2)
N[3] = 4 (1+1+1, 1+2, 2+1, 3)
그렇다면 N[4]는
1) 맨 앞에 1을 놓으면 뒤에는 3이 되어야 함
    1 + {합이 3이 되는 조합} = 1 + (1+1+1), 1 + (1+2, 2+1), 1 + (3) ---> N[3] = 4
2) 맨 앞에 2를 놓으면 뒤에는 2가 되어야 함
    2 + {합이 2가 되는 조합} = 2 + (1+1), 2 + (2) ---> N[2] = 2
3) 맨 앞에 3을 놓으면 뒤에는 1이 되어야 함
    3 + {1이 되는 조합} = 3 + (1) ---> N[1] = 1

따라서 N[4] = N[3] + N[2] + N[1] = 1 + 2 + 4 = 7

이를 N[i]로 확장하면, 아래와 같은 점화식으로 표현 가능
N[i] = N[i-1] + N[i-2] + N[i-3] 이때 4 <= i <= n
"""
def combination(n):
    if n < 0:
        return 0    # 단, 정수 0과 음수는 나타낼수 없으므로 그대로 0을 리턴한다.
    if n == 0:
        return 0
    elif n == 1:    # N[1]
        return 1
    elif n == 2:    # N[2]
        return 2
    elif n == 3:    # N[3]
        return 4
    # N[i] = N[i-1] + N[i-2] + N[i-3]
    return combination(n-1) + combination(n-2) + combination(n-3)

if __name__ == '__main__':
    for num in range(10):
        print(factorial_1(num))

    for num in range(10):
        print(factorial_2(num))

    print(muliple(10))

    n = random.sample(range(100), 10)
    print(n)
    print(sum(n))

    n2 = random.sample(range(100), 10)
    print(n2)
    print(sum_recur(n2))

    str = "abcde1edcba"
    print(palindrome(str))          # True
    print(palindrome_rucur(str))    # True

    print(func(3))
    print(func(4))

    print(combination(4), "개 입니다.")   # 7 개 입니다.
