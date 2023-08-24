from collections import deque

# BFS 함수
def BFS(graph, start, visited):
    # 큐 자료구조 deque로
    queue = deque([start])

    # 빈 큐가 될 때까지
    while queue:
        v = queue.popleft()
        
        # 해당 노드 방문처리
        visited[v] = True
        print(v, end= ' ')
        
        # 해당 노드와 연결되어 있고, 방문하지 않은 노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)

if __name__ == "__main__":
    graph = [
        [],
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
    BFS(graph, 1, visited)