# 큐: FIFO(First-In First-Out) 규칙의 순차적 자료구조
# 소에 비유
# Dequeue: Stack + Queue (양쪽으로 들어갔다 나올 수 있음)

# (insert) 스택의 push = 큐의 enqueue = list의 append
# (delete) 스택의 pop(마지막 값이 delete 리턴) = 큐의 dequeue(처음 값이 delete 리턴)

class Queue:
    def __init__(self):
        self.items = []  # 빈 리스트
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Q is empty")
            return None
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x