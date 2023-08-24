# DFS함수
def DFS(graph, v, visited):
    # 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 연결된 노드 중
    for i in graph[v]:
        # 방문 안 한 노드에 대해
        if not visited[i]:
            # 재귀 호출
            DFS(graph, i, visited)

if __name__ == "__main__":
    graph = [
        [],
        # 1번 노드에 연결된 노드들 오름차순으로 연결 표시
        [2, 4, 5],
        [1, 6],
        [4],
        [1, 3, 7],
        [1, 8],
        [2],
        [4],
        [5]
    ]
    
    # 방문 리스트
    visited = [False] * 9
    # 맨 처음 1번 노드부터
    DFS(graph, 1, visited)