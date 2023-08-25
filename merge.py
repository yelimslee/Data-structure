import sys
input = sys.stdin.readline  # 반복문 안에서 여러 줄을 입력받아야 할 때 효율적

def merge_sort(lt, rt):  # lt(left):맨 왼쪽 인덱스, rt(right):맨 오른쪽 인덱스
    if lt < rt:
        mid = (lt + rt) // 2

        # Divide
        merge_sort(lt, mid)  # 왼쪽 부분 정렬
        merge_sort(mid+1, rt)  # 오른쪽 부분 정렬

        #Conquer, Combine
        temp = list()
        # 나눴던 두 리스트의 시작 인덱스
        ls = lt  # 왼쪽 부분 리스트의 시작
        rs = mid + 1  # 오른쪽 부분 리스트의 시작

        # 비교하며 임시 리스트에 삽입
        while ls <= mid and rs <= rt:
            if arr[ls] < arr[rs]:
                temp.append(arr[ls])
                ls += 1
            else:
                temp.append(arr[rs])
                rs += 1

        # 둘 중 한 리스트가 임시 리스트에 다 삽입된 경우
        # 남은 리스트를 임시 리스트에 삽입
        if ls <= mid:
            temp = temp + arr[ls:mid + 1]
        else:
            temp = temp + arr[rs:rt + 1]

        for i in range(lt, rt + 1):
            arr[i] = temp[i - lt]

if __name__ == "__main__":
    arr = [4, 3, 7, 1, 2, 8, 5, 6]
    print("정렬전 리스트: ", end= '')
    print(arr)
    merge_sort(0, 7)
    print()
    print("병합정렬 후 리스트: ", end= '')
    print(arr)