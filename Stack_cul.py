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
    possible = list('0123456789.()+-*/')            # 수식에 입력 가능한 문자들의 리스트
    integers = list('0123456789')                   # 0~9까지의 정수들의 리스트
    operators = list('+-*/')                        # 수식에 사용될 연산자들의 리스트
    s = Stack()

    for i in range(len(expr)):
        if expr[i] not in possible:                 # 입력 가능한 문자가 아닐 경우 해당 위치 반환
            return i
        elif i == 0 and expr[i] in operators:       # 연산자가 수식의 가장 앞에 위치할 경우 해당 위치 반환 (ex. *123+4...)
            return i
        elif expr[i] in operators:
            if i + 1 == len(expr):                  # 연산자 뒤에 피연산자가 오지 않고 수식이 끝날 경우 위치 반환 (ex. 1+2+)
                return i
            else:                                   # 연속해서 연산자가 위치할 경우 해당 위치 반환 (ex. 1+*2...)
                if expr[i + 1] in operators:
                    return i + 1
        elif expr[i] == '(':                        # 수식에서 '('가 발견되었을 때
            if expr[i - 1] in integers and i != 0:  # 여는 괄호('(') 앞에 정수가 올 경우 해당 위치 반환
                return i
            else:
                if s.isEmpty():                     # 스택에 이미 값이 들어있으면 해당 위치 반환
                    s.push('(')                     # 스택이 비어있으면 push
                else:
                    return i
        elif expr[i] == ')':                        # 수식에서 ')'가 발견되었을 때
            if s.isEmpty():                         # 스택이 비어있으면
                return i                            # 해당 위치 반환
            elif expr[i + 1] in integers and i != len(expr) - 1:
                return i + 1                        # 닫는 괄호(')') 뒤에 정수가 올 경우 해당 위치 반환
            else:
                s.push(')')                         # 스택이 비어있지 않다면 해당 값을 스택에 push

    if not s.isEmpty():                             # 수식에 '('는 존재 하지만 ')'는 존재하지 않는 경우
        if s.pop() == '(':
            return len(expr)                        # 수식의 마지막 위치를 반환
 
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

# recognize_Operands( )
def recognize_Operands(infix):
    numbers = list('0123456789.')                       # 실수 계산기 이므로, 모든 피연산자는 0~9인 정수와 .으로 이루어진다
    recognized = []                                      # 수식의 숫자들을 피연산자로 인식하여 다시 담아 줄 리스트

    i = 0
    while i < len(infix):
        j = 1
        if infix[i] in numbers:                         # 연산자가 아닐 경우, 즉 숫자 또는 .일 경우
            while i + j < len(infix):                   # 해당 요소의 다음 요소도 숫자 또는 .인지를 판별하고
                if infix[i + j] in numbers:
                    j += 1
                else:
                    break
            recognized.append(''.join(infix[i:i + j]))   # 이들을 하나로, 즉 하나의 숫자로 인식 할 수 있도록 묶어준다
            i += j
        else:                                           # 연산자일 경우엔 리스트에 바로 추가해준다
            recognized.append(infix[i])
            i += 1
    return recognized

# 사용자가 입력한 수식에서 피연산자(실수)를 인식하기 위한 함수이다.
# 우선 해당 프로그램은 실수 계산기 이므로, 모든 피연산자는 0~9사이의 정수와 .만으로 이루어진다.
# 따라서 이를 인식하기 위한 리스트 numbers와 피연산자로 인식된 숫자들을 담아 줄 리스트 recognized를 선언해준다.
# ( ex. recognized = [12.9 , 30.1, 17.89, 48.66] )

# 다름으로 입력 된 중위 표기식(infix)의 앞에서부터 돌며 연산자가 발견될 경우, 리스트에 바로 추가해준다.
# 숫자 또는 .이 발견될 경우에는 해당 요소의 다음 요소도 숫자 또는 .인지를 판별한다.
# 맞을 경우 연산자가 나올 때 까지 위의 과정을 반복하며 이들이 하나의 숫자(피연산자)로 인식될 수 있도록 묶어주고,
# 그 상태로 recognized에 추가해준다.
# 위의 작업들이 모두 마무리 되고 나면 recognized를 반환해준다.


#  in2post( )
def in2post(infix):
    s = Stack()                                             # 스택 생성
    postfix = []                                            # 후위 표기법으로 바뀐 수식을 담아 줄 리스트
    for i in infix:
        if i == '(':                                        # 여는 괄호('(')일 경우 스택에 바로 push
            s.push(i)
        elif i == ')':                                      # 닫는 괄호(')')일 경우
            while s.top() != '(':                           # '('와 ')'사이의 연산자들을 모두 postfix 리스트에 추가
                postfix.append(s.pop())
            s.pop()                                         # 그리고 stack에 들어있던 '('는 삭제. (후위 표기법은 괄호를 표시하지 않으므로)
        elif i in priority:                                 # '+ - * /'일 경우
            while not s.isEmpty():                          # 스택이 비어 있지 않을 때
                if priority[s.top()] >= priority[i]:        # 스택의 top에 해당하는 연산자의 우선순위가 비교할 연산자의 우선순위보다 크거나 같을 경우
                    postfix.append(s.pop())                 # 해당 연산자(top)를 postfix 리스트에 추가한다
                else:
                    break
            s.push(i)                                       # 스택이 비어있을 경우엔 해당 연산자를 스택에 바로 push
        else:                                               # 피연산자(숫자)의 경우 리스트에 바로 추가
           postfix.append(i)
    while not s.isEmpty():                                  # '('보다 밑 스택에 남아있던 연산자들을
        postfix.append(s.pop())                             # 모두 리스트에 추가해준다

    return postfix                                          # 변환된 후위 표기식을 반환한다

# 중위 표기법으로 표기된 수식을 후위 표기법으로 바꿔줄 함수이다.
# 우선 하나의 스택과 후위 표기법으로 변환된 수식을 담아 줄 리스트 postfix를 선언해준다.

# 다음으로 입력 된 중위 표기식(infix)의 앞에서부터 돌며

# 1) 숫자(피연산자)가 발견될 경우 postfix에 바로 추가해준다.
# 2) 연산자(+ - * /)가 발견될 경우 스택이 비어 있으면 해당 연산자를 바로 스택에 push해준다
# 스택이 비어있지 않다면 해당 연산자와 스택의 top에 해당하는 연산자의 우선순위를 비교하고,
# 후자의 우선순위가 더 높을 경우 전자를 postfix에 추가해준다.
# 3) 여는 괄호가 발견 될 경우 스택에 바로 push해준다.
# 4) 닫는 괄호가 발견 될 경우 여는 괄호와 닫는 괄호 사이에 존재하는 연산자들을 모두 postfix에 추가해준다.
# 그후 postfix에 남아있던 여는 괄호는 삭제해준다.(후위 표기법은 괄호를 따로 표기하지 않기 때문)
# 5) 마지막으로 여는 괄호보다 밑 스택에 남아있던 연산자들을 차례로 postfix에 추가해주고, postfix를 반환해준다.

# 이때 연산자의 우선순위는 다음과 같이 설정해준다.


# post_Cal()
def post_Cal(postfix):
    s = Stack()

    for i in postfix:
        if i in priority:                                   # 연산자일 경우
            num1 = s.pop()                                  # 스택에 쌓여 있던 두 피연산자(숫자)를 꺼내
            num2 = s.pop()
            if i == '+':                                    # 덧셈(+)
                s.push(num2 + num1)
            elif i == '-':                                  # 뺄셈(-)
                s.push(num2 - num1)
            elif i == '/':                                  # 나눗셈(/)
                s.push(num2 / num1)
            elif i == '*':                                  # 곱셈(*)
                s.push(num2 * num1)                         # 두 피연산자에 대해 각 연산자에 해당하는 연산을 수행한 값을 스택에 push해준다

        else:                                               # 숫자일 경우
            s.push(float(i))                                # 해당 숫자를 float 자료형으로 스택에 push(실수 계산기이므로)

    return s.pop()                                          # 계산된 값을 반환한다

# 후위 표기법으로 변환된 수식을 계산하여 결과값을 반환하게 될 함수이다.
# 우선 후위 표기식(postfix)의 앞에서부터 돌며 숫자가 발견되면 해당 숫자를 float자료형으로 스택에 push해준다.
# 해당 프로그램은 '실수 계산기' 이기 때문이다.
# 연산자가 발견되면 스택에 쌓여 있던 두 피연산자를 꺼내고,
# 두 피연산자에 대해 각 연산자에 해당하는 연산(+ - * /)을 수행하고 그 결과값을 다시 스택에 push해준다.
# 수식의 모든 요소에 대해 위와 같은 과정을 반복하고 최종 결과값을 스택에서 꺼내 반환해준다.
