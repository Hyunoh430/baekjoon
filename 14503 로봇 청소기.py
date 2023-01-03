n, m = map(int, input().split())
x, y, direction = map(int ,input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]  #북동남서
dy = [0, 1, 0, -1]

result = 1
visited[x][y] = True        #현재 위치를 청소한다

def turnleft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
check = 0
while True:
    if check == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if data[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        check = 0
    turnleft()  #왼쪽방향부터 탐색
    nx = x + dx[direction]
    ny = y + dy[direction]
    if data[nx][ny] == 0 and visited[nx][ny] == False:  #청소하지않았고 빈칸이라면
        visited[nx][ny] = True  #청소처리
        result += 1 #청소한 곳 하나 추가
        x, y = nx, ny   #그 칸으로 이동
        check = 0
        continue
    if data[nx][ny] == 1 or visited[nx][ny] == True:
        check += 1



print(result)

