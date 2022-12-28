from collections import deque

m, n, h = map(int, input().split())
data = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        data[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
for i in range(h):      #높이
    for j in range(n):  #세로
        for k in range(m):      #가로
            if data[i][j][k] == 1:
                q.append([i, j, k])     #익은 토마토 큐에 대입

while q:
    z, x, y = q.popleft()

    for j in range(6):
        nz = z + dz[j]
        nx = x + dx[j]
        ny = y + dy[j]
        if 0<= nz < h and 0 <= nx < n and 0 <= ny < m:
            if data[nz][nx][ny] == 0:
                data[nz][nx][ny] = data[z][x][y] + 1
                q.append([nz, nx, ny])


check = 0
for i in data:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        check = max(check, max(j))
print(check - 1)


