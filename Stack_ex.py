# 스택 예1: 괄호 맞추기
# "(()))(" => X
# 문제 입력: 왼쪽, 오른쪽 괄호의 문자열 
# 출력: 괄호 쌍이 맞춰져있으면 True, 아니면 False

S = Stack()
for p in parseg:
    if p == '(':
        S.push(p)
    elif p == ")":
        S.pop()
    else:
        print("Not allowed symbol")

if len(S) > 0:
    return False
else:
    return True

# 스택 예2: 계산기 코드 작성
# 리스트: outStack
# 스택: opStack

for each token in expr:
    if token == operand:
        outStack.append(token)
    if token == '(':
        opStack.push(token)
    if token == ')':
        # opStack에 저장된 연산자 '('를 pop 할 때까지 pop of outStack에 append
    if token in '+,*,-,/':
    #     opStack에 token 보다 우선순위 높은연산자 모두 pop, 자신이 push
    # =>opStack에 남은 연산자 모두 pop -> outStack