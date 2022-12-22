r, c = map(int, input().split())
data = []
for i in range(r):
    data.append(list(map(str, input())))

visit = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
length = 0
def dfs(x, y):
    global length
    visit.append(data[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if data[nx][ny] not in visit:
                dfs(nx, ny)
                length = max(length, len(visit))
                visit.pop()


dfs(0, 0)
print(length)