class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)
    
a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c


# 한방향 연결리스트: pushFront(맨 앞에 원소 추가), pushBack(맨 뒤에 원소 추가)
class Node:
    def __init(self, key):
        self.key = key  # 노드의 데이터 값
        self.next = None  # 다음 노드

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드
        self.size = 0  # 리스트의 첫 번째 노드

    def pushFront(self, key):
        new_node = Node(key)  # 새로운 노드를 생성하고 데이터 값 할당
        new_node.next = self.head  # 새로운 노드의 다음 노드로 현재 첫 번째 노드를 가리킴
        self.head = new_node  # 리스트의 첫 번째 노드를 새로운 노드로 변경
        self.size += 1  # 리스트 크기 증가

    def pushBack(self, key):
        new_node = Node(key)  # 새로운 노드를 생성하고 데이터 값 할당
        if self.size == 0:   # 리스트가 비어있는 경우
            self.head = new_node  # 첫 번째 노드로 새로운 노드를 설정
        else:
            tail = self.head
            while tail.next != None:  # 마지막 노드 찾을 때까지 반복
                tail = tail.next  # 다음 노드로 이동
            tail.next = new_node  # 마지막 노드의 다음 노드로 새로운 노드 설정
        self.size += 1  # 리스트 크기 증가


# 한방향 연결리스트: popFront(맨 앞에 원소 삭제), popBack(맨 뒤에 원소 삭제)
def popFront(self):
    if len(self) == 0:   # 리스트가 비어있을 경우
        return None  # 아무 작업 없이 None 반환
    else: 
        x = self.head   # 첫 번째 노드 저장
        key = x.key    # 첫 번째 노드의 데이터 값을 저장
        self.head = x.next  # 첫 번째 노드를 다음 노드로 변경하여 제거
        self.size -= 1   # 리스트 크기 감소
        del x  # 제거된 노드 메모리에서 해제
        return key   # 제거된 노드의 데이터 값을 반환
    
def popBack(self):
    if len(self) == 0:  # 리스트가 비어있을 경우
        return None  # 아무 작업 없이 None 반환
    else:
        prev, tail = None, self.head  # 이전 노드와 마지막 노드를 초기화
        while tail.next != None:  # 마지막 노드까지 반복
            prev = tail   # 이전 노드를 현재 노드로 변경
            tail = tail.next  # 다음 노드로 이동

    if len(self) == 1:  # 리스트에 노드가 하나만 있는 경우
        self.head = None  # 첫 번째 노드를 None으로 설정하여 리스트를 비움
    else:
        prev.next = tail.next   # 이전 노드의 다음 노드를 None으로 설정하여 마지막 노드를 제거

    key = tail.key   # 마지막 노드의 데이터 값을 저장
    del tail  # 제거된 노드 메모리에서 해제
    self.size -=1  # 리스트 크기 감소
    return key  # 제거된 노드의 데이터 값을 반환


# 한방향 연결리스트 추가연산: 탐섹(search) + 제너레이터(generator)
 
# 단일 연결 리스트에서 특정 값을 가지는 노드를 검색하는 search 메서드
def search(self, key):  
    v = self.head  # 첫 번째 노드부터 시작하여 검색 시작
    while v != None:  # 노드가 끝까지 도달할 때까지 반복
        if v.key == key:  # 현재 노드의 데이터 값이 찾는 값과 같다면
            return v  # 해당 노드 반환 (검색 성공)
        v = v.next  # 다음 노드로 이동하여 검색 계속
    return None  # 모든 노드를 검색해도 찾는 값이 없다면 None 반환 (검색 실패)

#  단일 연결 리스트에서 반복자(iterator)를 생성하는 메서드
def __iterator__(self):
    v = self.head  # 첫 번째 노드부터 시작하여 반복 시작
    while v != None:  # 노드가 끝까지 도달할 때까지 반복
        yield v  # 현재 노드를 제너레이터로 내보내고 일시적으로 실행을 중단 (yield = return)
        v = v.next  # 다음 노드로 이동하여 반복 계속

# 이렇게 하면 for 루프나 다른 반복 구조를 사용하여 리스트의 각 노드를 순회할 수 있음.