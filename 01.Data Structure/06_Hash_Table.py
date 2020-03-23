"""
1. 해쉬 구조
    Hash Table: 키(Key)에 데이터(Value)를 저장하는 데이터 구조
        Key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
        파이썬 딕셔너리(Dictionary) 타입이 해쉬 테이블의 예: Key를 가지고 바로 데이터(Value)를 꺼냄
        보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용 (공간과 탐색 시간을 맞바꾸는 기법)
        단, 파이썬에서는 해쉬를 별도 구현할 이유가 없음 - 딕셔너리 타입을 사용하면 됨

2. 알아둘 용어
    해쉬(Hash): 임의 값을 고정 길이로 변환하는 것
    해쉬 테이블(Hash Table): 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
    해싱 함수(Hashing Function): Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
    해쉬 값(Hash Value) 또는 해쉬 주소(Hash Address): Key를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 Key에 대한 데이터 위치를 일관성있게 찾을 수 있음
    슬롯(Slot): 한 개의 데이터를 저장할 수 있는 공간
    저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음
"""
# Hash Table
hash_table = list([0 for i in range(10)])
print(hash_table)   # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Hash Function
def hash_func(key):
    """
    mod 연산으로 나머지 값을 사용해 해쉬 함수 연산
    key의 길이가 10이든 100이든 10000이든 관계없이 나머지 값을 사용해서
    임의의 길이 데이터를 고정된 길이의 데이터로 변환 할 수 있다.

    고정 길이 데이터 = 해시 값(해쉬 주소)
    """
    return key % 5

# Hash Table에 저장
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'
data4 = 'Anthor'

# ord(): 문자의 ASCII(아스키)코드 리턴. 문자를 해싱 하기위해 아스키 코드 사용
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))      # 65 68 84
print(ord(data1[0]), ord(data4[0]))                     # 65 65
print(ord(data1[0]), hash_func(ord(data1[0])))          # 65 0  ~> 키 ord(data1[0])에 대한 해쉬 값(주소)은 0

# Ex) 데이터와 값을 넣으면 해당 데이터에 대한 키를 찾아서, 해당 key에 대응하는 해쉬주소에 value를 저장
def storage_data(data, value):
    key = ord(data[0])              # key는 ord(data[0])
    hash_addr = hash_func(key)      # key의 나머지를 사용해 해쉬 주소 계산
    hash_table[hash_addr] = value   # 해쉬 테이블의 해쉬 주소에 해당하는 자리에 value 저장

storage_data('Andy', '01012345678')
storage_data('Dave', '01011112222')
storage_data('Trump', '01099998888')

# 해쉬 테이블에서 데이터 읽어오기
def get_data(data):
    key = ord(data[0])
    hash_addr = hash_func(key)
    return hash_table[hash_addr]

print(get_data('Andy'))     # 01012345678

# 연습1: 리스트 변수를 활용해서 해쉬 테이블 구현해보기
# 해쉬 함수: key % 8
# 해쉬 키 생성: hash(data)
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)   # 파이썬에는 hash() 함수가 내장되어 있음. 단 실행할 때마다 이 값이 변할 수 있으니 주의.

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_addr = hash_function(get_key(data))
    hash_table[hash_addr] = value

def read_data(data):
    hash_addr = hash_function(get_key(data))
    return hash_table[hash_addr]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print(read_data('Andy'))            # 01033232200
print(hash_table)                   # [0, 0, 0, 0, 0, 0, '0102030200', '01033232200']

#  충돌(Collision) 해결 알고리즘 (좋은 해쉬 함수 사용하기)
# ~> 해쉬 테이블의 가장 큰 문제는 충돌(Collision) 또는 해쉬 충돌(Hash Collision)이라고 부릅니다.

# 1. Chaining 기법
# ~> 개방 해싱 또는 Open Hashing 기법 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
# 충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법

# 연습2: 연습1의 해쉬 테이블 코드에 Chaining 기법으로 충돌해결 코드를 추가해보기
# 해쉬 함수: key % 8
# 해쉬 키 생성: hash(data)
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)                               # 데이터를 해싱하여 키로 바꾸고
    hash_addr = hash_function(index_key)                    # 해쉬 테이블에서 해쉬 값(주소)을 구한다.
    if hash_table[hash_addr] != 0:                          # 만약 데이터에 대한 해쉬테이블의 해쉬값이 0이 아니라면(데이터가 들어가 있다면)
        for index in range(len(hash_table[hash_addr])):     # 해쉬 테이블에서 해당 데이터가 있는 해쉬 주소 길이만큼(그 주소에 있는 데이터 개수만큼)
           if hash_table[hash_addr][index][0] == index_key: # 해쉬 테이블에서 해당 해쉬 값을 가진(해쉬 주소에 있는) 데이터는 [데이터의 해쉬값(index_key), value] 형태이므로
                                                            # 0번째. 즉, 데이터의 해쉬 값이 해당 데이터의 인덱스 키와 같으면 내가 넣고자 하는 데이터가 이미 있는 것이므로
                hash_table[hash_addr][index][1] = value     # 해쉬 테이블의 해쉬 값의 인덱스 1번째(value)를 value로 바꿈(즉, 기존 value를 새로운 value로 덮어쓴다)
                return
        hash_table[hash_addr].append([index_key, value])    # 내가 넣고자 하는 데이터가 해쉬 테이블의 해당 해쉬 주소에 없다면 해당 데이터의 인덱스 키와 데이터 값([데이터의 인덱스 키, value])을 해쉬 테이블의 그 주소 뒤에 append
    else:                                                   # 해쉬테이블의 해쉬값이 0이라면, 데이터가 없는 것이므로
        hash_table[hash_addr] = [[index_key, value]]        # 그 해쉬값(주소)에 데이터의 인덱스 키와 데이터 값을 넣음

def read_data(data):
    index_key = get_key(data)                                 # 읽고자 하는 데이터를 해싱하여 키로 바꾸고
    hash_addr = hash_function(index_key)                      # 그 키에 해당하는 해쉬 주소를 구한다.
    if hash_table[hash_addr] != 0:                            # 해쉬 테이블에서 그 주소에 해당하는 곳이 0이 아니라면(비어있지 않으면)
        for index in range(len(hash_table[hash_addr])):       # 그 주소에 들어있는 해쉬 주소 길이만큼(데이터 개수만큼)
            if hash_table[hash_addr][index][0] == index_key:  # 만약 테이블의 주소에있는 데이터의 0번째 값이 내가 원하는 데이터의 인덱스 키라면
                return hash_table[hash_addr][index][1]        # 그곳에 있는 value를 리턴
        return None                                           # 찾았는데 없다면 None
    else:
        return None                                           # 비어있다면 None


save_data('Dd', '1201023010')
save_data('Data', '3301023010')
print(read_data('Dd'))

print(hash_table)
# ~> [0, 0, 0, 0, 0, [[7483978537429328437, '3301023010']], [[-1420174019513410490, '1201023010']], 0]
# 앞의 7483...., -14201....는 해당 데이터의 index_key
# 뒤의 3301..., 1201...은 데이터의 value

# 2. Linear Probing 기법
# 폐쇄 해슁 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
# 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
# 저장공간 활용도를 높이기 위한 기법

# 연습3: 연습1의 해쉬 테이블 코드에 Linear Probling 기법으로 충돌해결 코드를 추가해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)
hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)                                   # 데이터를 해싱하여 키를 생성하고
    hash_addr = hash_function(index_key)                        # 그에 맞는 해시 값(해시 주소)를 연산한다.
    if hash_table[hash_addr] != 0:                              # 해시 테이블의 해시 주소가 0이 아니라면(비어있지 않다면)
        for index in range(hash_addr, len(hash_table)):    # 해당 해시 주소부터 해시 테이블 끝까지(빈 주소를 찾기위해)
            if hash_table[index] == 0:                          # 비어있는 해시 값(해시 주소)을 찾으면
                hash_table[index] = [index_key, value]          # 그곳에 [데이터의 인덱스 키, value]를 넣는다.
                return
            elif hash_table[index][0] == index_key:             # 만약 데이터의 인덱스 키와 같은 것을 찾는다면,
                hash_table[index][1] = value                    # 이미 데이터가 있는것이므로 새로운 value를 덮어쓴다.
                return
    else:                                                       # 해시 테이블의 해시 키(해시 주소)가 0이라면(비어있다면)
        hash_table[hash_addr] = [index_key, value]              # 해당 해시 키(해시 주소)에 [데이터의 인덱스 키, value]를 넣는다.

def read_data(data):
    index_key = get_key(data)                                   # 데이터를 해싱하여 키를 생성하고
    hash_addr = hash_function(index_key)                        # 그에 맞는 해시 값(해시 주소)를 연산한다
    if hash_table[hash_addr] != 0:                              # 해시 테이블의 해시 주소가 비어있지 않다면
        for index in range(hash_addr, len(hash_table)):         # 해당 주소부터 테이블 끝까지
            if hash_table[index] == 0:                          # 만약 해시 테이블의 해시 주소가 비어있다면(데이터가 저장된 적이 없다면)
                return None                                     # None 리턴
            elif hash_table[index][0] == index_key:             # 해시테이블에서 해시 값(해시 주소)의 0번째가 데이터의 인덱스 키라면
                return hash_table[index][1]                     # 그 value 리턴
    else:                                                       # 해시 테이블의 해시 주소가 비어있다면
        return None                                             # None 리턴


print(hash('dk') % 8)
print(hash('da') % 8)
print(hash('dc') % 8)

save_data('dk', '01200123123')
save_data('da', '3333333333')
print(read_data('dc'))
print(hash_table)
# [[966660765956178000, '3333333333'], 0, 0, 0, [-9052281577616304268, '01200123123'], 0, 0, 0]

# 해쉬 함수와 키 생성 함수
# 파이썬의 hash() 함수는 실행할 때마다, 값이 달라질 수 있음
# 유명한 해쉬 함수들이 있음: SHA(Secure Hash Algorithm, 안전한 해시 알고리즘)
# 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능

# 1. SHA-1
import hashlib

data = 'test'.encode()  # byte 타입으로 변환
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)  # a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

# 2. SHA-256
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)  # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

# 연습4: 연습2의 Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수를 sha256 해쉬 알고리즘을 사용하도록 변경해보기
# 1. 해쉬 함수: key % 8
# 2. 해쉬 키 생성: hash(data)
hash_table = list([0 for i in range(8)])

def get_key(data):
    hash_object = hashlib.sha3_256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)                               # SHA-1로 변환된 키값을 데이터의 인덱스 키로
    hash_addr = hash_function(index_key)                    # 데이터의 인덱스 키를 사용해 해쉬 테이블의 해쉬 값(해쉬 주소) 연산
    if hash_table[hash_addr] != 0:                          # 해쉬 테이블에서 해당 주소가 0이 아니면(비어있지 않다면)
        for index in range(hash_addr, len(hash_table)):     # 현재 해쉬 값(주소)부터 해쉬 테이블 끝까지
            if hash_table[index] == 0:                      # 해쉬 테이블에서 현재 슬롯이 0이라면(비어있다면)
                hash_table[index] = [index_key, value]      # 슬롯에 [데이터의 인덱스 키, value]를 넣는다.
                return
            elif hash_table[index][0] == index_key:         # 현재 슬롯의 인덱스 키가 해당 데이터의 인덱스 키와 같다면
                hash_table[index][1] = value                # 이미 있는 것이므로 새로운 value로 덮어쓴다
                return
    else:
        hash_table[hash_addr] = [index_key, value]          # 해쉬 테이블의 해쉬 값(해쉬 주소)가 비어있다면 [데이터의 인덱스 키, value] 저장


def read_data(data):
    index_key = get_key(data)                               # SHA-1로 변환된 키값을 데이터의 인덱스 키로
    hash_addr = hash_function(index_key)                    # 데이터의 인덱스 키를 사용해 해쉬 테이블의 해쉬 값(해쉬 주소) 연산
    if hash_table[hash_addr] != 0:                          # 해쉬 테이블에서 해당 주소가 0이 아니면(비어있지 않다면)
        for index in range(hash_addr, len(hash_table)):     # 현재 해쉬 값(주소)부터 해쉬 테이블 끝까지
            if hash_table[index] == 0:                      # 해쉬 테이블에서 현재 슬롯이 0이라면(비어있다면)
                return None                                 # None 리턴
            elif hash_table[index][0] == index_key:         # 현재 슬롯의 인덱스 키가 해당 데이터의 인덱스 키와 같다면
                return hash_table[index][1]                 # 현재 슬롯의 value 리턴
    else:
        return None                                         # 해쉬 테이블의 해쉬 값(해쉬 주소)가 비어있다면 None 리턴


print (get_key('db') % 8)
print (get_key('da') % 8)
print (get_key('dh') % 8)

save_data('da', '01200123123')
save_data('dh', '3333333333')
print(read_data('dh'))
