# 해시 테이블 생성: 100개의 원소를 0으로 초기화한 리스트를 생성합니다.
hash_table = [0 for _ in range(100)]

# 해시 함수 정의: 주어진 키를 해시 값으로 변환하기 위한 함수입니다.
def hash_function(key):
    return hash(key) % 100

# 데이터 삽입 함수 정의: 주어진 키와 값을 해시 테이블에 삽입하는 함수입니다.
def set_data(key, value):
    hash_value = hash_function(key)  # 주어진 키의 해시 값을 계산합니다.
    hash_table[hash_value] = value   # 계산된 해시 값을 인덱스로 사용하여 데이터를 삽입합니다.

# 데이터 조회 함수 정의: 주어진 키에 해당하는 값을 해시 테이블에서 찾아 반환하는 함수입니다.
def get_data(key):
    hash_value = hash_function(key)  # 주어진 키의 해시 값을 계산합니다.
    return hash_table[hash_value]    # 계산된 해시 값을 인덱스로 사용하여 해당하는 데이터를 반환합니다.

# 데이터 삽입
set_data('Radv', 2022)  # 'Radv'라는 키에 2022라는 값을 매핑하여 삽입합니다.
set_data('hello', 77)   # 'hello'라는 키에 77이라는 값을 매핑하여 삽입합니다.

# 데이터 조회 및 출력
print(get_data('Radv'))  # 'Radv' 키에 대응하는 값을 조회하여 출력합니다.
print(get_data('hello'))  # 'hello' 키에 대응하는 값을 조회하여 출력합니다.