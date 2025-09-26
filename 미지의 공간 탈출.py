from collections import deque

N, M, F = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

EAST, WEST, SOUTH, NORTH, TOP = 0, 1, 2, 3, 4
views = []
for i in range(5):
    a = []
    for j in range(M):
        a.append(list(map(int, input().split())))  # a = [[1, 2, 3],[4,5,6]]
    views.append(a)

dx = [0, 0, 1, -1]  #동서남북
dy = [1, -1, 0, 0]
#일단 최단거리부터 구현해보자, 출발점 '2'은 항상 벽의 윗면!

for i in range(M):
    for j in range(M):
        if views[TOP][i][j] == 2:   #시작점!
            start_x, start_y = i, j
            break
visited = []
for i in range(5):
    visited.append([[False] * M for _ in range(M)])

# 시작점이 있는 큐브의 2D 위치를 찾기
def find_cube_position(start_x, start_y):
    """TOP면 시작점 (start_x, start_y)가 있는 큐브의 2D 좌표 찾기"""
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 3:  # 큐브가 있는 위치
                # 이 큐브의 TOP면이 우리가 찾는 시작점을 포함하는지 확인
                # (문제에서 주어진 조건에 따라 판단)
                return r, c
    return 0, 0  # 기본값

def convert_3d_to_2d(face, x, y, wall_r, wall_c):
    """3D 면의 가장자리 좌표를 2D 좌표로 변환"""
    if face == NORTH:
        # 북쪽 면 아래쪽 → 2D 북쪽 출구
        return wall_r - 1, wall_c + (M - y - 1)
    elif face == SOUTH:
        # 남쪽 면 아래쪽 → 2D 남쪽 출구
        return wall_r + M, wall_c + y
    elif face == WEST:
        # 서쪽 면 아래쪽 → 2D 서쪽 출구
        return wall_r + x, wall_c - 1
    elif face == EAST:
        # 동쪽 면 아래쪽 → 2D 동쪽 출구
        return wall_r + (M - x - 1), wall_c + M
    return -1, -1

def bfs_3d(x, y):
    next_face, next_x, next_y = -1, -1, -1
    cube_r, cube_c = find_cube_position(start_x, start_y)
    q = deque()
    time = 0
    q.append([time, TOP, x, y])
    visited[TOP][x][y] = True
    edge_info = {}
    while q:
        time, face, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < M:
                if views[face][nx][ny] == 0:
                    q.append([time + 1, face, nx, ny])
                    visited[face][nx][ny] = True
            else:
                print(f"  경계 벗어남: nx={nx}, ny={ny}")
                if nx < 0:
                    if face == TOP:
                        next_face = NORTH
                        next_x = 0
                        next_y = M - ny - 1
                    elif face == NORTH:
                        next_face = TOP
                        next_x = 0
                        next_y = M - ny - 1
                    elif face == EAST:
                        next_face = TOP
                        next_x = M - ny - 1
                        next_y = M - 1
                    elif face == SOUTH:
                        next_face = TOP
                        next_x = M - 1
                        next_y = ny
                    elif face == WEST:
                        next_face = TOP
                        next_x = ny
                        next_y = 0

                elif nx >= M:  # x가 M 이상 = 아래쪽으로 나감
                    if face == TOP:
                        next_face = SOUTH
                        next_x = 0
                        next_y = ny
                    elif face in [NORTH, SOUTH, EAST, WEST]:
                        exit_2d_r, exit_2d_c = convert_3d_to_2d(face, x, y, cube_r, cube_c)

                        if 0 <= exit_2d_r < N and 0 <= exit_2d_c < N and graph[exit_2d_r][exit_2d_c] == 0:
                            edge_info[(exit_2d_r, exit_2d_c)] = time + 1

                elif ny < 0:  # y가 음수 = 왼쪽으로 나감
                    if face == TOP:
                        next_face = WEST
                        next_x = 0
                        next_y = nx
                    elif face == NORTH:
                        next_face = EAST
                        next_x = nx
                        next_y = M - 1
                    elif face == EAST:
                        next_face = SOUTH
                        next_x = nx
                        next_y = M - 1
                    elif face == SOUTH:
                        next_face = WEST
                        next_x = nx
                        next_y = M - 1
                    elif face == WEST:
                        next_face = NORTH
                        next_x = nx
                        next_y = M - 1

                elif ny >= M:  # y가 M 이상 = 오른쪽으로 나감
                    if face == TOP:
                        next_face = EAST
                        next_x = 0
                        next_y = M - nx - 1
                    elif face == NORTH:
                        next_face = WEST
                        next_x = nx
                        next_y = 0
                    elif face == EAST:
                        next_face = NORTH
                        next_x = nx
                        next_y = 0
                    elif face == SOUTH:
                        next_face = EAST
                        next_x = nx
                        next_y = 0
                    elif face == WEST:
                        next_face = SOUTH
                        next_x = nx
                        next_y = 0
                if next_face == -1:
                    print(f"정의되지 않은 전환: face={face}, nx={nx}, ny={ny}")
                    continue
                if views[next_face][next_x][next_y] == 0 and not visited[next_face][next_x][next_y]:
                    visited[next_face][next_x][next_y] = True
                    q.append([time + 1, next_face, next_x, next_y])
    return edge_info


def bfs_2d(edge_info):
    # 목표점 찾기
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 4:
                final_r, final_c = r, c
                break

    q = deque()
    visited_2d = [[-1] * N for _ in range(N)]  # -1로 초기화

    # 여러 진입점에서 시작
    for (start_r, start_c), start_time in edge_info.items():
        if 0 <= start_r < N and 0 <= start_c < N:
            q.append([start_time, start_r, start_c])
            visited_2d[start_r][start_c] = start_time

    while q:
        time, r, c = q.popleft()
        if r == final_r and c == final_c:
            return time

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            next_time = time + 1

            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] != 1:  # 벽이 아니면
                if visited_2d[nr][nc] == -1:  # 방문하지 않았으면
                    visited_2d[nr][nc] = next_time
                    q.append([next_time, nr, nc])

    return -1  # 도달 불가능


# 메인 실행
edge_info = bfs_3d(start_x, start_y)
result = bfs_2d(edge_info)
print(result)