from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = 2    #상어 크기
def bfs(x, y):  #최단거리 구하는 함수
    distance = [[-1] * n for _ in range(n)]
    checklist = []
    q = deque()
    q.append([x, y])
    distance[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or size < graph[nx][ny]:  #그래프 밖이거나 물고기가 더 크다면
                continue
            if distance[nx][ny] == -1:       #아직 안가본 곳이라면??
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny])

                if 1 <= graph[nx][ny] <= 6 and size > graph[nx][ny]:    #만약 먹을 수 있는 물고기라면?
                    checklist.append([distance[nx][ny], nx, ny])    #거리와 x, y좌표 체크리스트에 추가
    checklist.sort(key = lambda x : (x[0], x[1], x[2])) #거리가 짧고 가장 왼쪽 위에 있는 순으로 정렬

    return checklist    #먹을 수 있는 물고기 리스트 반환

time = 0
eat = 0
while True:
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                checklist = bfs(i, j)
                graph[i][j] = 0
    if not checklist:
        break   #더 이상 먹을 물고기가 없다면 종료
    dis, x, y = checklist[0][0], checklist[0][1], checklist[0][2]
    time += dis
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    graph[x][y] = 9
print(time)











