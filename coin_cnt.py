n = 2320
cnt = 0

# 큰 단위의 동전부터 적용하기 위해 순서대로
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    cnt += n
    n %= coin

print(cnt)
# 9 출력