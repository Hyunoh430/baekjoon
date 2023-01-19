from copy import deepcopy
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]
result = 0
dp = [[-1] * m for _ in range(n)]
def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] == -1:  #탐색하지 않은 곳이라면 ㄱㄱ
        dp[x][y] = 0    #탐색 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if data[nx][ny] < data[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0, 0))

