N, Q = map(int, input().split())

graph = [[0] * N for _ in range(N)]
micro_id = -1

def micro_input():
    global micro_id
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            if graph[i][j] == 0:
                graph[i][j] = micro_id

def micro_shape_size(micro_id):
    cells = []
    size = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == micro_id:
                cells.append([i, j])
                size += 1

    min_x = min(cell[0] for cell in cells)
    min_y = min(cell[1] for cell in cells)

    relative_shape = []
    for x, y in cells:
        relative_shape.append([x - min_x, y - min_y])

    return relative_shape, size


def micro_move():


    return

for _ in range(Q):
    micro_id += 1
    micro_input()
    micro_move()


