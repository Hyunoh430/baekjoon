import sys
from collections import deque

sys.setrecursionlimit(100000)

N, Q = map(int, input().split())
graph = []
for i in range(2 ** N):
    graph.append(list(map(int, input().split())))
L = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate(size, r, c):
    temp = []
    for i in range(size):
        temp.append([])
        for j in range(size):
            temp[i].append(graph[r + i][c + j])

    for i in range(size):
        for j in range(size):
            graph[r + i][c + j] = temp[size - 1 - j][i]


def melt():
    to_melt = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            if graph[i][j] > 0:
                ice_count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and graph[nx][ny] > 0:
                        ice_count += 1
                if ice_count < 3:
                    to_melt.append([i, j])

    for i, j in to_melt:
        graph[i][j] -= 1


# BFS로 변경하여 스택 오버플로우 방지
def ice_group():
    visited = [[False] * (2 ** N) for _ in range(2 ** N)]

    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        size = 0

        while queue:
            x, y = queue.popleft()
            size += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < 2 ** N and 0 <= ny < 2 ** N and
                        not visited[nx][ny] and graph[nx][ny] > 0):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        return size

    max_size = 0
    for x in range(2 ** N):
        for y in range(2 ** N):
            if not visited[x][y] and graph[x][y] > 0:
                size = bfs(x, y)
                max_size = max(max_size, size)

    return max_size


# 메인 로직
for step in L:
    # 회전
    for i in range(0, 2 ** N, 2 ** step):
        for j in range(0, 2 ** N, 2 ** step):
            rotate(2 ** step, i, j)

    # 녹이기
    melt()

# 최종 결과만 계산
total_ice = sum(sum(row) for row in graph)
max_ice_group = ice_group()

print(total_ice)
print(max_ice_group)