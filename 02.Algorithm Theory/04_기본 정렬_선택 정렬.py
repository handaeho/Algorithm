"""
>> 선택 정렬 (selection sort) 란?
    다음과 같은 순서를 반복하며 정렬하는 알고리즘
        1. 주어진 데이터 중, '최소값을 찾음'
        2. 해당 '최소값'을 데이터 '맨 앞에 위치한 값과 교체'함
        3. 맨 앞의 위치를 뺀 '나머지 데이터를 동일한 방법으로 반복'함

1) 데이터가 두 개 일때
    예: dataList = [9, 1]
    = data_list[0] > data_list[1] 이므로 datalist[0] 값과 data list[1] 값을 교환
2) 데이터가 세 개 일때
    예: data_list = [9, 1, 7]
    = 처음 한번 실행하면, 1, 9, 7 이 됨
      두 번째 실행하면, 1, 7, 9 가 됨
3) 데이터가 네 개 일때
    예: data_list = [9, 3, 2, 1]
    = 처음 한번 실행하면, 1, 3, 2, 9 가 됨
      두 번째 실행하면, 1, 2, 3, 9 가 됨
      세 번째 실행하면, 변화 없음

>> 즉,
1) for stand in range(len(data_list) - 1) 로 반복
2) lowest = stand 로 놓고,
3) for num in range(stand, len(data_list))로 stand 이후부터 반복
        내부 반복문 안에서 data_list[lowest] > data_list[num] 이면,
            lowest = num
4) data_list[num], data_list[lowest] = data_list[lowest], data_list[num]

>> 선택 정렬의 시간 복잡도
    - 반복문이 두 개 O(n^2)
    - 실제로 상세하게 계산하면, n * (n - 1) / 2
"""
import random
random.seed(428)


def selection_sort(data):
    for stand in range(len(data) - 1):  # 맨 마지막 데이터는 할 필요 없이 자동적으로 큰값이 갈 것이므로
        lowest = stand  # 주어진 데이터 중, 최소값을 저장
        for index in range(stand + 1, len(data)):   # 현재 원소의 다음 원소부터 끝까지
            if data[lowest] > data[index]:  # 최소값으로 저장한 원소가 더 크다면
                lowest = index  # 최소값 변경
            data[lowest], data[stand] = data[stand], data[lowest]   # 위치 교환
    return data


if __name__ == '__main__':
    data = random.sample(range(100), 50)
    print(data)
    print(selection_sort(data))


