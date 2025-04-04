N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

moves = []
for i in range(M):
    moves.append(list(map(int, input().split())))

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

def movement(d, s): #일단 구름 이동 시키는거 구현하자
    for _ in range(s):      #s번 이동 시킴
        #print(clouds)
        for cloud in clouds:
            cloud[0] = (cloud[0] + dx[d]) % N
            cloud[1] = (cloud[1] + dy[d]) % N

def magic():    #대각선 방향 물이 있는 바구니 수가 얼마나 있나 확인
    for cloud in clouds:
        check = 0
        for i in range(4):
            nx = cloud[0] + dx[2 * i + 1]
            ny = cloud[1] + dy[2 * i + 1]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] >= 1:
                    check += 1
        graph[cloud[0]][cloud[1]] += check

for move in moves:  #받은 움직임들 하나 씩 시작
    #print('dddd')
    movement(move[0] - 1, move[1])  # 일단 1번의 구름 움직임 진행 해줌
    visited = [[0] * N for _ in range(N)]
    for cloud in clouds:    #구름 있는 지역 물의 양 1 증가
        graph[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = 1 #구름 잇는 지역 체크
    #대각선 방향의 바구니 수 체크한 후 거기에 그만큼 물 추가
    magic()
    #print(1111)
    #print(clouds)
    clouds.clear()       #구름을 다 지웟음
    #이제 구름을 어떻게 이동시킬지 생각하자
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] >= 2:
                clouds.append([i, j])
                graph[i][j] -= 2

    #print(clouds)

result = 0

for i in range(N):
    for j in range(N):
        result += graph[i][j]

print(result)
