from collections import deque

N, T = map(int, input().split())
F = [[0] * N for _ in range(N)]
for i in range(N):      #우유 = 1, 초코 = 2, 민트 = 4, 초코우유 = 3, 민트초코 = 6, 민트초코우유 = 7
    foods = input()
    for j in range(N):
        if foods[j] == 'T':
            F[i][j] = 4
        elif foods[j] == 'C':
            F[i][j] = 2
        else:
            F[i][j] = 1

B = []  #신앙심
for i in range(N):
    B.append(list(map(int, input().split())))

def morning():
    for i in range(N):
        for j in range(N):
            B[i][j] += 1


dx = [-1, 1, 0, 0]  #위,아래,왼쪽,오른쪽
dy = [0, 0, -1, 1]
def choose_president(x, y, visited):
    q = deque()
    q.append([x,y])
    current = F[x][y]
    president = [x,y]
    count = 0
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if F[nx][ny] == current and not visited[nx][ny]:
                    if B[nx][ny] > B[president[0]][president[1]]:
                        president = [nx, ny]
                    elif B[nx][ny] == B[president[0]][president[1]]:
                        if nx < president[0] :
                            president = [nx, ny]
                        elif nx == president[0]:
                            if ny < president[1]:
                                president = [nx, ny]
                    q.append([nx, ny])
                    visited[nx][ny] = True

    return president, count

def lunch():
    #대표자를 찾자
    visited = [[False] * N for _ in range(N)]
    presidents = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                president, count = choose_president(i,j, visited)
                presidents.append([president[0], president[1],count])
                #print(president, count)
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][j] -= 1
    for x, y, c in presidents:
        B[x][y] += c



morning()
lunch()




