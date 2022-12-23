import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def meltcount(x, y):        #만약 0이 아니라면 이 함수 실행
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0:
                count += 1
    return [x, y, count]        #빙하 주위로 바다가 몇칸 있는지 리턴

def dfs(x, y):      #몇개의 빙하인 세기
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] != 0 and visited[nx][ny] == False:
                dfs(nx, ny)

year = 0
while True:
    count = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and visited[i][j] == False:
                dfs(i, j)
                count += 1

    if count >= 2:
        print(year)
        break
    #한번 실행해서 빙산가 두개가 아님을 확인했으면 이제 빙산을 녹이자
    a = []
    for i in range(n):
        for j in range(m):
            a.append(meltcount(i, j))
    for x, y, count in a:
        data[x][y] -= count
        if data[x][y] < 0:
            data[x][y] = 0
    year += 1
    visited = [[False] * m for _ in range(n)]
    if sum(map(sum, data)) == 0:
        print(0)
        break

