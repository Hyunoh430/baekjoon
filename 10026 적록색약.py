import sys
sys.setrecursionlimit(10 ** 6)      #런타임에러(recursionError)이뜬다면 이렇게 재귀를 늘리자!

n = int(input())
data = []
for i in range(n):
    data.append(list(map(str, input())))
data2 = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        data2[i].append(data[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, data):
    data[x][y] = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if data[nx][ny] == color:
            dfs(nx, ny, data)

count = 0
check1 = 0
check2 = 0
for i in range(n):
    for j in range(n):
        if type(data[i][j]) == str:
            color = data[i][j]
            count += 1
            dfs(i, j, data)
check1 = max(map(max, data))

for i in range(n):
    for j in range(n):
        if data2[i][j] == 'R':
            data2[i][j] = 'G'
count = 0
for i in range(n):
    for j in range(n):
        if type(data2[i][j]) == str:
            color = data2[i][j]
            count += 1
            dfs(i, j, data2)
check2 = max(map(max, data2))

print(check1, check2)