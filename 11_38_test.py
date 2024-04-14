# 깊이 우선 탐색 순회

from collections import defaultdict

# graph = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
# start = 'A'
graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
start = 'A'

adj_list = defaultdict(list)
# print(adj_list)
for u, v in graph:
    # print(u, v)
    adj_list[u].append(v)
print(adj_list)
# defaultdict(<class 'list'>, {'A': ['B'], 'B': ['C'], 'C': ['D'], 'D': ['E']})

# dfs
def dfs(node, visited, result):
    visited.add(node)
    result.append(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, result)

visited = set()
result = []
dfs(start, visited, result)

print(result)

