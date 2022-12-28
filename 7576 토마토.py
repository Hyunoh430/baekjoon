from collections import deque

m, n = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            q.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                q.append([nx, ny])

check = False
for i in range(n):
    if 0 in data[i]:
        check = True

if check == True:
    print(-1)
else:
    print(max(map(max, data)) - 1)
