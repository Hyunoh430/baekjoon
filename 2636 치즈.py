from collections import deque
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
cheese = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append([0, 0])    #0, 0부터 bfs 돌리자
    visited[0][0] = True
    check = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if data[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                if data[nx][ny] == 1:
                    visited[nx][ny] = True
                    data[nx][ny] = 0
                    check += 1
    cheese.append(check)
    return check
time = 0
while True:
    time += 1
    check = bfs()
    if check == 0:
        break
print(time - 1)
print(cheese[-2])

