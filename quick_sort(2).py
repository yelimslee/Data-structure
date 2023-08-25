import sys
input = sys.stdin.readline

def quick_sort(lt, rt):
    if lt < rt:
        p = lt
        pivot = arr[rt]

        # pivot 전까지 순회
        for i in range(lt, rt):
            # pivot보다 작을 때만 바꿔주고 p증가 시켜줌
            if arr[i] <= pivot:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1

        # 순회 후 pivot이랑 p 자리 교체
        arr[rt], arr[p] = arr[p], arr[rt]

        # divide
        quick_sort(lt, p-1)
        quick_sort(p+1, rt)

if __name__ == "__main__":
    arr = [4, 3, 7, 1, 2, 8, 5, 6]
    print("정렬전 리스트: ", end='')
    print(arr)
    quick_sort(0, 7)
    print()
    print("퀵소트후 리스트: ", end='')
    print(arr)