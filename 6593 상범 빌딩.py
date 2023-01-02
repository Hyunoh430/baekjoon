from collections import deque
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(z, x, y):
    global check
    q = deque()
    q.append([z, x, y])

    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if data[nz][nx][ny] == '.' and distance[nz][nx][ny] == -1:
                    distance[nz][nx][ny] = distance[z][x][y] + 1
                    q.append([nz, nx, ny])
                if data[nz][nx][ny] == 'E':
                    distance[nz][nx][ny] = distance[z][x][y] + 1
                    print("Escaped in %d minute(s)."%distance[nz][nx][ny])
                    check = True
                    return


while True:
    l, r, c = map(int, input().split())
    data = [[] * r for _ in range(l)]
    distance = [[[-1] * c for _ in range(r)] for _ in range(l)]
    check = False
    if l == 0 and r == 0 and c == 0:
        break
    for i in range(l):
        for j in range(r):
            data[i].append(list(map(str, input())))
        input()

    for z in range(l):
        for x in range(r):
            for y in range(c):
                if data[z][x][y] == 'S':
                    distance[z][x][y] = 0
                    bfs(z, x, y)

    if check == False:
        print("Trapped!")




