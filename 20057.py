N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_num = 0

visited = [[False] * M for _ in range(N)]

def dfs(x, y, count, res):
    global max_num
    if count == 4:
        max_num = max(max_num, res)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, res + graph[nx][ny])
            visited[nx][ny] = False


def fu():
    global max_num
    # ㅗ 모양 (4가지 회전)
    for i in range(N):
        for j in range(M):
            # ㅗ (위로 튀어나온 형태)
            if i >= 1 and j >= 1 and j < M - 1:
                temp = graph[i][j] + graph[i][j - 1] + graph[i][j + 1] + graph[i - 1][j]
                max_num = max(max_num, temp)

            # ㅜ (아래로 튀어나온 형태)
            if i < N - 1 and j >= 1 and j < M - 1:
                temp = graph[i][j] + graph[i][j - 1] + graph[i][j + 1] + graph[i + 1][j]
                max_num = max(max_num, temp)

            # ㅏ (오른쪽으로 튀어나온 형태)
            if i >= 1 and i < N - 1 and j < M - 1:
                temp = graph[i][j] + graph[i - 1][j] + graph[i + 1][j] + graph[i][j + 1]
                max_num = max(max_num, temp)

            # ㅓ (왼쪽으로 튀어나온 형태)
            if i >= 1 and i < N - 1 and j >= 1:
                temp = graph[i][j] + graph[i - 1][j] + graph[i + 1][j] + graph[i][j - 1]
                max_num = max(max_num, temp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False

       # visited[i][j] = False
fu()
print(max_num) # 정답 출력