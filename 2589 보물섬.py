from collections import deque

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(str, input())))    #L 육지 W 바다

maxnum = -1e9
#보물은 최단거리중 최댓값에 묻혀있다
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
distance = [[0] * m for _ in range(n)]
def bfs(x, y):
    q = deque()
    q.append([x, y])
    distance[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 'L' and distance[nx][ny] == 0:
                #만약 다음 땅이 육지이고 방문하지 않은 곳이라면!
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            distance = [[0] * m for _ in range(n)]
            bfs(i, j)
            maxdistance = max(map(max, distance))       #bfs돌린 후 distance에서 제일큰 값 저장
            maxnum = max(maxnum, maxdistance)   #maxdistance중 제일 큰 값 저장

print(maxnum - 1)

