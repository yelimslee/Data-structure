def insert(self, value):
    # 루트
    if self.head is None:
        self.head = Node(value)
    else:
        # 루트부터 검사
        node = self.head

        while True:
            # 값이 더 작은 경우 왼쪽 서브 트리로
            if value < node.getvalue():
                # 노드의 왼쪽 자식 노드가 없으면
                if node.getleft() is None:
                    # 왼쪽 자식 노드로 저장
                    node.setleft(Node(value))
                    break
                # 노드의 왼쪽 자식 노드가 있으면
                else:
                    # 현재 노드를 왼쪽 자식 노드로
                    node = node.left
            # 값이 더 큰 경우 오른쪽 서브 트리로
            else:
                if node.getright() is None:
                    node.setright(Node(value))
                    break
                else:
                    node = node.right