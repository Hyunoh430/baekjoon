N, Q = map(int, input().split())

graph = [[0] * N for _ in range(N)]
micro_id = 0  # 1부터 시작하도록


def micro_input():
    global micro_id
    micro_id += 1
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            graph[i][j] = micro_id

    # 올바른 범위로 수정
    for i in range(1, micro_id):
        if count_components(i) >= 2:
            remove(i)


def remove(target_micro_id):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == target_micro_id:
                graph[i][j] = 0


def count_components(target_micro_id):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == target_micro_id and not visited[i][j]:
                dfs(i, j, visited, target_micro_id)
                count += 1
    return count


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, visited, target_micro_id):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny] == target_micro_id:
                dfs(nx, ny, visited, target_micro_id)


def micro_shape_size(target_micro_id):
    cells = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == target_micro_id:
                cells.append([i, j])

    if not cells:
        return [], 0

    min_x = min(cell[0] for cell in cells)
    min_y = min(cell[1] for cell in cells)

    relative_shape = []
    for x, y in cells:
        relative_shape.append([x - min_x, y - min_y])

    return relative_shape, len(cells)


def micro_move(current_micro_count):
    micro_info = []
    # 올바른 범위로 수정
    for mid in range(1, current_micro_count + 2):
        shape, size = micro_shape_size(mid)
        if size > 0:
            micro_info.append([size, mid, shape])

    micro_info.sort(key=lambda x: (-x[0], x[1]))

    new_graph = [[0] * N for _ in range(N)]

    for size, mid, shape in micro_info:
        placed = False
        for x in range(N):
            if placed:
                break
            for y in range(N):
                can_place = True
                for dx, dy in shape:
                    nx, ny = x + dx, y + dy
                    # 경계 조건 수정
                    if nx >= N or ny >= N or nx < 0 or ny < 0 or new_graph[nx][ny] != 0:
                        can_place = False
                        break

                if can_place:
                    for dx, dy in shape:
                        new_graph[x + dx][y + dy] = mid
                    placed = True
                    break

    global graph
    graph = new_graph


def calculate_result(current_micro_id):
    micro_sizes = [0] * (current_micro_id + 1)
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                micro_sizes[graph[i][j]] += 1

    adjacent_pairs = set()
    result_num = 0

    for x in range(N):
        for y in range(N):
            if graph[x][y] != 0:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[x][y] != graph[nx][ny] and graph[nx][ny] != 0:
                            a = min(graph[x][y], graph[nx][ny])
                            b = max(graph[x][y], graph[nx][ny])
                            adjacent_pairs.add((a, b))

    for a, b in adjacent_pairs:
        result_num += micro_sizes[a] * micro_sizes[b]

    print(result_num)


for i in range(Q):
    micro_input()
    micro_move(i)  # current_micro_count는 i (0부터 시작)
    calculate_result(micro_id)
