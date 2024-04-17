def dfs(graph, node, visited):
    visited.add(node)  # 방문한 노드 추가
    print(node, end=' ')

    # 현재 노드와 연결된 모든 노드에 대해
    for neighbor in graph[node]:
        if neighbor not in visited:  # 아직 방문하지 않은 노드면
            dfs(graph, neighbor, visited)  # 재귀적으로 방문

from collections import deque
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# 그래프는 딕셔너리로 표현
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()  # 방문한 노드를 저장할 집합
dfs(graph, 'A', visited)                # A, B, D, E, C, F
print("")
bfs(graph, 'A')                         # A, B, C, D, E, F

