"""
>> 동적 계획법 (Dynamic Programming)과 분할 정복 (Divide and Conquer)

1. 동적 계획법(DP, Dynamic Programming)
    - 입력 크기가 작은 부분 문제들을 먼저 해결하고, 해당 문제의 정답을 활용해 더 큰 문제의 해결에 사용.
    - '상향식 접근법'으로 '가장 최하위 문제의 답'을 구하고 '점차 위'로 올라가며 '전체 문제의 답'을 구한다.
    - 'Memoization 기법'을 사용
        ~> emoization (메모이제이션) = 프로그램 실행 시 이전에 계산한 값을 저장하여,
                                      다시 계산하지 않도록 하여 전체 실행 속도를 빠르게 하는 기술
    - 문제를 잘게 쪼갤 때, '부분적인 문제'는 '중복되어 재활용'
        ~> ex) 피보나치 수열

2. 분할 정복 (Divide and Conquer)
    - 문제를 나눌수 없을 떄까지 나누고, 각각을 풀면서 다시 합쳐 전체 문제의 해답을 얻는 알고리즘
    - '하향식 접근법'으로 '상위의 답'을 얻기 위해 아래로 내려가며 '하위의 답'을 얻는다
    - 일반적으로 '재귀 함수'로 구현
    - 문제를 잘게 나눌 때, '부분적인 문제'는 '서로 중복되지 않음'
        ~> ex) 병합 정렬, 퀵 정렬

> 동적 계획법 / 분할과 정복
<공통점>
    - 큰 문제를 잘게 나누어, 가장 작은 단위로 분할
<차이점>
    - 동적 계획법
        -- '부분 문제는 서로 중복'되어, 상위 문제 해결에 '재활용'
        -- Memoization 기법 사용 (부분 문제의 해답을 저장해서 재활용하는 최적화 기법으로 사용)
    - 분할 정복
        -- '부분 문제는 서로 중복 X'
        -- Memoization 기법 사용 안함
"""
"""
연습. 피보나치 수열: n을 입력받았을 때 피보나치 수열로 결과값을 출력하세요
"""
# 피보나치 재귀 함수 Ver.
def fibonacci_recur(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)

# 피보나치 동적 계획법 Ver.
def fibonacci_dp(n):
    cache = [0 for index in range(n+1)] # n 크기의 0으로 채워친 리스트 생성
    cache[0] = 0    # 리스트 0번째 원소는 0
    cache[1] = 1    # 리스트 1번째 원소는 1

    for i in range(2, n+1): # 2번째 원소부터 n까지 반복
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n]


if __name__ == '__main__':
    print(fibonacci_recur(10))
    print(fibonacci_dp(10))

    # 분할 정복 알고리즘의 예는 다음 챕터에서 다루는 '병합 정렬'과 '퀵 정렬'을 통해 이해

