from collections import deque

r, c = map(int, input().split())
graph = []
data = []
distance = [[0] * c for _ in range(r)]
check = False
for i in range(r):
    graph.append(list(map(str, input())))


for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S' or graph[i][j] == '*':
            data.append([graph[i][j], i, j])      #data에 돌인지 물인지와 그것의 좌표 대입
data.sort()     #물이 먼저 퍼지고 이동을해야되니깐 * 먼저오게 정렬
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    global check
    q = deque(data)
    while q:
        # for i in range(r):
        #     print(graph[i])

        type, x, y = q.popleft()
        # print(type, x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.':
                    if type == '*':
                        graph[nx][ny] = '*'
                        q.append(['*', nx, ny])
                    if type == 'S':
                        graph[nx][ny] = 'S'
                        q.append(['S', nx, ny])
                        distance[nx][ny] = distance[x][y] + 1
                if graph[nx][ny] == 'D':
                    if type == '*':
                        continue        #물이 비버의 굴에 침범 안하기때문에
                    if type == 'S':
                        print(distance[x][y] + 1)
                        check = True
                        return
bfs()
if check == False:
    print("KAKTUS")


