# 양방향 연결리스트(Doubly Linked List)

# 원형 양방향 연결리스트(Circlar Doubly Linked List)
# 원형 연결 리스트: 빈리스트 (dummy node)

class Node:
    def __init__(self, key = None):
        self.key = key  # 노드에 저장되는 데이터 값
        self.next = self  # 현재 노드의 다음 노드를 자기 자신으로 초기화 (초기에는 자기 자신을 가리킴)
        self.prev = self  # 현재 노드의 이전 노드를 자기 자신으로 초기화 (초기에는 자기 자신을 가리킴)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # 연결 리스트의 맨 앞 노드를 생성하여 설정 (데이터 값 없이)
        self.size = 0  # 연결 리스트의 크기 (노드 개수)를 저장
    # for문을 돌리고 싶으면 def __iter__():
    # print문을 출력하고 싶으면 def __str__():
    # 길이를 알고 싶으면 def __len__():


# Slice연산***** (매우중요)
def splice(self, a, b, x):  # a,b,x는 노드
    # 조건1: a-> ... ->b
    # 조건2: a와 b사이에 head노드와 x노드가 있으면 안됨
    ap = a.prev
    bn = b.next
    xn = x.next

    ap.next = a
    bn.prev = ap
    x.next = a
    a.prev = x
    b.next = xn
    xn.prev = b

# 원래 연결 상태: ... -> ap -> a -> b -> bn -> ...
# splice 메서드를 실행한 후의 연결 상태: ... -> ap -> a -> x -> b -> bn -> ...



# 이동연산
# - moveAfter(self, a, x): 노드a를 노드x 다음으로 이동 =>splice(a, a, x)
# - moveBefore(self, a, x): 노드a를 노드x 전으로 이동 =>splice(a, a, x.prev)

# 삽입연산
# - insertAfter(self, x, key): key값을 가지고 있는 노드를 x노드 다음에 삽입 
# = moveAfter(Node(key), x)

# - insertBefore(self, x, key): key값을 가지고 있는 노드를 x노드 전에 삽입 
# = moveBefore(Node(key), x)

# - pushFront(key) 
# = insertAfter(self.head, key)
# - pushBack(key)
# = insertBefore(self.head, key)


# 삭제연산
def search(self, key):
    v = self.head  # dummy node
    while v != self.head:
        if v.key == key:
            return v
        v = v.next
    return None
    

# 탐색연산
def search(self, key):
    v = self.head
    while v.next != self.head:
        if v.key == key:
            return v
        v = v.next
    return None

# 삭제연산
def remove(x):  # 노드X를 삭제
    if x == None or x == self.head:
        return
    x.prev.next = x.next
    x.next.prev = x.prev
    del x

# popFront
# popBack

# join: 리스트 두개를 합치는 거 
# split: 하나의 연결리스트를 노드를 기준으로 두개로 쪼개는 것

# 연산의 시간 복잡도
# n개 노드를 갖는 이중 연결리스트
# search(key): => O(n)
# splice(a, b, x): 6개 링크 수정 => O(1)

# moveAfter/Before(a, x) => splice O(1)
# insertAfter/Before(x, key) => splice O(1)
# pushFront/Bacl(key) => spliceO(1) 

# remove(x) => O(1)
# popFront/Back() => O(1)





# 해시 테이블: Hash Table: 매우 빠른 평균 삽입,삭제,탐색연산 제공

# 조건
# 1. Table: List
# 2. Hash function
# 3. Collision resolution method


# 2. 해시 함수(Hash function)
# 좋은 Hash function: 1. less collision(최대한 적은 충돌)    2. fast compution(빠른 계산)

# 충돌 회피 방법(Collision resolution method)
# - open addressing: 선형 탐사(Linear Probing): 비어있는 슬롯을 찾음
# 이차 탐사(Quadratic Probing): 일정한 간격을 가지며 슬롯을 찾음. 선형탐사 보다 데이터를 줄일 수 있음
# 이중 해싱(Double Hashing): 두 개의 해시 함수를 사용. 함수를 사용하여 다음 위치를 계산하여 빈 슬롯을 찾음


# - chaining
# set, search, remove 연산

# set함수
# set(key, value = None):
# 1. key값이 H에 있으면 value를 update
# 2. key값이 H에 없으면 (key, value)을 insert


# search 연산
def find_slot(key):  # key값이 있으면 slot번호 리턴/ key값이 없다면 key값이 삽입될 slot번호 리턴
    i = f(key)
    start = i
    while H[i] == occupied and H[i].key != key:  # i가 차있거나 내가 찾는 값이 아니면
        i = (i+1) % m
        if i == start:
            return Full
    return i

# set 연산
def set(key, value = None):
    i = find_slot(key)
    if i == Full:  # H를 키워야 함
        return None
    if H[i].is_occipied:
        H[i].value = value
    else:
        H[i].key = value, H[i].value = key.value
    return key

# remove 연산
