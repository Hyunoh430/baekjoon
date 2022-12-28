import sys
sys.setrecursionlimit(10 ** 4)

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def meltcount(x, y):        #빙하 주위에 0이 몇개있는지 세기
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0:
                count += 1
    return [x, y, count]        #빙하 주위로 바다가 몇칸 있는지 리턴

def dfs(x, y):      #빙산이 몇개로 분리되는지 세기 위한 dfs
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
            if data[i][j] != 0 and visited[i][j] == False:      #만약 바다가 아니라 빙산이고 아직 방문한적 없는 곳이면 dfs
                dfs(i, j)
                count += 1          #dfs가 몇번 돌아갔는지 세보면 그것이 빙산의 개수
                if count == 2:
                    break
    if count >= 2:      #만약 2개이상으로 분리되면
        print(year)
        break
    if count == 0:  #만약 모두 녹아서 없어졌으면
        print(0)
        break
    #한번 실행해서 빙산가 두개가 아님을 확인했으면 이제 빙산을 녹이자
    a = []
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                a.append(meltcount(i, j))       #어떤 빙산을 녹일지에 대한 x,y좌표와 몇개 녹일지
    for x, y, count in a:
        data[x][y] -= count
        if data[x][y] < 0:
            data[x][y] = 0
    year += 1
    visited = [[False] * m for _ in range(n)]
    # if sum(map(sum, data)) == 0:
    #     print(0)
    #     break

