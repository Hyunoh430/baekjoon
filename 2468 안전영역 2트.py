from collections import deque

N = int(input())
data = []
max_height = 0

for i in range(N):
    data.append(list(map(int, input().split())))
    for height in data[i]:
        if height > max_height:
            max_height = height

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, height, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if (visited[nx][ny] == 0 and data[nx][ny] > height):
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


result = []

for height in range(max_height):     #높이가 height이하인 지점은 다 잠겨야함
    #잠기지 않은 영역을 구하는거임, height보다 커야함 ㅇㅇ
    count = 0
    visited = [[0] * N for _ in range(N)]   #visited는 매번 초기화
    for x in range(N):
        for y in range(N):
            if(visited[x][y] == 0 and data[x][y] > height):
                bfs(x, y, height, visited)
                count += 1
    result.append(count)

print(max(result))


