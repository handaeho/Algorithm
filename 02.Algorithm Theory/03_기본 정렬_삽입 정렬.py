"""
>> 삽입 정렬 (insertion sort) 란?
    - 삽입 정렬은 '두 번째 인덱스부터 시작'
    - 해당 인덱스(key 값) '앞에 있는 데이터(B)부터 비교'해서 key 값이 더 작으면, B값을 뒤 인덱스로 복사
    - 이를 key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동

>> 삽입 정렬의 시간 복잡도
    - 반복문이 두 개 O(n^2)
    - 최악의 경우, n * (n - 1) / 2
    - 완전 정렬이 되어 있는 상태라면 최선은 O(n)
"""
"""
연습. 데이터가 네개 일때 동작하는 선택 정렬 알고리즘을 함수로 만들어보세요

데이터 갯수에 따라 복잡도가 떨어지는 것은 아니므로, 네 개로 바로 로직을 이해해보자.
데이터가 네 개 일때, 
    예: data_list = [9, 3, 2, 5]
        - 처음 한번 실행하면, key값은 9, 인덱스(0) - 1 은 0보다 작으므로 끝: [9, 3, 2, 5]
        - 두 번째 실행하면, key값은 3, 9보다 3이 작으므로 자리 바꾸고, 끝: [3, 9, 2, 5]
        - 세 번째 실행하면, key값은 2, 9보다 2가 작으므로 자리 바꾸고, 다시 3보다 2가 작으므로 끝: [2, 3, 9, 5]
        - 네 번째 실행하면, key값은 5, 9보다 5이 작으므로 자리 바꾸고, 3보다는 5가 크므로 끝: [2, 3, 5, 9]
"""
import random
random.seed(428)


def insertion_sort(data_list):
    for i in range(len(data_list) - 1): # 삽입 정렬은 '두 번째 인덱스부터 시작' 그리고 key = i
        # 앞에 있는 원소와 비교하므로 key의 그 다음 원소부터 거꾸로 처음 원소까지 반복
        for index in range(i + 1, 0, -1):
            if data_list[index] < data_list[index - 1]: # 뒤의 원소가 앞의 원소보다 작다면
                data_list[index], data_list[index-1] = data_list[index-1], data_list[index] # 위치 교환
            else:   # 뒤의 원소가 앞의 원소보다 작지 않다면 정렬이 끝난 것이므로
                break
    return data_list


if __name__ == '__main__':
    data_list = random.sample(range(100), 50)
    print(data_list)
    print(insertion_sort(data_list))