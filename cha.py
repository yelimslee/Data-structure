# 에라토스테네스의 체 구현
# 자연수 n입력
n = int(input())

# 2~n 범위의 리스트 할당
a = [0] * (n+1)

for num in range(2, n+1):
    if a[num] == 0:
        # 소수이면 출력
        print(num, end=' ')
        # 배수 소수 처리
        for j in range(num, n+1, num):
            a[j] = 1