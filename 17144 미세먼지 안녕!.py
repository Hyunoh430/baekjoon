r, c, t = map(int, input().split())
data = []
for i in range(r):
    data.append(list(map(int, input().split())))
    if data[i][0] == -1:
        location = i        #공기청정기의 아래쪽 위치 저장


dx = [-1, 1, 0, 0]      #상하좌우 방향정보
dy = [0, 0, -1, 1]
def spread():       #확산 구현
    storage = [[0] * c for _ in range(r)]   #확산될때의 계산 정보 저장할 리스트
    for x in range(r):      #확산을 얼마씩 해야될질 먼저 구하자
        for y in range(c):
            if data[x][y] > 0:  #만약 미세먼지가 있는 곳이라면?
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    #상하좌우 중 칸이 있거나 공기청정기가 아니라면?
                    if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != -1:
                        dust = data[x][y] // 5   #이동할 먼지 수
                        storage[nx][ny] += dust
                        storage[x][y] -= dust
    for i in range(r):
        for j in range(c):
            data[i][j] += storage[i][j]

def cleanup():        #공기청정기 위쪽 구현
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y, i = location - 1, 1, 0
    prev = 0    #공기청정기에서 나오는건 0 이므로
    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        if x == location - 1 and y == 0:
            break
        if nx >= r or nx < 0 or ny >= c or ny < 0:
            i += 1
            continue
        data[x][y], prev = prev, data[x][y]
        x, y = nx, ny

def cleandown():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, i = location, 1, 0
    prev = 0
    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        if x == location and y == 0:
            break
        if nx >= r or nx < 0 or ny >= c or ny < 0:
            i += 1
            continue
        data[x][y], prev = prev, data[x][y]
        x, y = nx, ny

for i in range(t):
    spread()
    cleanup()
    cleandown()

result = 0
for i in range(r):
    result += sum(data[i])
result += 2
print(result)
