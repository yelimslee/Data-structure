import sys
input = sys.stdin.readline

def quick_sort(lt, rt):
    if lt < rt:
        p = lt
        pivot = arr[rt]

        # pivot 전까지 순회
        for i in range(lt, rt):

            # pivot 보다 작을 때만 바꿔주고 p증가 시켜줌
            if arr[i] <= pivot:
                arr[i], arr[p] = arr[p], arr[i]
                p += 1

        # 순회후 pivot이랑 p 자리 교체 
        