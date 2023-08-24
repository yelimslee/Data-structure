# 알고리즘의 수행시간 = 최악의 경우의 입력에 대한 기본 연산 횟수
# Big-O 표기법: 함수 값을 결정하는 최고차항 만으로 간단하게 표기
# 1. 최고차항만 남긴다 2. 최고차항 계수(상수)는 생략 3. Big-O(최고차항)

# 예시 1
algorithm arrayMax(A, n):
    currentMax = A[0]  # 1번
    for i = 1 to n-1 do  # n-1번
        if currentMax < A[i]:  # 1번
            currentMax = A[i]  # 1번
    return currentMax

# 총 T(n) = 2n - 1 
# T1(n) = O(n)


# 예시 2
algorithm sum2(A, n):
    sum = 0  # 1번
    for i = 0 to n-1 do  # n번
        if A[i] % 2 == 0:  # 2번
            sum += A[i]  # 2번
    return sum

# 총 T(n) = 4n + 1
# T2(n) = O(n)


# 예시 3  
algorithm sum3(A, n):
    sum = 0  # 1번
    for i = 0 to n-1 do  # n번
        for j = i to n-1 do  # n(n+1)/2*3번
            sum += A[i] * A[j]  # 3번
    return sum 

# 총 T(n) = 3/2n(n+1)+1 = 3/2n**2 + 3/2n + 1
# T3(n) = O(n**2)