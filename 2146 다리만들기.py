from collections import deque
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
vis = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#땅 구분하기
def bfs(x, y):
    q = deque()
    q.append([x, y])
    data[x][y] = count
    vis[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] == 1 and  not vis[nx][ny]:
                    data[nx][ny] = count
                    vis[nx][ny] = True
                    q.append([nx, ny])

def bfs2(num):
    global min_distance
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if data[i][j] == num:
                q.append([i, j])
                visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] > 0 and data[nx][ny] != num and visited[nx][ny] == -1:
                    min_distance = min(visited[x][y], min_distance)
                    return
                if visited[nx][ny] == -1 and data[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])


    return min_distance
count = 2
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            bfs(i, j)
            count += 1
min_distance = 1e9
for i in range(2, count):
    bfs2(i)
print(min_distance)





