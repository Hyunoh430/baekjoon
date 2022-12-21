n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    data[x][y] = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 1:
                dfs(nx, ny)


count = 1       #집이 1로 표기되니깐 숫자 2부터 스타트해서 세보자
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            count += 1
            dfs(i, j)
result = []
print(count - 1)

for k in range(2, count + 1):
    check = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == k:
                check += 1
    result.append(check)

result.sort()
for c in result:
    print(c)

