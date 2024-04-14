# 양과 늑대
from collections import deque

info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]     # 0: 양, 1: 늑대
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

tree = [[] for _ in range(len(info))]
for edge in edges:
    tree[edge[0]].append(edge[1])
print(tree)
# [[1, 8], [2, 4], [], [], [3, 6], [], [5], [], [7, 9], [10, 11], [], []]

# BFS 를 위한 큐 생성
# 현재 위치, 양의 수, 늑대 수, 방문한 노드 집합
q = deque([(0, 1, 0, set())])
max_sheep = 1

while q:
    current, sheep_count, wolf_count, visited = q.popleft()
    max_sheep = max(max_sheep, sheep_count)
    visited.update(tree[current])
    # print(visited)

    for next_node in visited:
        if info[next_node] == 1:    # 늑대
            if sheep_count != wolf_count + 1:
                q.append((next_node, sheep_count, wolf_count + 1, visited - {next_node}))
        else:
            q.append((next_node, sheep_count + 1, wolf_count, visited - {next_node}))
print(max_sheep)