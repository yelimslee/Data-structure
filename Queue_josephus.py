# 문제
# 요세푸스 문제는 다음과 같다.
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

class Solution:
    def josephus(self, N: int, K: int):
        persons = [x for x in range(1, N+1)]  # 1부터 N까지의 사람들을 리스트에 추가

        idx = 0  # 인덱스 변수 초기화
        answer = []  # 결과를 저장할 리스트

        for _ in range(N):  # N번 반복하며 사람을 제거하고 결과 리스트에 추가
            idx += (K-1)  # K번째 사람의 인덱스 계산

            if idx >= len(persons):  # 인덱스가 리스트 범위를 벗어날 경우 원형 구조를 위해 모듈로 연산 사용
                idx = idx % len(persons)

            answer.append(str(persons.pop(idx)))  # 인덱스가 리스트 범위를 벗어날 경우 원형 구조를 위해 모듈로 연산 사용

        print("<", ", ".join(answer), ">", sep="")  # 결과 리스트 출력

N, K = map(int, input().split())  # N과 K를 입력받음
Solution().josephus(N, K)  # Solution 클래스의 josephus 메서드 호출하여 문제 해결과 결과 출력