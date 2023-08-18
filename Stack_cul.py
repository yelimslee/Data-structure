# 계산기 만들기 코드
# 계산식을 입력하면 그 결과 값을 돌려주는 프로그램을 작성한다.

# ⚡️ 조건
# 사용되는 연산자는 + - * / ( ) 이다.
# 입력에 사용되는 수는 실수이다.
# 수식에서 괄호는 최대 1회만 사용한다. 또한 겹쳐진 괄호는 쓰지 않는다.
# 잘못된 수식이 입력된다면 어느 위치에 문제가 있는지 알려준다.

# 프로그램의 전체 프로세스는 다음과 같다.

# 1) 입력 받은 수식의 오류 탐색
# 2) (오류가 발견되지 않았다면) 수식의 피연산자 식별
# 3) 입력 받은 수식(infix)을 후위 표기법(postfix)으로 변경
# 4) 후위 표기법으로 변경된 수식의 계산 결과값 도출

# ⚡️ 활용방안

# 주어진 수식을 왼쪽에서 오른쪽으로 스캔하며, 피연산자는 스택에 저장하고,
# 연산자이면 필요한 수만큼의 피연산자를 스택에서 꺼내 연산을 실행하고,
# 연산의 결과를 다시 스택에 저장하는 방식으로 계산기가 실행되도록 프로그램을 작성하였다.

# Stack()
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(stack.items)
    
    def isEmpty(self):
        return self.__len__() == 0
    

# 프로세스를 실행하기 위한 함수들

# search_Error( ): 입력 받은 수식의 오류를 찾아내는 함수
def search_Error(expr):
    possible = list('0123456789.()+-*/')  # 수식에 입력 가능한 문자들의 리스트
    integers = list('0123456789')  # 0~9까지의 정수들의 리스트
    operators = list('+-*/')  # 수식에 사용될 연산자들의 리스트
    s = Stack()

    for i in range(len(expr)):
        if expr[i] not in possible:   # 입력 가능한 문자가 아닐 경우 해당 위치 반환
            return i 
        elif i == 0 and expr[i] in operators:  # 연산자가 수식의 가장 앞에 위치할 경우 해당 위치 반환 (ex. *123+4...)
            return i
        elif expr[i] in operators:
            if i+1 == len(expr):  # 연산자 뒤에 피연산자가 오지 않고 수식이 끝날 경우 위치 반환 (ex. 1+2+)
                return i
            else:           # 연속해서 연산자가 위치할 경우 해당 위치 반환 (ex. 1+*2...)
                if expr[i+1] in operators:
                    return i + 1
        elif expr[i] == '(':  # 수식에서 '('가 발견되었을 때
            if expr[i-1] in integers and i != 0:  # 여는 괄호('(') 앞에 정수가 올 경우 해당 위치 반환
                return i
            else:
                if s.isEmpty():  # 스택에 이미 값이 들어있으면 해당 위치 반환
                    s.push('(')  # 스택이 비어있으면 push
                else:
                    return i
        elif expr[i] == ')':  # 수식에서 ')'가 발견되었을 때
            if s.isEmpty():  # 스택이 비어있으면
                return i  # 해당 위치 반환
            elif expr[i+1] in integers and i != len(expr) -1:
                return i+1  # 닫는 괄호(')') 뒤에 정수가 올 경우 해당 위치 반환
            else:
                s.push(')')  # 스택이 비어있지 않다면 해당 값을 스택에 push

    if not s.isEmpty():  # 수식에 '('는 존재 하지만 ')'는 존재하지 않는 경우
        if s.pop() == '(':
            return len(expr)  # 수식의 마지막 위치를 반환
 
# 입력 받은 수식(expr)에서 오류가 발생한 부분을 찾아 낼 함수이다.
# 우선 수식에 입력 가능한 문자들(0123456789.()+-*/)의 리스트 possible
# 0~9까지의 정수들의 리스트 integers
# 수식에 사용될 연산자들의 리스트 operators를 선언해준다.
# 그 후 오류가 발생하는 case를 나눠 오류를 찾아낸다. 케이스는 다음과 같다.

# ⚡️ case
# 1) 입력 가능한 문자가 아닐 경우
# 2) 연산자가 수식의 가장 앞에 위치할 경우 (ex. 123+4...)
# 3) 연산자 뒤에 피연산자가 오지 않고 수식이 끝날 경우 (ex. 1+2+)
# 4) 연속해서 연산자가 위치할 경우 (ex. 1+2...)
# 5) 수식에서 여는 괄호 앞에 정수가 올 경우, 또는 스택에 이미 값이 들어있을 경우 (괄호는 최대 1번만 사용 가능한데, 이 경우는 1번이상 사용 되었다는 의미이므로)
# 6) 수식에서 닫는 괄호 뒤에 정수가 올 경우, 또는 스택이 비어있을 경우 (닫는 괄호를 쓸려면 여는 괄호가 이미 쓰여 있어야 하는데 이 경우는 그렇지 않다는 의미이므로)
# 7) 수식에 여는 괄호는 존재하지만, 닫는 괄호는 존재하지 않는 경우

# 1~7까지 각각의 경우에 해당하는 위치, 즉 오류가 발생한 위치를 반환한다.