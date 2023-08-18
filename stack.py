# Stack: first in last out (선입 후출) ex.말미잘
# 삽입: push(=append)  삭제: pop(=pop)


class Stack:
    def __init__(self):  # self라는 매개변수를 만듦.
        self.items = []  # 데이터 저장을 위한 리스트 준비 *필수로 있어야 하는 메소드

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:   # pop 할 아이템이 없으면 IndexError 발생
            print("Stack is empty")

    def top(self):   # top 메소드: 맨 마지막 값을 리턴
        try: 
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    
    def __len__(self):   # len()로 호출하면 stack의  item 수 반환
        return len(self.items)
    
S = Stack()
S.push(10)
S.push(2)
print(S.pop())  # 2
print(S.top())  # 10
print(len(S))  # 1
