# 게임 맵 최단 거리

# maps 는 n x m 크기의 게임맵의 상태가 들어있는 2차원 배열
# 0 은 벽이 있는 자리
# 1 은 벽이 없는 자리
# 처음 캐릭터는 1,1 위치에 있고 상대팀은 n, m 위치에 있음

from collections import deque

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

# 이 문제는 결국 최솟값이 필요하다. 너비 우선 탐색. bfs

# moves 좌 하 상 우
moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]

n = len(maps)
m = len(maps[0])

# 거리를 저장하는 배열 -1로 초기화
dist = [[-1] * m for _ in range(n)]

def bfs(start):
    q = deque([start])
    dist[start[0]][start[1]] = 1

    while q:
        here = q.popleft()

        for direct in moves:
            row, column = here[0] + direct[0], here[1] + direct[1]

            # 위치를 벗어난 것이면 다음 방향으로
            if row < 0 or row >= n or column < 0 or column >= m:
                continue

            # 벽이면 다음 방향
            if maps[row][column] == 0:
                continue

            if dist[row][column] == -1: # 처음 방문
                q.append([row, column])
                dist[row][column] = dist[here[0]][here[1]] + 1

    return dist

bfs([0, 0])

print(dist)
print(dist[n - 1][m - 1])