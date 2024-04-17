from collections import deque

def bfs(graph, start_node):
    visited = set()  # 방문한 노드를 저장할 집합
    queue = deque([start_node])  # 큐 생성 후 시작 노드를 큐에 추가

    while queue:  # 큐가 빌 때까지 반복
        node = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            # 모든 인접 노드를 큐에 삽입
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# 같은 그래프 사용
bfs(graph, 'A')
