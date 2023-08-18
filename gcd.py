# 최대공약수(GCD 또는 HCF)를 구하는 가장 간단한 방법은 math모듈을 사용하는 것.
# 그리고 그 외.

# 1. 두 정수의 GCD  (math 모듈 사용)
import math

print(math.gcd(60, 48))  # 12
print(math.gcd(60, 0))  # 60
print(math.gcd(0, 0))  # 0
print(math.gcd(10, 'a'))  # TypeError


# 2. recursion(재귀) 사용
def computeGCD(a, b):
    if(b == 0):
        return a
    else:
        return computeGCD(b, a % b)  # 재귀 호출: b는 a로 대체되고, a%b는 b로 대체. b가 0이 될 때까지 계산.

a = 40
b = 48
print(f"{a}와 {b}의 GCD는 {computeGCD(a, b)}입니다.")
# 40와 48의 GCD는 8입니다.


# 3. loop 사용
def compute(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x%i==0) and (y%i==0)):
            gcd = i

    return gcd

a = 40
b = 48
print(f"{a}와 {b}의 GCD는 {computeGCD(a, b)}입니다.")
# 40와 48의 GCD는 8입니다.


# 4. 유클리디안 알고리즘
def computeGCD(x, y):
    while(y):  # y가 0이 아닌 동안 반복 = y가 0이 되면 반복을 멈춤
        x, y = y, x % y  # x와 y의 값을 교환하고 x를 x%y로 업데이트 = 이것은 나머지 연산을 통해 x와 y사이의 크기를 줄여나가는 과정
                         # 이 과정을 반복하여 y가 0이 되면 반복문이 종료, 이때의 x값이 최대공약수
    return x

a = 40
b = 48
print(f"{a}와 {b}의 GCD는 {computeGCD(a, b)}입니다.")


# 5. 두 부동 소수의 GCD
import math

def computeGCD(a, b):
    if (a < b):
        return computeGCD(b, a)  # 이렇게 하면 항상 a가 b보다 크거나 같은 상태가 유지.
    
    # base case
    if (abs(b) < 0.001):  # b의 절댓값이 매우 작을 때(거의 0에 가까울 때)의 기저 경우를 처리.
        return a
    else:
        return (computeGCD(b,a - math.floor(a / b) * b))  # math.floor(a / b) = 몫을 구하는 것.
    # a - math.floor(a / b) * b) = a를 b의 배수를 뺀 값으로, 이를 이용해 a와 b를 최대공약수를 유지하면서 줄여나가는 과정
    
a = 1.20
b = 22.5
print(f'{computeGCD(a, b):.1f}')  # 0.3


# 6. 세 개 이상의 수(리스트)의 GCD
def computeGCD(x, y):
    while(y):
        x, y = y, x % y

    return x

l = [2, 4, 6, 8, 16]

num1 =l[0]
num2 =l[1]
gcd = computeGCD(num1, num2)  # gcd 변수에 num1과 num2의 최대공약수를 계산한 값을 저장.

for i in range(2, len(l)):
    gcd = computeGCD(gcd, l[i])

print(gcd)  # 2