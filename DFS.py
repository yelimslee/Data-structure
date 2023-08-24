def DFS(n):
    if n < 1:
        return
    print(n, end=' ')
    DFS(n-1)

DFS(5)