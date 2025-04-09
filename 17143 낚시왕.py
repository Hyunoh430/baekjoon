R, C, M = map(int,input().split())
shark = []
graph = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int,input().split())    #(r,c) speed, direction, 크기
    graph[r-1][c-1] = [s, d-1, z]  #상어의 위치와 크기 저장
#d=1 위, d=2 아래, d=3 오른쪽, d=4 왼쪽
dx = [-1,1,0,0]
dy = [0,0,1,-1]

#모든 움직임을 한후 i번째 상태면 i번째 행을 확인한다 생각하면 될듯
def change_d(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def move(graph):
    #check = 0
    #print('이거맞나요')
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            #print('현재위치',i,j)
            x, y = i, j
            if graph[x][y]:  #만약 상어가 있다면?    speed, direction, size 이렇게 정보가 잇음
                #print(1111)
                #print(x, y)
                data = graph[x][y]
                s, d, z = data[0], data[1], data[2]
                #print(x,y,[s,d,z])
                for k in range(s):  #speed동안 수행
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        d = change_d(d)
                        nx = x + dx[d]
                        ny = y + dy[d]
                    x, y = nx, ny
                #이제 이동 완료 후
                #print(x,y,[s,d,z])
                #print(1111)
                #겹치는게 있는지 확인
                if temp[x][y]:
                    #print(x, y, [s,d,z])
                    #print(x,y,temp[x][y])
                    #print(1111)
                    if temp[x][y][2] <= z:
                        temp[x][y] = [s, d, z]
                else:
                    temp[x][y] = [s,d,z]


    return temp



result = 0

for y in range(C):
    check = 0
    for x in range(R):
        #print(x, y)
        if graph[x][y]:
            #print(1111)
            result += graph[x][y][2]
            graph[x][y] = []
            graph = move(graph)
            check = 1
            break
    if check == 0:
        graph = move(graph)

print(result)