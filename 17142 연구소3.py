from collections import deque
from itertools import combinations

N, M = map(int, input().split())

data = []
virus = []
for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(len(data[i])):
        if data[i][j] == 2:
            virus.append([i,j])


dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

virus_list = list(combinations(virus, M))
#print(virus)
def bfs(vir):
    q = deque()
    result = [[0] * N for _ in range(N)]

    for v in vir:
        q.append(v)
        result[v[0]][v[1]] = 0
    check = 0
    while q:
        check += 1
        x, y = q.popleft()
        if check <= M:
            result[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                #만약 벽이 아니고 | 아직 전염을 안했고 | 바이러스가 아니라면?
                if data[nx][ny] != 1 and result[nx][ny] == 0: #and data[nx][ny] != 2:
                    result[nx][ny] = result[x][y] + 1
                    q.append([nx, ny])

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2 and result[i][j] != 0: #만약 비활성바이러스라면?
                result[i][j] = -1        # 카운트 안해줘야되니깐 이것들은 걍 0 으로 바꾸자
            if data[i][j] == 0 and result[i][j] == 0:   #미완성인거 발견했다면?
                #result = [[-1] * N for _ in range(N)]
                return -1
    return result

min_num = []

for vir in virus_list:  #바이러스 후보 쭉 돌린 후 최소시간 구해보자
    result = bfs(vir)
    if result == -1:
        continue
    #print(vir)
    max_num = 0
    for i in range(N):
        #print(result[i])
        check = max(result[i])
        if max_num < check:
            max_num = check
    #print(max_num)
    #print(1111)

    min_num.append(max_num)
if not min_num:
    print(-1)
else:
    print(min(min_num))
